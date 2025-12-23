import os, re, pathlib, datetime, urllib.parse
import feedparser, requests
from markdownify import markdownify as html_to_md

# ========== CONFIG ==========
SUBSTACK_FEED = "https://sagarwadhwa.substack.com//feed"   # or https://substack.com/feed/@your_handle
JEKYLL_ROOT   = "../"           # repo root

# Images go here (no category in path)
ASSETS_ROOT   = os.path.join(JEKYLL_ROOT, "assets", "posts")

# Map Substack tag (lowercased) -> Jekyll category folder (which contains _posts/)
CATEGORY_MAP = {
    "books": "books",
    "finance": "finance",
    "econ": "econ_research",
    "economics": "econ_research",
    "research": "econ_research",
    # add/adjust as you like
}
DEFAULT_CATEGORY = "misc"   # -> misc/_posts
FORCE_CATEGORY   = None     # e.g., "finance" or None

# Only import entries strictly AFTER the max existing date found in *_/ _posts
RESPECT_MAX_EXISTING_DATE = True

MAX_POSTS = 50
TIMEZONE_OFFSET_HOURS = 0  # adjust if needed to align dates
# ===========================


def ensure_dir(p):
    pathlib.Path(p).mkdir(parents=True, exist_ok=True)

def dt_from_struct(tm_struct):
    return datetime.datetime(*tm_struct[:6]) + datetime.timedelta(hours=TIMEZONE_OFFSET_HOURS)

def slug_underscored(text):
    s = text.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE)  # keep letters/digits/_/space/hyphen
    s = re.sub(r"[\s-]+", "_", s)                     # spaces/hyphens -> underscores
    s = re.sub(r"_+", "_", s)
    return s[:120].strip("_")

def extract_images(html):
    return re.findall(r'<img [^>]*src=["\']([^"\']+)["\']', html, flags=re.IGNORECASE)

def safe_filename_from_url(url):
    name = os.path.basename(urllib.parse.urlparse(url).path)
    if not name:
        name = "image"
    root, ext = os.path.splitext(name)
    if not ext:
        ext = ".jpg"
    root = slug_underscored(root)
    return (root or "image") + ext.lower()

def download_image(url, dest_dir):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        fname = safe_filename_from_url(url)
        with open(os.path.join(dest_dir, fname), "wb") as f:
            f.write(r.content)
        return fname
    except Exception as e:
        print(" image download failed:", url, e)
        return None

def choose_category(substack_tags):
    if FORCE_CATEGORY:
        return FORCE_CATEGORY
    for t in (substack_tags or []):
        key = (t or "").strip().lower()
        if key in CATEGORY_MAP:
            return CATEGORY_MAP[key]
    return DEFAULT_CATEGORY

def to_front_matter(title, subtitle, tags):
  import json
  title_json = json.dumps(title or "")
  subtitle_json = json.dumps(subtitle or "")
  tags_json = "[" + ", ".join(json.dumps(t) for t in (tags or [])) + "]"
  return (
  "---\n"
  "layout: post\n"
  f"title: {title_json}\n"
  f"subtitle: {subtitle_json}\n"
  f"tags: {tags_json}\n"
  "---\n\n"
  )

# def to_front_matter(title, subtitle, tags):
#     tags_yaml = "[" + ", ".join(f"\"{t}\"" for t in (tags or [])) + "]"
#     return (
#         "---\n"
#         "layout: post\n"
#         f'title: "{(title or "").replace("\"", "\\\"")}"\n'
#         f'subtitle: "{(subtitle or "").replace("\"", "\\\"")}"\n'
#         f"tags: {tags_yaml}\n"
#         "---\n\n"
#     )

def convert_html_to_markdown(html):
    md = html_to_md(html, heading_style="ATX", strip=["script", "style"])
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip()

def get_entry_html(entry):
    if "content" in entry and entry.content:
        return entry.content[0].value
    if hasattr(entry, "summary_detail") and entry.summary_detail:
        return entry.summary_detail.value
    return getattr(entry, "summary", "") or ""

def get_entry_subtitle(entry):
    for k in ("subtitle", "sub_title", "deck", "description"):
        v = getattr(entry, k, None)
        if v:
            return v
    summary = getattr(entry, "summary", "") or ""
    clean = re.sub("<[^>]+>", "", summary).strip()
    return clean[:180] if clean else ""

