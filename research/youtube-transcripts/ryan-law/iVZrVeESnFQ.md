# How to automate blog writing with AI

- Video URL: https://www.youtube.com/watch?v=iVZrVeESnFQ
- Author: ryan-law
- Fetched: 2026-07-04
- Provider: free

## Transcript

[0.0s] Soryan, I was thinking today, it didn't
[2.8s] take us too long to go from this AI
[6.2s] thing cannot really do great content to
[8.9s] oh my god, this is amazing, right? And
[11.6s] here we are.
[13.0s] You have devised an AI content
[16.6s] automation workflow that you used to
[18.7s] actually publish quite a few articles on
[20.2s] HRF's blog already, and these are good
[23.0s] articles. These are great articles.
[25.2s] And yeah, full disclosure, I haven't
[27.5s] seen it yet, so I'll be checking it out
[30.0s] live together with anyone watching it.
[33.0s] And I'm excited. Yeah. Do you want to
[35.1s] say a few quick words on what people are
[37.3s] about to see?
[39.0s] >> Yeah, well, exactly that. So, we've
[40.9s] obviously been tinkering with using AI
[43.0s] in our content workflows for years at
[45.7s] this point. And it's always been very
[47.6s] effortful. It could be helpful, but you
[49.5s] have to sink a ton of time and energy
[51.1s] into it. There's still a lot of manual
[52.5s] stuff that has to happen.
[54.3s] I kind of feel like that's not the case
[55.6s] anymore. Uh it's a bit spooky, actually.
[57.9s] I think since Claude code is probably
[59.5s] the big thing that has changed this.
[61.6s] This kind of agentic workflow where
[63.4s] Claude can make some decisions on your
[65.3s] behalf, and you can provide it with some
[67.3s] guardrails to actually make it do things
[69.6s] in a certain way.
[71.2s] Um so, we've basically, yeah, built I
[73.7s] call it the blog pipeline.
[76.0s] Uh and it is a kind of content
[77.4s] automation system for new articles and
[79.6s] for content updates.
[81.3s] Uh we've done maybe like 30 article
[83.8s] updates with it so far.
[85.8s] Uh published maybe 10 15 articles. Got
[89.6s] maybe something similar in progress at
[91.7s] the moment. Um
[93.9s] yeah, it's been pretty cool.
[94.9s] >> Let's Let's Let's review it. Show it to
[96.6s] me.
[97.1s] >> Yeah, let's do it. Um so, obviously two
[99.5s] things on the screen right now. We have
[101.2s] a terminal and we have Claude code
[104.1s] running in that terminal. So, that is
[105.5s] just a folder that I've called blog
[107.4s] pipeline and Claude code is living in
[109.7s] that folder and it will do stuff in that
[111.5s] folder for me when I ask it to.
[114.0s] Um and we've got VS code over here. This
[116.1s] is just a really good way of showing you
[117.6s] the contents of that folder in a way
[119.4s] that is a bit easier to understand.
[121.6s] Uh these are all the folders on the
[123.7s] left-hand side and they've all got files
[125.3s] inside them.
[127.1s] And I of course I asked Claude I said
[129.9s] I'm going to present this process on a
[131.4s] podcast with Tim. Give me some notes and
[133.6s] visualizations to help explain this so
[135.6s] it added a handy little podcast folder
[137.5s] here
[138.4s] uh that has some notes and
[139.4s] visualizations to make this a bit more
[141.9s] interesting.
[144.0s] But the basic premises
[145.9s] uh
[147.1s] we have basically set it up such that
[148.8s] there are maybe 23 or so uh skill files
[152.9s] in here. You can see them in this
[154.2s] folder.
[155.7s] Uh and what is a skill?
[156.9s] >> skill files? That's That's a lot.
[159.4s] >> That is a lot.
[161.1s] Um and each of these skill files is
[162.7s] basically a process. It is a process
[165.0s] that at some point during creating
[166.6s] content or updating content as a human
[169.0s] we generally do something like this or
[171.1s] very similar to this.
[172.8s] Um and this is just a markdown document
[175.6s] with very simple instructions.
[177.2s] >> lost me already. I I kind of know what
[179.4s] skills are but you lost me already.
[180.9s] Let's start from the beginning. Where
[182.5s] does the process start? What do we start
[184.5s] from? Do we start from a keyword? Do we
[186.0s] start from an idea? What's the first
[187.6s] step with this?
[188.6s] >> Yes.
[190.0s] Uh so what you can do is So this is a
[192.5s] keyword ideas CSV.
[194.6s] Um so it's obviously a bit hard to see
[196.2s] in this format.
[197.9s] But basically we've even set up a a
[200.4s] process right now where we can use the
[202.7s] Ahrefs MCP which is obviously a way for
[205.2s] Claude and other to access Ahrefs data
[208.4s] and it will run a content gap analysis
[210.3s] for us.
[211.7s] And I've then set up another process
[213.2s] where it will review this list of
[214.4s] keywords and prioritize them.
[216.9s] Uh it looks at
[217.8s] >> Ryan, again, let me uh use my Eastern
[220.4s] European politeness uh to bring you
[223.2s] right to the point. We're not talking
[224.3s] about keyword research. We're talking
[225.6s] about creating content. So let's say we
[227.8s] have a keyword or a topic. Uh what do do
[230.2s] with it? We're not We're not talking
[231.3s] about keyword research. We want to
[232.5s] create content.
[234.1s] >> All right, let me show you then.
[235.6s] Let me
[236.3s] clear this.
[238.4s] >> [snorts]
[241.9s] >> Uh so, I can trigger blog pipeline. I
[244.3s] can put in a keyword like keyword
[246.3s] opportunities.
[248.8s] And if I want, I can add some context to
[251.1s] it and explain, you know, if there are
[252.3s] points I want to add, I can add that.
[255.1s] And off Claude goes.
[257.2s] And probably somewhere from between 8 to
[259.2s] 11 minutes from now, it will have a
[261.3s] draft ready for review.
[263.2s] Um it goes through, yeah, about 12 steps
[266.9s] at this point, as you can see.
[269.8s] >> Oh, wow.
[270.5s] >> It's actually It's actually telling me
[271.6s] we've already It's so clever. It's not
[273.5s] letting me do the same one that we've
[275.1s] already done before.
[277.2s] Um so, there's a research step. There's
[279.4s] a reference step where it looks at
[280.8s] existing articles on the Ahrefs blog.
[283.5s] There's an outlining step where it turns
[285.3s] that into a structured outline.
[287.4s] There's a like product annotation stage
[289.8s] where we look for opportunities to
[291.4s] mention specific Ahrefs products.
[294.0s] There is a drafting phase, a citation
[296.6s] phase for internal linking and finding
[298.7s] supporting sources.
[300.4s] There's a screenshot phase which doesn't
[301.8s] work very well, but we're working on
[303.4s] that.
[304.2s] Uh a preview phase where you can
[305.9s] actually preview how it would look on
[307.6s] the blog. Uh and then a formatting for
[309.8s] publish phase where it will add in all
[311.9s] the WordPress shortcodes, all that kind
[313.4s] of stuff we need.
[315.2s] Um
[316.4s] >> Hm, so basically, when you when you ask
[318.9s] it to create uh a a piece of content
[321.6s] around a given keyword,
[323.6s] you are essentially uh launching a
[326.5s] skill,
[327.8s] which is a combination of steps where
[331.0s] each step is
[333.0s] uh a separate skill.
[335.1s] And basically, it has to finish them one
[337.0s] by one, or how does it work?
[340.5s] >> Exactly that, yeah. So, what you can
[342.8s] either trigger the skills individually.
[344.4s] So, if you just want an outline, you can
[345.9s] just ask for an outline by triggering
[347.4s] that skill. But, I've created these kind
[349.4s] of master skills, and they are very
[351.3s] simple. They exist just to tell Claude
[353.3s] to work through the other skills in a
[355.1s] particular order.
[356.6s] Um so, this one's called blog pipeline,
[358.3s] and there's also update pipeline.
[360.7s] Uh and they literally, yeah, just stitch
[362.2s] them together and make Claude
[363.7s] systematically work through these
[365.2s] processes.
[366.0s] >> Okay.
[367.1s] Uh
[367.8s] let me go straight into the
[371.0s] uh
[371.8s] phase of being critical of this. Uh
[375.5s] how is this not a slope? So, what makes
[378.3s] this process produce good content and
[381.2s] not some generic stuff?
[385.1s] >> Yeah. So, that's a very good question. I
[387.7s] think this definitely works best, for
[389.4s] one thing, on topics that we have
[391.2s] already covered in some capacity on the
[394.1s] Ahrefs blog. Um so, one we published
[397.2s] recently, content gap.
[399.4s] We have never written an article about
[401.0s] content gap spec- What was it? Keyword
[403.4s] gap? One of these two. Content decay and
[405.1s] keyword gap. We've written loads about
[407.0s] these concepts generally, but in
[408.7s] slightly different contexts. But, we've
[410.8s] never specifically targeted that
[412.3s] keyword.
[413.5s] But, because this uh is able to go and
[415.3s] look up existing Ahrefs articles and
[417.7s] anchor the content generation process in
[420.2s] what we've already written, uh that goes
[423.1s] a long way to getting rid of a lot of
[424.6s] the problems you'd have.
[426.3s] Um
[427.4s] and there are also some topics, I think,
[429.6s] I'm mainly using this for very
[430.9s] straightforward informational topics,
[433.0s] things that the LLMs know a lot about.
[435.8s] Um there are opportunities for you to
[437.8s] provide some context in it. Uh there's a
[440.4s] particular step in here that looks for
[442.5s] um opportunities to add information
[444.3s] gain. So, it actually reads the
[445.7s] top-ranking articles, summarizes the
[448.2s] contents of them, and makes suggestions
[450.7s] for ideas that are not covered, but
[452.2s] would be useful for the reader to
[453.4s] understand within this.
[456.0s] And I think AI is better at research
[458.5s] than a person is, as well.
[460.2s] Um it can be faster and more systematic
[462.0s] about it. It can go out and look up, uh,
[464.3s] you know, the latest research articles,
[465.8s] the latest stats, all these kinds of
[467.3s] things.
[468.0s] >> Okay, so we definitely cannot go
[470.8s] through, uh, all of your skills, uh, in
[473.4s] the course of this podcast episode
[475.6s] because there is a lot of, uh, a lot of
[477.5s] content in each of the skills. But, I
[479.6s] want you to, uh,
[481.8s] start from the very first step of
[484.2s] creating content and then go to the
[485.9s] second and third and highlight maybe one
[489.0s] or two kind of counter-intuitive things.
[492.0s] So, for example, what what might people
[494.2s] get wrong if they would want to kind of
[496.7s] recreate your process? Because, uh, I'm
[499.0s] not sure that we want to just, uh, give
[500.8s] out your process to everyone else if we
[502.7s] want just like open source it and have
[504.9s] everyone else have access to the same
[506.4s] process. And I would imagine that people
[508.2s] would want to,
[509.8s] uh, make it uh, personal to to them and
[513.2s] their voice and their blog and the style
[515.0s] of content that they want. But, yeah,
[516.8s] walk me through each step and tell me if
[519.4s] you uncovered
[522.2s] anything interesting about uh, giving
[526.3s] instructions to AI on how to kind of
[530.0s] improve the output of this specific
[532.0s] step, if you know what I mean.
[533.2s] >> Yeah, yeah, yeah. So, well, you made a
[535.4s] very good point there as well. I think
[537.3s] the way we are using this is not as
[538.9s] though this is the universal process
[541.1s] that everyone in the team has to follow.
[543.3s] Um, we've actually set it up such that
[545.3s] the team can fork their own versions of
[547.6s] this repo, so they can make their own
[549.6s] version of this folder and they can
[551.4s] modify it how they like. This version
[553.9s] has examples of content that I like and
[556.2s] my writing voice and it's used as part
[558.4s] of the article generation process. It
[560.3s] would be super weird if SQ or Louise,
[563.0s] uh, did the same thing, used my writing
[564.8s] voice for their articles. So, it's very
[567.2s] easy to actually update it and
[568.2s] personalize it. And part of that might
[570.2s] be changing the steps it goes through,
[571.8s] your own personal preferences. Um, this
[574.6s] is kind of very unique to me, I think,
[576.4s] and that's I kind of, I think, how they
[578.2s] should be used.
[579.9s] Um, another good point as well, you said
[582.4s] you were surprised at how many steps
[584.0s] there were in this process. I think that
[585.6s] is actually a very, very good thing.
[588.1s] Um,
[589.2s] the more steps you create, the more kind
[592.4s] of introspection you have into the
[593.7s] process, the better you understand it,
[595.9s] uh, the more opportunities you have to
[597.4s] actually control and personalize how the
[599.4s] content turns out.
[601.2s] So, one very important thing I learned
[602.8s] very quickly,
[604.2s] obviously I could just set this process
[606.2s] in motion and it would give me an
[608.0s] article in 8 minutes, and either it's
[610.0s] good or it's bad, it's quite hard to
[612.2s] work out how to fix and improve the
[613.6s] process if you do that. So, actually, at
[616.3s] every single step of the process, um,
[619.5s] you can actually see it it will give me
[621.2s] an output at every stage. So, if
[623.4s] something goes wrong, if I don't like
[625.0s] the article or how it turned out, I can
[626.5s] go back and see uh, which part of the
[628.5s] process it didn't work very well.
[631.4s] >> I'm actually surprised that when you
[633.5s] initially tried to launch this process,
[636.1s] you said that you would wait like 8 to
[638.1s] 12 minutes, because I was expecting that
[640.7s] you would actually baby sit it from step
[643.9s] to step, so you would see the output of
[645.7s] the first step, see if you want to
[647.6s] refine it, if if it's according to your
[649.4s] expectations, and then allow it to go to
[652.0s] the second step, but it's all just
[653.8s] batched for you. And the thing is
[656.0s] that that's actually an interesting tip.
[657.8s] This is exactly what I was looking for,
[659.3s] some tips for people of,
[661.9s] uh, what they need to look for when
[663.1s] they're building this themselves. And
[665.0s] the tip is make sure that the process
[667.7s] saves the output of the step, so if you
[670.3s] don't like the final thing, you can go
[672.8s] step by step and review at which step
[675.3s] kind of it went sideways, so that you
[678.1s] could, uh, like give it more
[679.5s] instructions or refine the the skill
[682.1s] that that refers to the step, uh, and
[684.6s] make it, uh, do over again and see if
[687.2s] that would help. But yeah, I'm surprised
[689.2s] that, uh, you let it run for like 8 to
[692.4s] 12 minutes. Is this the point that you
[695.2s] trust it well enough, you like your
[697.0s] steps? Or yeah, probably it's that. I
[700.4s] don't see any other reason why would you
[702.0s] would just let it cook for so long and
[703.9s] follow all the steps.
[705.1s] >> Yeah, great point. Very importantly,
[707.0s] this is
[708.4s] uh actually months and months of
[710.5s] refinement has gone into this thinking
[712.2s] in the process in here. And actually,
[714.0s] the last podcast episode we talked about
[715.8s] where we had the custom GPTs,
[718.4s] it was like the kind of baby version of
[720.0s] this process. So, a lot of the skills I
[721.5s] have in here are things that we improved
[724.0s] and refined and did handhold and babysit
[727.1s] as part of that process. So, we'd
[729.0s] already written these, already tested
[730.4s] these, already made dozens and dozens of
[732.3s] article outputs with them and kind of
[733.9s] learned to refine them.
[735.6s] So, the thing that Claude does very well
[737.2s] is just stitching those together, um
[739.4s] actually automating that process.
[742.2s] >> Okay, let's go step by step. The first
[743.9s] step I think I see, though it is quite
[746.0s] small, is research, right? Any like one
[748.5s] or two tips to that you saw that would
[751.6s] significantly improve the output of this
[754.0s] step?
[754.5s] >> So, it does a combination of things. Uh
[756.7s] maybe most people would assume, you
[758.2s] know, keyword research is the most
[759.7s] important thing to do, and we have that
[761.2s] in here. It goes and gets a bunch of
[763.5s] Ahrefs data from the MCP, uh related
[766.3s] keywords, parent topic, all this kind of
[768.4s] thing.
[770.1s] And we don't have this yet, but I've
[771.7s] asked for it. What is more important, I
[773.6s] think, is going and looking at the
[774.8s] existing SERP, the content that is
[776.8s] ranking, and analyzing that and seeing
[779.8s] the topics that are kind of consensus
[781.9s] and commonly used there, opportunities
[783.7s] to differentiate from that.
[785.8s] Um
[787.0s] that is what AI content helper is
[788.6s] perfect for doing, but we don't have the
[790.2s] endpoint for that yet. So, this does a
[792.0s] kind of laborious manual version of
[793.9s] that.
[794.5s] >> But what is ex- what is exactly like
[796.6s] what are you asking it to do? Do you ask
[798.3s] it like
[799.4s] open the top ranking articles for this
[802.2s] keyword and what? And and read them and
[805.5s] summarize them? What do What do you ask
[807.8s] it to do? Like, give me something
[809.2s] interesting about the research step.
[811.4s] >> Yeah, let me try and find it. Here we
[813.2s] go. This is the skill file.
[817.6s] Um so, it starts with keyword ideas.
[822.3s] It gets uh primary keyword metrics and
[824.1s] parent topic. Uh it finds long-tail
[826.2s] keyword variations that share the same
[828.4s] parent topic.
[830.3s] Uh there's some prioritization where it
[832.0s] groups them together and discards ones
[833.8s] that wouldn't fit the writing 10.
[835.8s] >> [snorts]
[836.0s] >> Pulls the questions report through the
[837.6s] MCP as well, so we get commonly asked
[839.6s] questions that people might have related
[841.0s] to this topic. Groups them into question
[843.3s] themes, so we're not just doing like FAQ
[845.5s] spam.
[847.2s] Uh we get the SERP overview. We use that
[849.8s] to go and look at the type of content
[851.4s] that is ranking, the estimated traffic,
[853.2s] all these kinds of things.
[854.8s] Uh analyze the dominant search intent of
[856.9s] the SERP results, so we can see what
[858.6s] type of content performs best that's
[860.4s] kind of going into this process.
[862.6s] Uh and then it looks at the actual
[864.3s] top-ranking pages, so it uses web fetch,
[866.5s] it retrieves the content, it extracts
[868.8s] the headers, it summarizes them, it
[871.2s] looks for themes and gaps in them.
[873.6s] And yeah, creates content gaps and
[875.6s] opportunities.
[877.1s] >> [sighs and gasps]
[878.0s] >> Um and you can see an example of the
[879.6s] kind of output. So, it basically creates
[881.2s] a report, like a research report at this
[882.9s] step. I don't have to see this, but this
[885.2s] is what gets fed into Clawed at the next
[887.0s] stage of the process.
[888.8s] Uh so, you've got loads of keyword data,
[890.2s] questions to answer, organic results.
[893.1s] Uh
[893.7s] >> You know what? At this point, as I'm
[895.8s] looking at how
[897.8s] detailed and sophisticated these steps
[900.2s] are,
[901.4s] I want to say the word over-engineered.
[905.0s] >> Mhm.
[905.4s] >> I'm actually wondering if you would like
[907.3s] remove half of that, would it just do
[910.6s] as good of a job?
[913.3s] >> Yeah, quite possibly. And that's another
[915.1s] really important part of this process.
[917.2s] Um
[918.3s] I'm always surprised at how good,
[920.0s] increasingly, the most like uh frontier,
[922.2s] most up-to-date models actually are on
[924.5s] their own without any input. Um so a big
[927.8s] part of the testing and iteration we've
[929.4s] been doing is to we've actually been
[931.5s] writing um like test cases. We've been
[934.7s] following this these steps with the
[937.0s] skill file and without it and seeing
[940.1s] whether the without version is actually
[941.8s] good enough. Does the skill file
[943.0s] actually add any benefit to it?
[945.2s] Um
[946.3s] a good number of cases, the models do a
[948.3s] very good job on its own and it just
[950.2s] needs a little nudging in a particular
[952.0s] direction. So I expect as we continue to
[954.6s] improve on these, these skill files and
[956.3s] these outputs will just get simpler and
[958.1s] simpler over time until they're
[959.8s] distilled down to the handful of things
[961.4s] that are very important for getting the
[963.0s] output that we want. Cuz yeah, it's
[965.1s] probably completely over-engineered at
[966.8s] this point, I think.
[968.3s] >> But again, my brain wants some kind of
[971.6s] structure to what we're trying to do. So
[975.2s] the the structure I would So if I were
[978.0s] building this process myself from
[979.9s] scratch and they needed to start from
[982.0s] research of competitors and I know that
[984.4s] my competitors are the pages that are
[986.0s] ranking at the top. Uh what I would tell
[990.5s] uh AI or Claude specifically to do, I
[992.6s] would tell it to download all the
[994.3s] content in the folder
[996.7s] and then yeah, I would I would ask it to
[999.6s] extract from each piece of content kind
[1002.0s] of the main themes and the main ideas
[1004.5s] and then I would ask it to
[1005.6s] cross-reference those main themes and
[1008.0s] the main ideas between the articles and
[1010.2s] create me one master document with all
[1014.4s] of the kind of ideas, stories,
[1017.1s] interesting points
[1018.8s] uh from all of the content. So my my
[1021.3s] output uh I I don't necessarily need
[1023.8s] like you had the people also ask
[1025.5s] questions and that stuff. I would just
[1027.3s] ask it to
[1028.9s] uh analyze articles and create kind of a
[1031.2s] blended master file with everything
[1034.5s] unique that is pulled from all the
[1036.0s] articles. Actually, I do a similar
[1037.5s] process right now when I when I prepare
[1039.8s] for podcast interviews with
[1042.7s] marketing leaders. What I do is I do a
[1044.6s] pretty similar thing.
[1046.5s] I give Claude their previous interviews,
[1050.2s] links to their previous interviews on
[1051.7s] YouTube. It downloads the transcript and
[1054.4s] then it creates me for each of these
[1056.8s] transcripts because I don't want to read
[1058.3s] the whole thing. I want TLDR, too long
[1060.4s] didn't read. So, I ask it extract the
[1062.5s] questions because questions are topics
[1064.7s] within the interview. And then
[1066.1s] differentiate between
[1068.0s] main questions and follow-up questions
[1070.0s] where the host is digging more into this
[1072.2s] topic. So, yeah, you know, like where
[1074.7s] the main question, where the follow-up
[1076.2s] question, and then instead of giving me
[1077.8s] the whole answer, give me TLDR, just a
[1081.2s] few sentences of what the guest replied.
[1084.0s] Give me if there was any hot take. Give
[1086.1s] me if there was any story. Give give me
[1088.1s] if there was any specific number, like,
[1090.0s] "Oh, we increased our leads by 300% or
[1093.0s] something."
[1094.6s] And I think there was something else,
[1095.9s] but I forgot about it. So, it creates me
[1098.2s] TLDR for each of the interviews and as
[1101.1s] the next step, I ask it, "Now create me
[1103.8s] a master TLDR." And this is what I would
[1107.6s] read while preparing for for the podcast
[1110.3s] interview because it would give me all
[1112.3s] the unique information from like a dozen
[1114.8s] interviews. So, it feels that when I
[1117.5s] want to create a piece of content, it's
[1119.1s] kind of the same. I want to know
[1121.1s] what has been said already by
[1124.4s] on this topic. So, this is what I would
[1126.5s] include research phase. But, yeah,
[1129.0s] you're giving it people also ask
[1131.8s] questions, parent topics, but it feels
[1134.0s] that when you say that you're extracting
[1135.9s] kind of topics from a page, it feels the
[1138.2s] same what I'm doing when I'm extracting
[1140.1s] questions that a host asked my guest and
[1143.0s] then I Do Do you also ask it to create a
[1145.0s] master document with everything?
[1148.8s] >> Uh with that is yeah, the basic that
[1150.3s] research document is the kind of um
[1153.3s] uh this is the research document it
[1155.4s] would hand over to the next step of the
[1156.6s] process.
[1158.7s] >> Okay, uh we discussed research. What is
[1160.5s] the next step?
[1162.8s] >> So, the next step
[1165.7s] uh Ahrefs references.
[1168.2s] >> So, how does how does it work?
[1170.8s] >> So, this was I actually added this very
[1172.1s] recently and this has been very helpful.
[1174.4s] Um
[1176.2s] Claude can do a good job writing an
[1177.5s] article on most topics. It can go and
[1179.3s] look up other content. That's all well
[1181.0s] and good. Um I really wanted a part of
[1182.9s] the process where, you know, as a human
[1184.8s] writer, I would go and see what we
[1186.4s] already have on a topic because I want
[1188.4s] to make sure a new article is consistent
[1190.0s] with old things we've written. I want to
[1192.0s] interlink between them. Uh I want to
[1193.9s] make sure the kind of framing is useful.
[1195.8s] I want to be efficient and make sure I'm
[1197.4s] not repeating myself. I can just pluck
[1199.9s] elements from existing articles. So,
[1202.1s] this specifically looks up the target
[1203.8s] keyword to see what we have already
[1205.4s] published on that topic, what is already
[1207.0s] ranking for similar topics, and it
[1209.6s] incorporates elements of that into the
[1213.8s] uh
[1214.3s] like outlining and generation process.
[1217.9s] >> Okay, it feels like
[1219.8s] it feels again I will try to
[1222.4s] uh
[1223.2s] explain it from my perspective. Uh I
[1225.3s] will try to kind of simplify the
[1226.7s] process. So, it feels the same as
[1229.6s] research as the first step where you
[1231.5s] take the pages where you extract kind of
[1233.8s] unique information from them and you
[1235.5s] want to understand kind of the the
[1237.3s] overall topic coverage uh as pulled from
[1240.8s] like a dozen different pages. And now
[1242.9s] what you're doing, you're referencing
[1244.7s] our own content. So, rather than
[1246.4s] searching which are the top 10 ranking
[1248.8s] pages for the topic, you're going and
[1250.8s] searching, okay, what relevant pages
[1253.4s] does Ahrefs does our website already
[1256.1s] have on this topic? And can we pull
[1258.6s] something interesting from them and
[1260.3s] again cross-reference with my master
[1262.8s] document if we're saying something
[1265.2s] unique uh that this master document is
[1267.6s] not saying and what's what's important
[1269.3s] is because our content is very product
[1271.4s] laden we try to fill our content with
[1274.3s] use cases of our tools and data.
[1277.5s] Often times the unique bits that AI can
[1280.8s] pull from our content on this topic are
[1283.2s] those use cases and you can even
[1284.8s] specifically instruct it. So you can
[1286.4s] tell Claude so specifically look for
[1288.8s] whenever we're discussing this topic,
[1290.5s] how are we
[1292.2s] teaching people to use our tools? What
[1294.1s] kind of actionable use cases we're
[1295.4s] teaching them?
[1296.8s] And then it would create you another
[1298.4s] document with like, okay, this is the
[1300.4s] master document of what all competitors
[1302.4s] are talking about this topic and these
[1304.3s] are unique insights that I saw published
[1307.8s] on your blog and here are unique I know
[1310.2s] use cases of your product that I saw in
[1313.0s] your articles on this topic. So is this
[1316.0s] more or less what you're looking for?
[1318.0s] >> Yeah, exactly that.
[1320.0s] And this step is quite simple as well.
[1321.6s] It's basically I wanted to provide a
[1324.5s] almost like a list of modules or
[1326.7s] sections that could be relevant to this
[1329.6s] topic that we have already covered so
[1331.5s] that when it comes to outlining and
[1332.6s] drafting Claude can go and look up these
[1334.8s] examples, incorporate those headers,
[1337.1s] link back to them as an internal linking
[1339.0s] step. Just make it kind of an integrated
[1341.0s] part of how we create content.
[1344.0s] >> Okay, and then we have next step.
[1346.2s] >> Yeah, and now on to the outlining phase.
[1348.6s] Um so let's have a look see if I can
[1350.9s] find the skill for this one.
[1353.6s] So these are this is very similar to
[1355.0s] what we had in the custom GPTs. This is
[1358.1s] kind of the editorial process that when
[1360.4s] a writer puts together an outline, this
[1362.4s] is how I expect them to do it.
[1364.4s] Um
[1365.4s] so it's got some very simple core
[1367.0s] concepts. Um you know, every uh we must
[1370.2s] use the bluff principle. So every
[1372.1s] section must open with the most
[1373.4s] important idea and then segue to
[1376.5s] examples, extra context, that kind of
[1378.6s] thing.
[1379.4s] >> [snorts]
[1380.2s] >> Um we to make sure we're logically
[1382.5s] supporting the thesis. So, the headers
[1384.2s] must make sense within the context of
[1386.2s] the title you've created. We need to be
[1388.2s] exhaustive in how we cover the topic. We
[1390.0s] need to be mutually exclusive, so we
[1391.6s] don't have loads of overlap between each
[1394.3s] of the sections.
[1395.8s] Um, and again, these are things that if
[1397.8s] you ask Claude to edit an article and
[1399.9s] make it MECE, it does a fairly good job
[1402.0s] of that. It has a good comprehension of
[1403.4s] what that means.
[1405.4s] Um, and then you can see an example
[1408.0s] outline of an outline here.
[1412.3s] So, we've got a hook, key points, uh,
[1414.7s] any ideas for transition it wants to
[1416.3s] include, or a specific example it wants
[1418.2s] to include, it wants to include a table.
[1421.4s] Um, these are the bones of the article.
[1424.9s] >> You mentioned a very, uh, important
[1427.4s] word. The word is example.
[1430.0s] Uh, I can give you,
[1433.1s] uh, a quick reference of, uh, why I'm
[1435.3s] talking about it. So, I have a bunch of,
[1438.2s] uh, skills in my Claude code for
[1441.1s] creating LinkedIn posts.
[1443.4s] Uh, so,
[1444.2s] for example, I have, uh, product-based
[1446.7s] LinkedIn posts when I'm announcing a
[1448.2s] feature. I have, uh, podcast
[1451.2s] announcements when I'm announcing that I
[1453.0s] had a new guest on the podcast,
[1455.3s] uh,
[1455.9s] or just regular posts when I have an
[1458.2s] idea and they want to kind of deliver it
[1460.3s] in the best possible and punchy way.
[1463.2s] The thing is, for, like, each of those
[1466.0s] is a separate skill that I have created,
[1468.1s] that I have instructed,
[1470.0s] uh, Claude code of what I'm looking for.
[1471.9s] When I'm announcing a podcast, that's
[1473.8s] one format. When I'm announcing a
[1475.6s] product update from Ahrefs, that's
[1477.2s] another format. When I want just to
[1479.4s] improve a random post that can be about
[1481.7s] anything, that's a different set of
[1483.2s] instructions.
[1484.5s] But the thing is, for each of those
[1486.5s] skills, I have a folder where I I have
[1489.8s] given Claude code a bunch of examples.
[1493.1s] Here [snorts] are the examples of my
[1494.6s] previous podcast announcements, so that
[1496.8s] not only you have my instructions of how
[1499.2s] to write them, how to structure them,
[1501.2s] you have examples of how I did that in
[1503.1s] my voice already previously. And also,
[1505.2s] like those examples come also with
[1508.0s] engagement metrics. So, it's
[1509.9s] even sees which posts perform better,
[1512.2s] which posts performed worse.
[1514.6s] Uh same for podcast announcements, same
[1516.4s] for product announcements, and same for
[1518.4s] random posts. So, we'd always have a
[1521.3s] folder with examples to reference, and I
[1523.3s] almost feel like
[1525.4s] when it only has instructions
[1529.2s] versus when it has instructions and like
[1532.4s] five to 10 examples
[1534.4s] I feel it does a better job when it has
[1537.6s] kind of the actual examples to fall back
[1539.8s] to. So, when you're saying that this is
[1542.0s] there's a step of an outline, I almost
[1544.7s] want to you to have a folder where you
[1547.4s] have five examples of outlines of
[1549.9s] previous posts.
[1552.2s] >> We do have that somewhere. Is it
[1553.9s] templates? [clears throat]
[1557.2s] Yeah, somewhere we do have that. Maybe
[1558.8s] it's in part of the
[1560.9s] the skill files.
[1562.6s] Cuz they're exactly the same thing. I
[1564.4s] Yeah, we
[1565.3s] Every time we generate something, we
[1567.0s] generally want it to maybe sound like us
[1569.0s] or sound a particular way.
[1571.0s] And I used to see a lot of people feed
[1573.2s] it writing and say, "Can you distill my
[1575.8s] writing down to a handful of principles
[1577.6s] that you can then follow?"
[1579.4s] >> I would I was always very skeptical of
[1581.0s] that though. Like, how can you reduce
[1582.3s] somebody's unique voice down to a
[1584.1s] handful of things that then Claude
[1585.6s] without that example to back it up can
[1587.6s] actually go away and do? I think what
[1589.6s] you're you're right, the much better
[1590.8s] thing to do is let the model infer
[1592.3s] itself from an actual example.
[1595.2s] Uh cuz, you know, your writing style I
[1596.8s] don't think is always going to map
[1599.1s] neatly across to a five bullet point
[1601.2s] lists of
[1602.6s] your writing style or whatever. But,
[1604.9s] Claude is a large language model. It can
[1606.5s] infer from large samples of text the
[1608.3s] patterns that do actually exist in your
[1610.5s] content, and that is how it'll will up
[1612.5s] sounding like you. So, I totally agree.
[1614.2s] Anchoring it with an actual example and
[1615.8s] saying "Make it sound like and feel like
[1617.8s] this" is actually pretty good from um
[1620.2s] what I've seen.
[1620.8s] >> Yeah, and this is this is exactly how
[1623.0s] people should create those skills in the
[1624.8s] first place, because the way I created
[1626.9s] my skills is I gave it a bunch of my
[1629.7s] previous podcast announcements. I said
[1632.7s] "Analyze these posts. Tell me what I'm
[1635.4s] doing here. Tell me what's my style."
[1638.2s] It would tell me like what it kind of
[1640.3s] inferred from uh reading my posts, and I
[1642.8s] would correct it if I disagree
[1644.3s] somewhere. If if it doesn't feel like it
[1646.6s] understands what I'm doing, uh sometimes
[1649.0s] it would understand what I'm doing
[1650.4s] better than myself, which is funny. I'm
[1652.4s] like, "Oh, that's that's really what I'm
[1654.9s] doing. I just I I was doing it
[1656.3s] subconsciously. I didn't understand
[1657.9s] that." And then, for example, uh
[1660.5s] speaking of podcast announcements, I
[1662.2s] would give it some podcast announcements
[1664.1s] from Lenny Rachitsky, how he announces
[1666.3s] his podcast interviews on LinkedIn, and
[1668.2s] I would say, "Okay, analyze what Lenny's
[1670.0s] doing here." Uh it would analyze what
[1672.4s] Lenny's doing. Again, I would correct if
[1674.4s] I disagree with something. And then I
[1676.2s] would say, "Now create kind of something
[1678.7s] in between, something between my
[1680.3s] approach and Lenny's approach, and tell
[1682.4s] me what set of instructions you would
[1683.8s] come up with." So, basically, I'm not
[1685.8s] creating instructions myself. I don't
[1687.8s] need to write out instructions. I'm
[1689.7s] giving it examples. I'm telling I'm
[1691.8s] telling it "Analyze and tell me what you
[1694.2s] see, like what's the kind of principles
[1696.5s] behind this piece of content." And then
[1698.7s] I would correct it if with something. I
[1701.0s] would monitor what what instructions it
[1703.2s] is creating for itself, and I would uh
[1705.4s] correct it. And then, like I said, it's
[1707.2s] very important to have those examples
[1708.9s] for it to fall back on uh because then I
[1712.2s] just I just feel the output is always
[1714.0s] better.
[1715.0s] Okay, so that's outlining step.
[1717.1s] Uh like you said, you you do have some
[1719.3s] outline examples. Actually, it's as easy
[1721.4s] as asking Claude, "Hey, outlining step.
[1724.5s] Uh tell me, do we have examples for it?
[1726.3s] How are they stored? are they stored in
[1728.0s] a text document, are they stored in a
[1729.6s] folder, and it would tell you, and if
[1731.4s] you don't, you can just say, "Okay, then
[1733.2s] create this folder, add these examples,
[1735.9s] and cross-reference it." So, yeah,
[1738.4s] uh a lot of people kind of
[1741.6s] I am not sure if I can use the word
[1742.9s] over-engineer, but they overthink. They
[1745.0s] overthink what is AI, but it's like as
[1747.6s] easy as just talking to it, asking it
[1749.6s] questions like, "How did you do this?
[1751.0s] How did you do that?" And guiding it uh
[1753.7s] well, of course, if you have a good idea
[1755.6s] of what you want to achieve, but it's
[1757.0s] very important to be able to break the
[1759.3s] process into kind of
[1762.0s] uh smaller steps, into building blocks,
[1764.2s] so to say.
[1765.4s] >> Yeah.
[1766.7s] >> Okay, next uh after outline, what's the
[1768.6s] step?
[1769.6s] >> So, now what we do is we look at the
[1771.6s] outline we've created, and we ask Claude
[1773.6s] to find specific opportunities to
[1775.8s] mention relevant Ahrefs products.
[1778.5s] Um I tried, you know, having this at
[1780.8s] integrated into other steps, and it was
[1782.6s] a bit hit and miss, and this is
[1783.7s] obviously something that really matters
[1785.0s] to us, because
[1786.6s] this is why we write content. We want to
[1788.4s] talk about the product in context where
[1790.0s] it makes sense to do that. So, this is a
[1792.0s] discrete stage. This will do this every
[1793.7s] single time.
[1795.0s] Um
[1797.2s] Uh you know, it's very simple, cuz
[1799.4s] within the skill, I actually have a kind
[1801.1s] of master list of Ahrefs products and
[1803.8s] features,
[1804.9s] which I asked Claude to create for me,
[1806.8s] and then I updated and tweaked myself to
[1808.8s] include like newer ones, add some
[1810.5s] features. So, it goes to that, and it
[1812.6s] looks at the outline, it says, "Which of
[1814.3s] these can I contextually mention in this
[1817.5s] outline, and have it make sense, have it
[1819.4s] be useful for the reader?" And it just
[1821.2s] adds a little signpost for the next
[1822.6s] step, uh so that when it comes to
[1824.1s] drafting, it knows to actually
[1825.6s] incorporate Ahrefs into it.
[1828.6s] Like, you know, Keyword Explorer, that
[1829.9s] kind of thing.
[1832.1s] >> And again, probably this is not
[1833.4s] something that people need to write
[1835.8s] start to finish themselves. Just drop
[1838.5s] links to your landing pages, to your
[1840.4s] video overviews, ask it to analyze it
[1843.2s] and tell it tell you what the product
[1845.2s] is, what is it what is it good for, what
[1847.6s] are the top use cases, what are they
[1849.7s] like use cases for I don't know for this
[1852.8s] area, for that area, and then you just
[1855.0s] correct it. So, yeah, it's it's actually
[1857.5s] those things are easier to create than
[1859.9s] than people might think.
[1862.0s] >> Yeah, exactly. I would go site audit,
[1864.4s] rank tracker, content explorer.
[1866.8s] Claude did most of the heavy lifting
[1868.2s] here. I just reviewed it.
[1870.1s] And I added in some I need to add in
[1871.6s] like fire hose and things like that
[1873.1s] actually.
[1876.0s] But again, Claude can do all this for
[1877.4s] you. It's a fantastic diligent worker.
[1880.6s] And then after that is the drafting
[1882.2s] stage. And I think when most people
[1884.1s] would do like a AI content process, this
[1886.3s] is probably the only stage they would
[1887.8s] create. And certainly when I've talked
[1889.4s] to people, this is all they do. They
[1890.7s] focus on what are the best prompts for
[1893.0s] making an article.
[1894.6s] But yeah, from all of our trial and
[1896.4s] error, I think having tons of steps for
[1898.2s] research and structure before you get to
[1900.3s] writing is what ends up giving you the
[1902.0s] best outcome.
[1906.0s] And this is again similar to the writing
[1908.4s] rules we had in our previous GPT. It
[1910.2s] just has some This is adapted from our
[1912.3s] own internal writers like style guide
[1914.6s] for writing.
[1915.8s] You know, use the problem agitate
[1917.2s] solution
[1918.6s] formula. Here's an example of it in
[1920.3s] action as part of the introduction. That
[1922.2s] works pretty well.
[1923.6s] Some structural stuff, that inverted
[1925.8s] pyramid,
[1927.3s] always explain what and why.
[1930.2s] All these very simple things that
[1932.8s] contribute well.
[1934.3s] Mhm.
[1935.1s] >> Draft is not a final step, right?
[1937.8s] >> It is not the final step.
[1938.6s] >> So, what go goes after draft?
[1941.5s] >> So,
[1944.1s] as we have a kind of verify claims
[1945.9s] stage.
[1947.1s] Internal
[1948.6s] linking is very important for us and for
[1950.6s] SEO, and also making sure we have
[1953.9s] included useful up-to-date sources for
[1956.6s] everything that we do. So, there is a
[1957.8s] particular step in here that
[1959.7s] it actually goes through the draft and
[1961.3s] it looks for the claims.
[1963.8s] Things, you know, claims that the
[1965.2s] article is making that we would need to
[1966.7s] go out and validate and it makes sure
[1968.7s] that it has an up-to-date source for
[1971.2s] that or it update it reviews it to see
[1974.1s] if it's accurate or not. Um and actually
[1976.9s] I've been working on this, you know,
[1979.0s] updating this skill because this is a
[1980.6s] big part of our content updating
[1982.4s] workflow. We want to go back to old
[1984.4s] articles, find all the claims, make sure
[1986.1s] they have the most up-to-date validation
[1988.2s] and accurate stats for it.
[1990.2s] Uh so that's the next step of that
[1991.4s] process there.
[1993.5s] >> And there is there is more steps after
[1995.3s] this?
[1996.0s] >> Yeah, not too many more.
[1997.8s] Um so we have
[1999.8s] uh a preview stage. So at this point I
[2001.7s] wanted to be able to look at the draft
[2003.8s] and sanity check it and see if I was
[2005.1s] happy with it.
[2006.3s] And it's not always I don't like looking
[2008.1s] at markdown files like this, so it
[2009.7s] actually generates a HTML file that is
[2012.5s] styled to look like the Ahrefs blog. And
[2015.2s] I can then open that up in my browser
[2016.9s] just to like see what it would look like
[2019.0s] and feel like on the blog, so I can
[2020.6s] quickly review it from that point of
[2022.4s] view.
[2024.0s] And the thing that still takes a ton of
[2026.3s] my time that I am trying to work on is
[2029.0s] uh screenshots.
[2030.6s] So much of our content is product-led,
[2032.3s] it involves using the Ahrefs product.
[2034.4s] Screenshots are so important for that.
[2037.8s] At the moment what this does is it will
[2040.7s] uh suggest a report
[2043.0s] uh that we can actually go and visit and
[2045.1s] take a screenshot of.
[2046.8s] And we actually have another skill that
[2048.6s] other people on the company in the
[2049.7s] company have built which allows the claw
[2052.4s] to structure correct URLs for our
[2054.8s] reports. So it can actually generate a
[2056.9s] genuine report URL for you to visit in
[2059.0s] Ahrefs and then I can take a screenshot
[2061.2s] of that. So that's quite useful. I'm
[2063.6s] trying to automate that with some
[2064.9s] headless browser stuff and some
[2066.6s] screenshotting and that kind of thing.
[2068.8s] Um but at the moment I spend as much
[2070.7s] time doing the screenshots as I do
[2072.4s] actually editing, reviewing, generating.
[2075.0s] So, that's a big part of it.
[2077.4s] >> Okay, since my my job on this podcast
[2081.4s] and in our calls is to essentially
[2083.6s] criticize everything you do.
[2085.5s] >> [laughter]
[2086.9s] >> What what what a fun job. People would
[2088.6s] would think I'm a terrible person, but
[2092.6s] it is what it is. To be honest, one one
[2094.8s] step I I
[2096.7s] expected to see in this process
[2100.2s] is when you would
[2102.8s] kind of dictate to this system some of
[2106.8s] your thoughts of where to take this
[2108.7s] article in free form. And I would
[2111.2s] explain why Ah, you have it or
[2113.3s] something? You you you you're pointing
[2114.7s] something out.
[2115.2s] >> I do indeed. Yeah, I kind of glossed
[2116.6s] over it. Um,
[2118.3s] I totally agree. Sometimes you just want
[2119.8s] to provide a few sentences of thought or
[2121.5s] direction. You want to mention a
[2123.1s] specific product and you don't trust
[2125.2s] that it will do it itself. So, one of
[2127.0s] the things I added recently was this
[2128.3s] context trigger.
[2129.9s] Um, so this right at the get-go, when
[2132.2s] you trigger the workflow, you can
[2133.4s] provide it with as many sentences of
[2135.2s] context as you would like, and that is
[2137.5s] then used to shape and inform the rest
[2139.4s] of the process.
[2140.8s] Um, so often I'll say cover this topic
[2143.0s] or this topic or review this existing
[2145.2s] article and bring elements of that into
[2147.0s] it or mention this new product and that
[2149.1s] kind of thing. And it's just a little
[2151.0s] directional nudge and then again, that
[2152.8s] seems to be very useful for getting a
[2154.4s] good outcome from it.
[2156.4s] >> Uh, I think it's like a critical step in
[2159.9s] my opinion. Again, we are still in the
[2162.7s] very early days of all that. We're still
[2164.6s] experimenting and
[2166.5s] like I have so many thoughts
[2169.3s] in regards to all this. So, first of
[2170.8s] all, I think it's important to point out
[2172.4s] that what you just showed is a work in
[2175.3s] progress because any any kind of skill,
[2178.6s] any kind of workflow that you build for
[2180.8s] yourself in Claude Code or any other AI,
[2183.8s] it shouldn't be set in stone every time
[2186.4s] you run it and every time you analyze
[2189.3s] the output, whether total output or
[2191.7s] whether output of the steps,
[2193.6s] and you don't like something, you need
[2195.4s] to go and refine, and you keep refining
[2197.4s] and refining, and you're basically
[2198.7s] teaching your AI workflow, AI agent, AI
[2202.3s] skills, skill to do a better job, and
[2204.8s] with every run it would get better and
[2206.4s] better. Uh so, this is the first point.
[2208.4s] The second point, I feel this uh this
[2211.0s] step of giving it context
[2213.6s] is super important because it is what
[2217.1s] will essentially make your content
[2220.2s] unique. Because again, uh the reason why
[2223.6s] I was also surprised that you would let
[2225.2s] it run for 8 minutes and just generate
[2227.1s] something for you, is because I would
[2229.0s] expect that uh you would get a TLDR file
[2232.7s] from the top competitors, you would go
[2235.4s] through it, and you would just like in
[2236.9s] free form, uh I'm I'm using Whisper
[2239.0s] Flow, this thing to dictate into into
[2241.6s] anywhere, basically, in text all the
[2243.6s] time, and I would just click a button,
[2245.4s] and I would say, "Oh, like, so I
[2247.2s] disagree with this part. I think this
[2249.3s] part is good. Don't even mention this
[2251.5s] part, it's not important. Here is where
[2253.5s] I think you can" and you can give it a
[2255.6s] lot of instructions. It's almost as when
[2257.6s] we had those content mastermind calls,
[2260.4s] where we would discuss ideas, and we
[2261.9s] would brain brainstorm where to take
[2263.9s] every idea.
[2265.2s] In the same way that we were giving each
[2267.3s] other feedback, and uh kind of figuring
[2270.1s] out what angle is best to take uh with
[2273.7s] uh any given content idea, in the same
[2276.1s] way you can provide uh feedback to or
[2279.8s] context to AI, and I feel it would it it
[2283.8s] typically would do a great job uh at
[2286.0s] doing this.
[2288.1s] >> And that's very another very good point.
[2290.4s] Maybe I'll talk briefly about how I
[2291.8s] think conceptually this process should
[2293.7s] be used for content marketing generally.
[2296.3s] Like, this is not the Ahrefs content
[2298.7s] process going forward. It is not as
[2300.0s] though everything we create has to come
[2301.6s] through this or will come through this.
[2303.8s] Um we spend a lot of time writing stuff
[2306.2s] that is AI still not very good at
[2308.3s] helping with things that require tons of
[2310.8s] thought and experience and unique
[2312.5s] perspectives and ideas that maybe other
[2314.4s] people haven't even shared before.
[2316.7s] I think this is really useful because
[2319.0s] you know, we've written literally
[2320.6s] thousands of articles over the years and
[2323.4s] what I see being really important for us
[2325.5s] going forward is having this
[2326.6s] well-maintained library of evergreen
[2328.8s] search content. I want to make sure we
[2330.8s] cover all the core topics that relate to
[2332.6s] our product and how to use it, keep them
[2334.3s] updated. And a lot of times that is very
[2336.7s] simple, quite repetitive stuff. Like how
[2338.8s] many ways are there to do keyword
[2340.1s] research? Quite a few as it turns out.
[2343.4s] So I think this is really good for
[2345.4s] topics, you know, we have tons of
[2347.1s] information documenting keyword research
[2349.2s] and all these kinds of topics that can
[2350.8s] be used to inform this process. This is
[2353.4s] almost like, you know, doing our
[2354.8s] housekeeping for us in some sense. Um
[2357.5s] it's not something that requires a ton
[2359.2s] of direct involvement and guidance
[2361.0s] because we've already done that. We've
[2362.1s] written dozens of articles on these
[2363.9s] topics that it is using
[2365.6s] used to shape these articles now.
[2368.4s] Um and you know, I've generated tons of
[2370.1s] articles from this that were I could
[2371.8s] have published and would have been fine,
[2373.8s] but I didn't know enough about them. I
[2375.3s] didn't think they were interesting
[2376.5s] enough and I've chosen not to do that
[2378.4s] because I still deeply care about
[2380.5s] everything we publish and I'm I want to
[2382.0s] make sure we put out the best thing we
[2383.4s] can.
[2385.7s] >> So yeah, I feel this process and the
[2387.8s] reason why kind of you let it run on
[2390.4s] itself with little output, it feels that
[2393.2s] it's best used to take some kind of what
[2396.5s] we call a general knowledge topic and
[2399.0s] adapt it to us because one of the steps
[2402.1s] it pulls from our existing content and
[2404.3s] it finds what kind of unique stuff we
[2406.0s] said, then it finds the uh the way to uh
[2409.4s] include Ahrefs and our use cases in this
[2411.5s] post. So basically, for example, there's
[2414.0s] plenty of information about link
[2415.8s] building,
[2417.0s] but it doesn't necessarily share what we
[2420.6s] have shared about link building, and it
[2422.2s] doesn't necessarily makes good use of
[2424.6s] Ahrefs tools when it comes to link
[2426.2s] building. So, with this automated
[2427.8s] process, this is where you don't need to
[2429.4s] write something from scratch. You can
[2430.9s] analyze existing content, and AI can
[2432.9s] find a lot of information from our
[2435.4s] existing articles and from our tools to
[2437.9s] include in the post, and yeah, you have
[2440.2s] the post ready.
[2442.0s] Am I right?
[2443.1s] >> Yeah, exactly that.
[2445.1s] Yeah, I like to think, is this a boring
[2447.0s] topic that I don't want to write
[2449.2s] because we've covered it a thousand
[2450.6s] times? If so, maybe it's a good
[2452.2s] candidate for the AI process,
[2454.7s] which is not everything we publish.
[2458.2s] >> In that regard,
[2460.0s] oh, you have something else to say.
[2462.2s] >> Yeah, so very briefly, I just it kind of
[2463.9s] ties onto this. And also, we built a
[2465.6s] content updating pipeline. This is a bit
[2467.7s] newer, I'm still tinkering with this.
[2469.6s] But in a similar way, we have yeah,
[2471.2s] thousand published articles, for
[2472.7s] example, and it's very hard for human
[2475.7s] people to keep on top of that, keep them
[2477.2s] updated. So, we're working on a similar
[2479.5s] process here that is designed to
[2481.7s] basically periodically give you updated
[2484.5s] content to review and edit and approve
[2486.4s] and potentially publish.
[2488.1s] And very similar thing, there are
[2490.3s] basically three things this does.
[2492.9s] It looks for claims that might be
[2495.0s] outdated. So, there's an old stat or
[2497.6s] something that doesn't make sense,
[2499.1s] Claude will review it and try and find a
[2500.8s] new version of that and allow you to
[2502.4s] accept it if you want to.
[2504.3s] You can find opportunities to add new
[2506.5s] Ahrefs product features. So, obviously
[2509.0s] some of our articles were published like
[2511.0s] eight years ago, they don't mention our
[2512.6s] latest products like fire hose or you
[2514.6s] know, AI content helper. This can make
[2517.1s] recommendations for you.
[2518.8s] And lastly, updating topic gaps. So,
[2521.6s] this is where it looks at the SERP and
[2523.0s] it says, is there anything that has
[2525.0s] other articles talk about that we don't?
[2527.2s] Perhaps we should draft a section for
[2529.2s] you to review and edit and include. And
[2531.4s] it just makes, you know, a very boring,
[2533.6s] um, unstructured process a bit more
[2535.6s] organized and a bit more, um, fun for
[2537.9s] people to engage with, I think.
[2540.2s] >> I I really really like where all of this
[2542.5s] is going because I think this is
[2544.3s] actually the future of how content is
[2546.7s] going to be created. And, uh, I wanted
[2549.4s] to wrap wrap this up from a different
[2552.0s] perspective because you essentially
[2553.6s] shared a workflow of how uh to create
[2556.8s] content on what you call like a boring
[2558.6s] topic, something that been covered over
[2560.8s] and over and we just have like some
[2563.2s] unique spin or we want to cover this
[2565.2s] topic and include our products and
[2567.0s] services. I wanted to to share a quick
[2569.2s] story, uh, from the other side when you
[2571.4s] want to create something completely
[2573.1s] unique. Uh, and that is, uh, so I'm in
[2576.1s] the process of writing a book as I
[2577.7s] mentioned many times on this podcast
[2579.6s] already. And, uh, just 8 months ago I
[2583.2s] was complaining to, uh, a bunch of our
[2585.5s] team members that it is very hard for me
[2588.4s] to context switch because when I stop
[2590.9s] working on the book and I do some like
[2593.1s] projects, uh, inside Ahrefs and then I
[2596.0s] need to return to the book like a few
[2597.7s] weeks later, I barely remember what I
[2600.0s] was writing about, I barely remember my
[2602.0s] train of thought and it's almost like I
[2603.7s] need to upload all the information from
[2605.6s] scratch. And, uh,
[2607.9s] I think it was father who said, uh, "Why
[2609.8s] don't you just upload like all your
[2611.6s] chapters to AI and kind of ask it to
[2613.9s] guide you like AI would ask like a
[2615.9s] journalist or a ghost writer who'd be
[2617.7s] interviewing you asking you questions
[2619.7s] and would be kind of writing the book
[2621.2s] for you." It was 8 months ago, about 8
[2623.8s] months ago. And I said,
[2625.9s] "I cannot see how I would be able to do
[2628.3s] that." So, back in the day we didn't
[2629.7s] have Claude Claude, back in the day like
[2631.6s] ChatGPT just released their custom GPTs
[2634.2s] or something.
[2635.5s] I couldn't see how I would upload like
[2638.5s] my entire book and be able to work with
[2640.5s] it. Fast forward 8 months and the last
[2643.6s] chapter of my book, I just finished the
[2645.5s] the draft. The last chapter I wrote it
[2647.4s] with AI by dictating my ideas into
[2650.5s] Claude code. And my process was I told
[2652.6s] it, "Okay, the name of the chapter is
[2654.9s] this. What is going to happen is you're
[2657.2s] going to create a folder with my random
[2659.8s] dictations because I have a list of
[2661.4s] notes what I want to say within this
[2663.4s] chapter, and those notes exist in the
[2665.8s] form of
[2667.1s] three words or one sentence. Basically,
[2669.5s] talk about this or expand on this idea."
[2672.7s] And I would hit a button and I would
[2674.6s] just ramble. So, there's this idea and
[2677.5s] they wanted to say blah blah blah. And
[2679.6s] we like did this thing at Ahrefs and we
[2682.2s] have this interesting story blah blah
[2683.6s] blah.
[2684.6s] Dictation over. Next idea. And I was
[2687.2s] just
[2688.2s] rambling on each of my ideas. I had a
[2690.5s] few dozen of them. Okay, it saved it to
[2692.8s] the folder. And I said, "Okay, I'm also
[2695.4s] like when talking when talking about
[2696.9s] those ideas, I was referencing a few
[2698.6s] things. Some of the things that I
[2699.9s] discussed with some other marketing
[2701.2s] leaders on the podcast, some of the
[2702.9s] things that we actually covered on
[2704.2s] Ahrefs blog." For example, we have an
[2705.7s] article about taste. And I just said,
[2707.8s] "Oh, like I'm talking about taste in in
[2709.9s] my chapter and you have my voice
[2711.7s] dictation with my ramblings about it,
[2713.7s] but we also wrote a nice post. Please
[2716.1s] include it as sources when talking about
[2718.4s] taste." So, I gave AI I gave it all my
[2721.5s] dictations and I gave it all the
[2723.6s] resources that I remembered like
[2725.2s] different YouTube videos, interviews,
[2727.6s] different articles that I want to
[2729.0s] reference, etc. Even some LinkedIn posts
[2731.5s] that I saw from people who are sharing
[2733.2s] these ideas.
[2734.7s] And then I said, "Okay, now the general
[2737.9s] idea of this chapter
[2740.0s] is this. I'm trying to make a point that
[2742.8s] blah blah blah blah blah.
[2744.9s] Now you know like all my dictations, now
[2747.2s] you know all my resources, all the
[2748.7s] stories I want to tell.
[2750.8s] Tell me how would you connect the dots?
[2753.5s] How would you structure it? So,
[2754.8s] essentially, create me an outline." And
[2758.0s] it would write me, "Oh, so I suggest
[2759.6s] that you lead with this story, then it
[2761.4s] transitions well this, and then this
[2763.3s] argument, and then these things, blah
[2764.8s] blah blah.
[2766.3s] At which point I would say, like I would
[2768.4s] give it some feedback where change it or
[2770.2s] not,
[2771.2s] or I would say, sounds good to me, write
[2774.1s] it. And it would write a chapter for me.
[2776.7s] And then I also like upload it to Claude
[2779.2s] Code. I I downloaded from Google
[2781.1s] Documents all my previous chapters, and
[2782.9s] I said, okay, for each chapter, create
[2785.5s] kind of a synopsis file. What this
[2787.7s] chapter is about, what are the key
[2789.3s] arguments that I'm making, and what is
[2791.2s] the TLDR outline of a chapter, what are
[2793.3s] the main stories and key ideas that I'm
[2795.0s] sharing. So, for each chapter it created
[2797.4s] this file kind of with a recap of the
[2799.1s] chapter, and then I said, now refer to
[2801.6s] all the files of all the chapters, and
[2804.1s] create me a synopsis of the book. I want
[2806.0s] to know like what the book is about, how
[2807.6s] it is structured, and what is illogical.
[2810.6s] And it is so good. It's like it's
[2812.4s] literally like you're you're offloading
[2815.1s] some of your brain work to someone else.
[2817.1s] Like you have an external brain that
[2819.1s] processes information for you. So, this
[2822.4s] is why kind of when when we started
[2825.2s] talking and when you shared that you
[2826.5s] created a system for
[2828.8s] creating blog post fast, and you said
[2831.6s] that your productivity increased, that
[2833.1s] you published like three articles in a
[2835.2s] few days or something like that,
[2837.4s] I am actually expecting that all of the
[2840.1s] content that we're going to create, it
[2842.3s] would go through AI, that we will no
[2845.0s] longer manually write stuff. We will
[2848.0s] just hit a button, we would ramble to AI
[2850.3s] what we want to say, we would point it
[2852.7s] at like whatever resources we want to
[2855.5s] use to make a point, and it would help
[2857.9s] us write even a better article because
[2860.6s] its ability to connect the dots and
[2862.6s] understand what you're saying
[2865.0s] is actually quite crazy. I'm very
[2867.3s] surprised how well it was able to
[2869.3s] distill my ramblings into coherent
[2873.5s] ideas, and connect the dots between
[2875.6s] them, and organize it in a way where I'm
[2877.6s] like woah, this actually looks quite
[2880.4s] good. So, yeah,
[2882.8s] the process that that we just covered in
[2885.6s] in this podcast is mostly for kind of
[2888.4s] semi-automated content. You still want
[2890.6s] to like overlook it and like like you
[2892.5s] said, you have a step to give it context
[2894.2s] of where you want to take it and what's
[2895.8s] the unique angle and stuff like this,
[2898.1s] but it's still like you're you're
[2899.9s] floating the majority of the work. While
[2903.1s] I think going forward creating content
[2906.4s] yeah, AI would act like a journalist, an
[2909.8s] editor, a ghostwriter, and you would act
[2912.5s] as a source of ideas and opinions. And
[2915.3s] people who don't have a good writing
[2917.1s] skill, but have strong opinions would be
[2919.4s] able to publish their content fast. So,
[2921.6s] what are your thoughts on this?
[2923.5s] >> Yeah, I totally agree with that. Um, I
[2926.0s] always find some people think that human
[2928.6s] creativity is too unique and magical and
[2931.2s] special that like AI could never help
[2933.0s] with it and never be a useful aid in
[2934.4s] that process.
[2935.7s] But actually there's a lot of mental
[2937.3s] drudgery we do when we're writing a book
[2939.7s] or an essay or anything like that. I
[2942.1s] think the ideas, the motivations, the
[2943.9s] experiences, the things we care about,
[2946.2s] that is still uniquely you in your book.
[2948.4s] It's still your book and your ideas, but
[2951.2s] all yeah, the sitting down for hours and
[2953.1s] shuffling these ideas about and working
[2954.9s] out what are the common themes, that is
[2957.1s] something that AI is fantastic at doing.
[2959.8s] Um, yeah, if it can make these writing
[2962.5s] and creative processes more fun for us,
[2964.4s] then like well, that shouldn't be scary.
[2966.3s] I think that should be fun. We'll be
[2967.3s] more prolific, we'll share more stuff,
[2969.2s] there'll be more of our unique thoughts
[2970.8s] and ideas out in the world.
[2972.6s] Um,
[2973.6s] so if yeah, for all the kind of like sad
[2975.4s] drudgery and you know, are we automating
[2977.0s] careers and jobs away, actually we could
[2978.9s] create more cool stuff than has ever
[2980.7s] existed before in human history. Totally
[2983.1s] possible now.
[2984.9s] >> [snorts]
[2985.0s] >> I like I like the word drudgery. I think
[2987.3s] what what AI does, it it literally
[2989.4s] eliminates drudgery. Because like I
[2991.5s] said, for me it was a pain to go back
[2995.7s] and to because I would need to read my
[2997.6s] entire chapter again to remember what I
[3000.0s] was saying there. And now I can say,
[3001.8s] "Remind me what was the synopsis of the
[3003.5s] chapter, where we left off, which ideas
[3006.4s] need work?" It would tell me all that
[3008.2s] and I'm like immediately I can continue
[3010.3s] working and I can pick up where we left
[3012.1s] off. So,
[3013.4s] yeah, let's let's not make it longer
[3015.7s] than than we need.
[3017.9s] Thanks a lot for sharing your process.
[3020.5s] Thanks a lot for as always letting me to
[3023.0s] jump in with my thoughts and ideas.
[3025.8s] I generally think we're on the right
[3027.6s] track with with
[3029.2s] these kinds of things and this is the
[3031.2s] future, definitely. This is the future
[3033.2s] of content marketing and content
[3034.6s] creation.
[3035.8s] Thank you, Ryan.
[3037.0s] >> Thanks, Tim.
