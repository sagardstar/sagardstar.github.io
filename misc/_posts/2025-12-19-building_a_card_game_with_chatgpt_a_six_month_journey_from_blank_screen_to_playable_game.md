---
layout: post
title: "Building a Card Game with ChatGPT: A Six-Month Journey from Blank Screen to Playable Game"
tags: []
---

I’ve always admired software engineers who can just _make_ things. People who built apps in their spare time, the two creators who came together to create [Obsidian](https://obsidian.md/), transforming how people take notes, developers casually mentioning they “threw together a tool” over the weekend. It seemed like a superpower I’d never possess. I know basic Python, but building an actual application felt firmly out of reach.

Then ChatGPT arrived, and my social media feeds filled with stories of non-coders building remarkable things. One post particularly caught my attention: [Scott Cunningham](https://www.scunning.com/), an Economics professor I follow on Substack, had created a sophisticated goal-tracking website for himself, complete with a reward system using ChatGPT. He wasn’t a software engineer either. The phrase “vibe coding” started appearing in my feeds—people with minimal coding knowledge building functional applications with AI assistance.

Maybe, I thought, I could try too, maybe.

## **The Motivation**

My interest wasn’t purely experimental either, I had a genuine need for a tool too. For years, I’ve been playing 250, a card game I discovered during my PhD days. Unlike most four-player card games where partners are fixed throughout, 250 constantly shuffles partnerships. This dynamic nature keeps things fresh and, crucially, reduces the rivalries that can sour game nights.

The problem was that 250 requires exactly four players in the same physical space. Living far from friends, dealing with conflicting schedules, or simply bad weather often meant we couldn’t play. I checked online—there was no digital version anywhere. I thought maybe if I could build something, it would allow us to play more regularly.

Armed with my ChatGPT Plus subscription and buoyed by all those success stories, I started at it. ChatGPT, as it usually does, enthusiastically agreed it was possible and could be done soon enough. Maybe a few hours, and I’d surprise my wife with a working game, I thought. I explained the set up through a series of prompts. It suggested what kind of files we would need to have it up and running. It guided me through creating files, pasting code, setting things up. Everything seemed to be going smoothly. I thought this was super fun and super easy. “Now your game is ready, give it a go” it finally announced. “You should be able to run it locally.”

I ran it.

Blank screen. No cards, nothing. Just errors in terminal I didn’t understand, talking about JavaScript and HTML—languages I’d never learned and couldn’t distinguish between.

[![](/assets/posts/2025-12-19-building_a_card_game_with_chatgpt_a_six_month_journey_from_blank_screen_to_playable_game/https3a2f2fsubstack_post_medias3amazonawscom2fpublic2fimages2fd58539bd_c0a1_4ce1_89e5_037f2db2c02a_2816x1536.png)](https://substackcdn.com/image/fetch/$s_!1lra!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd58539bd-c0a1-4ce1-89e5-037f2db2c02a_2816x1536.png)

Created using Gemini

## **A Different Starting Point**

That blank screen was not very encouraging, to say the least. Maybe this wasn’t _that_ easy after all. Rather than surprising my wife with a functional game, I turned to her for help, as she has a PhD in Computer Science. She looked at my approach and immediately redirected me. “Don’t start with the UI,” she said. “Build a command-line version first. Get the game logic working in the terminal before you worry about cards showing up.”

This was my first real lesson: the path ChatGPT and I had chosen—jumping straight to a visual interface with cards displaying in Chrome—was putting the cart before the horse. We needed to walk before we could run. But because I had no idea how any of this worked, I thought this should be possible straight away.

With her guidance on debugging and my continued reliance on ChatGPT for implementation, we finally got a terminal version working. No graphics, just text. But the cards dealt, the game progressed, and something _worked_. That first small victory restored my hope.

## **The Bidding Problem**

With the basic structure in place, we tackled the game’s most complex feature: bidding. In 250, bidding isn’t straightforward. One player opens with a bid or passes. The next player can raise or pass. But if they raise, the action returns to the previous player, who can match or raise or pass. It’s a back-and-forth negotiation that needs careful logic.

This is where ChatGPT and I hit a wall. I’d paste an error message. ChatGPT would _extremely_ confidently suggest a fix. I’d implement it. Same error, or a new one. Repeat. And repeat. ChatGPT never ran out of suggestions, and I wasn’t running out of errors. I tried different, allegedly more advanced models ChatGPT offered, but the errors still remained.

My wife tried working with ChatGPT herself on this section. After several frustrating rounds, she declared she’d just code it herself. When she finished, it worked—fewer lines, cleaner logic, exactly what we needed. “You just need to code everything on your own,” she told me. “Working with ChatGPT is too frustrating.”

For her, having studied (and taught) Computer Science for years, it was probably faster to write it from scratch than to wrestle with ChatGPT’s suggestions. But for me? Without ChatGPT, there would be no game. I had no ability to code the bidding logic—or anything else related to the game—on my own. Either ChatGPT helped me build this, or it wouldn’t get built at all.

Then I had an idea. I took her working code and fed it back to ChatGPT. “Here’s code that implements the bidding correctly,” I told it. “Can you integrate this into the rest of our game?” It worked. ChatGPT could understand the working code and weave it into our existing structure. The bidding logic finally functioned. I immediately saved that version (in two places so that it wouldn’t get lost)—at least this crucial piece was solid.

I realized this pattern: ChatGPT struggled to create complex features from my verbal descriptions, but it could work with concrete code and clear examples to implement.

## **The Context Problem**

A major challenge emerged as the codebase grew: ChatGPT could only “see” one file at a time. It would suggest a fix for one file without knowing how it would affect others. I’d fix something in the game logic only to break the card display. The frustration of this back-and-forth loop was real—ChatGPT confidently suggesting solutions to problems it didn’t fully grasp because it lacked context.

Things improved somewhat when I started using the ChatGPT Mac app, which could access my terminal and make edits in VS Code. But it still couldn’t see the full picture of our multi-file project.

Then, around August (around four months after I had started building the game), I discovered [Codex by ChatGPT](https://openai.com/index/introducing-codex/). The key difference was that Codex could read my entire [GitHub](https://github.com/) repository. Suddenly, it understood how the pieces fit together. Progress accelerated. Fixes made sense. Features worked together rather than breaking each other.

All this time, life continued—including our little one growing up. Progress was remarkably slow, measured in whatever fragments of time I could find. What I’d imagined (mistakenly) as a weekend project stretched into months.

## **Testing in Four Windows**

Before we could play online, I had to test locally. This meant opening four different Chrome windows, each representing a player, and playing every hand myself. I’d bid for all four players, then play through all 52 cards, then check if the scoring worked correctly. But the game is actually not just one round of 52 cards and 250 points. It actually runs till one player reaches 1000 points, so it continues for multiple rounds. After implementing that, testing became even more painful, as now I had to play all the cards from four windows for multiple rounds to verify things were working correctly. I thought it would be so much better if I could get four people to join the game, and play it out, and then see if everything was working as it should. But that wasn’t possible as the game only worked locally and was not being hosted anywhere.

## **Going Online**

I once again turned to ChatGPT: “How do I host this game online, but free?” I was clear about not wanting another monthly subscription. The first two suggestions turned out to be outdated—those platforms had discontinued their free tiers. The third suggestion, though, worked: [Render.com](https://render.com/) still offered free hosting. After some more roadblocks along the way, I had a deployed game. The game was available online for players to join on render.

## **First Game Trial**

When I invited friends who knew the game to test it out, the first online playtest felt less like playing and more like giving a live demonstration. As soon as we started, my friends spotted issues: “The bids are not updating. The scores are not correct. The cards aren’t showing up right in this orientation.” It was exciting—something I’d built was real enough to play!—but also nerve-wracking. I couldn’t just enjoy the game; I was presenting a project, waiting to see what would break, and taking notes on the suggestions. It was so much better though to test the game this way and find things which needed fixing.

The second playtest went better. By then, I’d fixed several bugs through more Codex sessions. The game flowed more smoothly. My friends could actually play without constant interruptions. They also seemed genuinely impressed. “You built this in JavaScript and HTML?” they asked. “Yes,” I admitted. “Though I still can’t really explain the difference between them.”

[![](/assets/posts/2025-12-19-building_a_card_game_with_chatgpt_a_six_month_journey_from_blank_screen_to_playable_game/https3a2f2fsubstack_post_medias3amazonawscom2fpublic2fimages2fd4fa18c3_b600_40c7_ad36_fd55cc8bed3f_3024x1212.png)](https://substackcdn.com/image/fetch/$s_!telg!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd4fa18c3-b600-40c7-ad36-fd55cc8bed3f_3024x1212.png)

Current UI of the game

## **What I Learned**

This journey on creating this game with Gen AI has been fun. An expert could probably code it up themselves much faster and much more efficiently. But for me, the tool made it _possible_ to have something running.

The learning curve was also steep. I discovered how to run local versions of applications, navigate GitHub, and debug JavaScript errors using Chrome Developer Tools. I learned to distinguish between game logic problems and code syntax issues. Some of this was genuine learning; some was brute-force trial and error until something worked.

I also feel working with a tool like ChatGPT pays off best when you have context knowledge. When my wife looked at error messages, she immediately knew which file to check and what to fix. When I saw the same errors, I was trapped in a loop—copying and pasting messages into ChatGPT, trying suggestion after suggestion, with no mental model of what was actually broken. Even then I feel, things would have been even more challenging for me had I not had even the basic knowledge of Python. While there are parts that handle the user interface in other languages, the core logic of the game is coded in Python. So, I could at least verify some things if not all.

The tools keep evolving too. What ChatGPT couldn’t handle six months ago—understanding a full codebase, making coherent changes across multiple files—Codex can do now. In another six months, it will likely be even easier. I haven’t tried other platforms like [Lovable](https://lovable.dev/?utm_feeditemid=&utm_device=c&utm_term=lovable&utm_source=google&utm_medium=ppc&utm_campaign=US+-+Search+-+Lovable+-+CORE&campaignid=23072209374&devicetype=c&gclid=Cj0KCQiA6Y7KBhCkARIsAOxhqtNtudRW8MIENE3oc3ZCR5yxwFN22Ain1BtCHIDX-vZcLqcfZFJhR1AaAmz4EALw_wcB&creativeid=777017041384&gad_source=1&gad_campaignid=23072209374&gbraid=0AAAAA-iIxGcsvR4U3m2QThCJuC-f3_IZ8&gclid=Cj0KCQiA6Y7KBhCkARIsAOxhqtNtudRW8MIENE3oc3ZCR5yxwFN22Ain1BtCHIDX-vZcLqcfZFJhR1AaAmz4EALw_wcB) or [Claude’s](https://claude.ai/) coding features, but apparently, they are even more suitable for such vibe-coding projects.

The game still has bugs. The UI could be much better. Sometimes it breaks in ways I haven’t figured out yet (though Codex helped me add a fix we haven’t tested). But it works. Any group of four people can go to the URL: <https://card-game-250.onrender.com/>, enter a common room number, and play 250 together from different cities or countries, and I would have never thought a year ago that I could build it.

If you’ve ever looked at builders and thought “I wish I could make something,” this might be your moment too. The technology isn’t perfect. You’ll face frustration. Things will break in confusing ways. You might spend six months on what you thought would be a weekend project. But you also might end up with something real. Something that works. Something that didn’t exist before.

Until next time,

Sagar