# ---- NEW: scan existing posts to get max existing date (YYYY-MM-DD in filename)
POST_NAME_RE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})-.*\.(md|markdown)$", re.IGNORECASE)

def all_posts_dirs(root):
    dirs = []
    root_posts = os.path.join(root, "_posts")
    if os.path.isdir(root_posts):
        dirs.append(root_posts)
    # any immediate subdir that has _posts
    for name in os.listdir(root):
        p = os.path.join(root, name, "_posts")
        if os.path.isdir(p):
            dirs.append(p)
    return dirs

def max_existing_post_date(root):
    """
    Returns a datetime.date of the latest date found in filenames like YYYY-MM-DD-*.md
    across all *_/ _posts folders. Returns None if no posts exist.
    """
    max_dt = None
    for d in all_posts_dirs(root):
        try:
            for fn in os.listdir(d):
                m = POST_NAME_RE.match(fn)
                if not m:
                    continue
                y, mo, da = map(int, m.groups()[:3])
                try:
                    dt = datetime.date(y, mo, da)
                    if (max_dt is None) or (dt > max_dt):
                        max_dt = dt
                except ValueError:
                    pass
        except FileNotFoundError:
            continue
    return max_dt
# ---------------------------------------------

def main():
    ensure_dir(JEKYLL_ROOT)
    ensure_dir(ASSETS_ROOT)

    # Determine the cutoff date if respecting existing content
    cutoff_date = max_existing_post_date(JEKYLL_ROOT) if RESPECT_MAX_EXISTING_DATE else None
    if cutoff_date:
        print(f"Max existing post date found: {cutoff_date.isoformat()} (will import only newer)")

    feed = feedparser.parse(SUBSTACK_FEED)
    entries = feed.entries[:MAX_POSTS]

    for e in entries:
        # Determine publish date
        tm = (
            e.published_parsed if hasattr(e, "published_parsed") and e.published_parsed
            else e.updated_parsed if hasattr(e, "updated_parsed") and e.updated_parsed
            else datetime.datetime.utcnow().timetuple()
        )
        date_dt = dt_from_struct(tm)
        date_prefix = date_dt.strftime("%Y-%m-%d")
        entry_date = date_dt.date()

        # Respect cutoff: ONLY strictly newer than max existing date
        if cutoff_date and entry_date <= cutoff_date:
            print(f" skip older/same-date: {date_prefix}  {getattr(e, 'title', 'Untitled')}")
            continue

        title = e.title if hasattr(e, "title") else "Untitled"
        tags  = [c.term for c in getattr(e, "tags", [])] if hasattr(e, "tags") else []
        subtitle = get_entry_subtitle(e)
        category = choose_category(tags)

        posts_dir = os.path.join(JEKYLL_ROOT, category, "_posts")
        ensure_dir(posts_dir)

        slug = slug_underscored(title)
        md_filename = f"{date_prefix}-{slug}.md"   # underscores in slug
        md_path = os.path.join(posts_dir, md_filename)

        # Also skip if exact file already exists
        if os.path.exists(md_path):
            print(" skip existing file:", os.path.relpath(md_path, JEKYLL_ROOT))
            continue

        # Fetch & rewrite content
        html = get_entry_html(e)

        # Download images to assets/posts/<YYYY-MM-DD-slug>/
        dated_slug = f"{date_prefix}-{slug}"
        post_asset_dir = os.path.join(ASSETS_ROOT, dated_slug)
        ensure_dir(post_asset_dir)

        url_map = {}
        for img_url in extract_images(html):
            if img_url.startswith("data:"):
                continue
            local_name = download_image(img_url, post_asset_dir)
            if local_name:
                url_map[img_url] = f"/assets/posts/{dated_slug}/{local_name}"

        # Replace HTML img src with local paths
        def repl_src(m):
            src = m.group(1)
            return f'src="{url_map.get(src, src)}"'
        html = re.sub(r'src=["\']([^"\']+)["\']', repl_src, html)

        md_body = convert_html_to_markdown(html)
        fm = to_front_matter(title=title, subtitle=subtitle, tags=tags)

        with open(md_path, "w", encoding="utf-8") as f:
            f.write(fm + md_body + "\n")

        print(" wrote:", os.path.relpath(md_path, JEKYLL_ROOT))

if __name__ == "__main__":
    main()
