---
layout: page
title: Playground
subtitle: Small tools, experiments, and systems I've built - often with the help of generative AI.
permalink: /playground/
---

<p>
  Here are some experimental projects that I have built, for tools I personally want to use.
  Gen AI has made it possible for me to build them. Some of these are playful, some practical.
</p>

<div class="playground-grid">
  {% for project in site.data.playground %}
    {% if project.url %}
      <a class="playground-card" href="{{ project.url }}" target="_blank" rel="noopener">
        {% if project.image %}
          <div class="playground-media">
            <img src="{{ project.image }}" alt="{{ project.title }} snapshot" loading="lazy">
          </div>
        {% endif %}
        <h3 class="playground-title">{{ project.title }}</h3>
        {% if project.description %}
          <p class="playground-description">{{ project.description }}</p>
        {% endif %}
      </a>
    {% else %}
      <div class="playground-card">
        {% if project.image %}
          <div class="playground-media">
            <img src="{{ project.image }}" alt="{{ project.title }} snapshot" loading="lazy">
          </div>
        {% endif %}
        <h3 class="playground-title">{{ project.title }}</h3>
        <p class="playground-description">Link coming soon.</p>
      </div>
    {% endif %}
  {% endfor %}
</div>
