---
layout: post
title: Can Digital Authentication Reduce Corruption?
subtitle: Lessons from use of Aadhar Cards in Public Distribution System
# cover-img: /assets/img/path.jpg
# thumbnail-img: /assets/img/thumb.png
# share-img: /assets/img/path.jpg
tags:
  [
    India,
    Public Distribution System,
    Jharkhand,
    Development Economics,
    Corruption,
  ]
# author: Sharon Smith and Barry Simpson
---

<!-- # Research paper discussion series: Aadhar Cards and Corruption -->

I am experimenting with a new series, as part of which, I write about an Economics research paper. I did my PhD in Economics, and I feel that many applied Economics papers are largely telling a story, which tends to become inaccessible due to the technical jargon. Here, I intend to focus more on the story, abstracting as much as possible from the jargon, and in some cases, hoping to explain the technical terms so that you get more comfortable with these terms. As always, please let me know what you think about this idea, what you like about it, and how it could be better. Let’s get started with the first paper in this series.

The government of India uses this system called Public Distribution System (PDS) which it uses to try to ensure that everyone has food on their plate. There is a nationwide network of over 500K shops which provide food to the eligible households at prices way below the market prices. With the massive scale though, there are many opportunities for corruption here. Sometimes, these shops will keep the grains for themselves or sell them in the market. In other cases, households which are not eligible will end up taking the grains home. The shops are also known to give less quantity or charge more prices than they should be. As a result, many poor households end up not getting the grains they should be getting. By some estimates, around 41-42% of this grain nationwide was getting diverted in 2014-15.

![https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fef84434c-6cf6-4482-afc4-b8c4cc178b3e_380x285.jpeg](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fef84434c-6cf6-4482-afc4-b8c4cc178b3e_380x285.jpeg)

As you can imagine, this is a massive program with huge costs, and the government wanted to do something to reduce this huge leakage. One such proposed solution has been digitization of all transactions. Government has introduced electronic point of sale (ePOS) devices which will process and record the transactions between the dealer and the beneficiary. In another effort, government has been issuing unique identifier cards (known as Aadhar cards) in India, which are linked to biometric information (such as fingerprint scans) of an individual. By June 2019, around 1.24 billion people or 91% of the country’s population, had these Aadhar cards. The idea was simple (in theory, at least), that if you are part of an eligible household, you link this information to your Aadhar card, when you go to your assigned shop to collect your grains, you would need to verify yourself with fingerprint, the dealer would give you the required grains for the subsidized price, and the details of the sale would be sent to the central server through the ePOS device. This mechanism was called ABBA (Aadhar Based Biometric Authentication). The intent was clear: the government would be able to ensure that the eligible households got the grain through biometric authentication, they will have an idea of how much grains a shop received, and how much they distributed in total, so they could adjust or reconciliate the grains to be distributed next month. However, the critics were skeptical. They were concerned that all this would do is make it harder for eligible households to get the grains that they need. In their paper, “[Identity verification standards in welfare programs: experimental evidence from India](<https://econweb.ucsd.edu/~kamurali/papers/Working%20Papers/ABBA%20(Current%20WP).pdf>)”, Karthik Muralidharan, Paul Niehaus and Sandip Sukhtankar set out to answer whether this ABBA program achieved its objectives or not.

![https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdda829ac-eca8-4e2f-a279-74f1f3ba28a3_1200x675.jpeg](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdda829ac-eca8-4e2f-a279-74f1f3ba28a3_1200x675.jpeg)

## What is the research question

The authors are interested in two main questions here:

- What is the impact of ABBA program on corruption in the distribution of grains? They define corruption or leakage in the system as the difference between the total grains distributed by the government, and the total grains received by the eligible beneficiaries. Each month, the government distributes the grains to a dealer based on the number of eligible beneficiaries assigned to that shop. So, if the government is disbursing grains which are not being distributed to the beneficiaries, that means the difference is either going to ineligible households or being pocketed by the dealers.
- The second thing that they are studying is the impact of associated reconciliation on the quantity disbursed by the government, quantity received by the eligible households, and the associated leakage. As part of reconciliation, the government used the data that was being collected to inform how much to send to each dealer. Suppose the government sends 100 kg of rice to a particular shop every month. Now, with the digitized data, the government knows that only 80 kg is being distributed from this shop, so in coming months, they can reduce how much to send to this shop.

## Why it’s tricky to answer this question

Suppose we could find two states where one implemented this program while the other did not. One way to answer this question can be to compare the leakages of these states and see if the state with ABBA had lower leakage. Let’s say that in this comparison, we find that the state which had ABBA had lower levels of corruption, that is, eligible households were getting the grains that they were entitled to, while in the other state without ABBA, eligible households were not getting the grains that they should have. Can we conclude that the program works? Think about it, why would one state have the program and other would not? It could be that the state which is able to implement the program is generally good in implementing policies. They may have better systems to ensure people are able to link their eligibility to Aadhar card, they may generally have lower levels of corruption to begin with, even without ABBA. This would mean that our comparison is not really that useful: we can’t say for sure whether this lower corruption is a result of the program, or more of an indicator of why they were able to implement the program early. This is the classic, “correlation does not imply causation” remark that you might have come across.

## How do the authors go about it then

In this paper, the authors use a Randomized Experiment to estimate the impact of ABBA. Essentially, what this means is that, which place gets ABBA and which place doesn’t get ABBA is randomly drawn. You can imagine it as taking a place, flipping a coin, if you get Heads, the place gets ABBA, if you get Tails, the place doesn’t get ABBA, and you move on to the next place; or you can also think of it as writing down names of all places, one each on a small sheet of paper, and then drawing some names randomly from them. By randomizing access to the program, the researchers don’t have to wonder why some places had ABBA and others did not. Here, they are ensuring that the reason some places had the program was just pure chance, and it’s not because they had lower levels of corruption or better systems in place. In other words, randomization helps in ensuring that the places with and without ABBA are similar, so we can go ahead and compare them.

In particular, the authors work with the state of [Jharkhand](https://en.wikipedia.org/wiki/Jharkhand) in 2016-17, and within that state, they randomly select some sub-districts for the program. The state government agrees to launch the program first in the sub-districts randomly selected by the researchers first, and around eight months later in the rest of sub-districts. The authors also needed a lot of data for this project. They collected data from the government about how much grain was distributed each month, which households were eligible to receive subsidized grains, which shops they were assigned to. They also conducted surveys to learn from eligible households how much grains they received.

## What do they find

For the first part, the authors find that ABBA by itself did not have much impact on average on leakage in the system for the eight months where only few sub-districts had this program. Things largely continued as they were earlier, with the paper records replaced by the digitized ones, and the paper records based verification replaced by the biometric authentication. However, while on average, there was not much impact, there were a section of households which were negatively affected. These were the households who were not able to link their eligibility to their Aadhar card, and hence, could not receive the grains they should have got. The authors’ calculations suggest that around 150,000 beneficiaries (out of 15 million total beneficiaries in the state) were denied because their eligibility was not linked to their Aadhar cards. This situation got better later, as few months later, the proportion of households who had the eligibility linked, had crossed 99%.

Reconciliation, on the other hand, had more stark effects. While the timing of introducing ABBA was randomized, the timing of reconciliation was not randomized. The government introduced the reduction in grains being sent at the same time in the entire state. Only difference was that for the areas that by design, received ABBA early, the government had more data on how much stock should have been left over with the dealers from previous months. As a result, those sub-districts received even less quantity than other sub-districts which had ABBA later. The government assumed that these dealers would have kept the undistributed grains from previous months, but that was not the case, at least, not entirely. Many dealers sent the beneficiaries back empty handed because they had not received the grains from the government. There was some reduction in leakage, that is, dealers were able to use some of previously undistributed grains, but many eligible households did not receive the grains either. By authors’ estimates, around 1.2 million beneficiaries did not receive grains as a result of reconciliation. Moreover, because government was using the data on previous distributions to anticipate the actual need in an area, some dealers made the beneficiaries ‘sign’ biometrically for more grains than they were receiving. They were using the threat that if the households don’t report receiving higher quantity of grains, the government would send less quantity next month, which would mean even less quantity for the households. All this lead to political backlash which made the government suspend reconciliation altogether.

In conclusion, the authors highlight the damage that a crackdown on corruption can cause. Even with good intentions, a policy can backfire if the implementation is not well thought out. This is also not to say that Aadhar card based authentication is not valuable long term. The authors also highlight that they study the policy in a transition period when the reform was being introduced.

<!-- ## Favorites of the month

**Movie:** [Last month](https://sagarwadhwa.substack.com/p/book-of-the-month-twelfth-fail), I wrote about the book, Twelfth Fail. I finally ended up watching the [movie](https://youtu.be/WeMJo701mvQ?si=9PeYv_Sn7_lIeJ2D) too and loved it. The character of Shraddha Joshi stands out in the book for me, and [Medha Shankar](https://en.wikipedia.org/wiki/Medha_Shankar) does incredible justice to the character in the movie too.

**Song:** Satinder Sartaaj has released a bunch of songs in the past month. While I love all of them, I have been listening to [Ulfat da sheher](https://www.youtube.com/watch?v=2qLI0u4FvYA) the most.

Until next time,

Sagar -->
