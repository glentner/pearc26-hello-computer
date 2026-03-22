# PEARC26 Paper Review: Phase 1

**Meeting Recording** — February 17, 2026, 8:00 PM  
**Duration:** 1h 17m 48s  
**Participants:** Ashish Ashish, Geoffrey R. Lentner

---

**Ashish** `1:59`
Hey.

**Geoffrey** `2:00`
Hey, can you hear me OK?

**Ashish** `2:01`
Yeah.

**Geoffrey** `2:03`
Awesome.

<!-- redacted personal conversation -->

**Geoffrey** `8:16`
So I've got — I don't know if everybody in Purdue IT has access to this. I have mixed feelings about Copilot. So I've got the recording going and the transcription going, and I've got Copilot in here who's supposed to be doing a better job. That's not important. Because what I intend on doing is taking the transcript — I'll even cut the first part of that off so that it doesn't get confused. What I want you and I to do is take a look at the project. I'm going to walk through some of the structure of it for a second again, and then what I'd like you and I to do is just have a review session where you and I just have a conversation about the existing paper. So I'm gonna pull up the PDF and I want you to pull up the PDF and we're gonna literally read it. I want to keep it to our 4:00 PM end time. So we'll just go through it. There's only four pages of content — it's actually only three pages if it were double-spaced.

**Ashish** `9:15`
Sir. Sure. OK.

**Geoffrey** `9:30`
Where we are now. I'll just pull it up and I'll show you. We'll start talking about it. So I'm gonna start sharing my screen and then you can have the PDF on your end too, so you can read it.

**Ashish** `9:34`
OK.

**Geoffrey** `9:46`
Uh, let me see. I'm turning on my Do Not Disturb. OK, cool. Share this other screen. OK.

**Ashish** `10:09`
Yeah, yeah. Yeah.

**Geoffrey** `10:10`
Yeah, OK. So like I said before with the workflows I already have — I already have CI built, so if you look at the workflow I have a release. I was playing with an agent thing, but I'm — this is the part that we're going to ignore and we're just having a conversation right now and I think that's how I want to do it. But the PDF release workflow literally just uses LaTeX to compile the thing and then uploads it as a release asset. So all of these are here, so if you don't already have a copy of it, you can go here to releases and grab this.

**Ashish** `10:45`
Yeah. Mhm. Mm-hmm.

**Geoffrey** `11:03`
So um. Other screen, here it is. So here's the PDF as it stands now.

**Ashish** `11:17`
OK.

**Geoffrey** `11:18`
Um... that's not — I swear to God, Mac OS. Why did they have to make this more difficult? All right, you should still be able to see that.

**Ashish** `11:42`
Yeah.

**Geoffrey** `11:48`
OK, so. Just to recap, all of the interactions are stored in the log, so this is the entire history of like what it is that we worked on and every time we come up with it. So these are kind of like the macro level plans for each kind of activity that we did, and then the micro level stuff is in logs. There's some rules and some notes and if you look at it in outline — every section that is actually in the PDF right now is pulled from the draft. So an integration step means that it took this and pulled it into the `.tex` file.

**Ashish** `12:28`
Mhm. Yeah.

**Geoffrey** `12:44`
So these documents represent our sort of high level thinking, which is informed by other stuff that is either in snippets or in notes we have — like bits that we've worked on — as well as the annotated bibliography of all the 13 references.

**Ashish** `13:03`
Right, right. OK.

**Geoffrey** `13:09`
So if you want — not right now, but later — you can go through these. All 13 references that we're including in the abstract are in this timeline order. So it's foundational AI stuff and then the more recent agentic stuff.

**Ashish** `13:13`
Yeah. All right.

**Geoffrey** `13:29`
And the intersection of that with high performance computing. And so these are either academic papers — some of them are actually blog posts, like the Anthropic thing is a blog post — and then obviously the Genesis Mission is actually an executive order from the White House website. But the detailed stuff is in here, so this is the one on the Genesis Mission. The YAML front matter looks kind of weird when you're looking at it in the pretty mode, but there's some meta stuff in there. We did a really nice job of sort of fully summarizing both what the actual thing was that we were including in our reference, but also specifically how does that influence what the main themes are and what we're trying to write about? OK, so we did a first integration. That was the last thing that I touched like two weeks ago — doing a first pass on the draft in each section, and that's how we got to this paper.

**Ashish** `14:31`
OK. Yeah, yeah.

**Geoffrey** `14:53`
Continue with scroll. Thank you. OK. So — abstract — before we start reading, my sort of rough take on this is: I love the structure. I love the structure that was more informed by me. I kind of told it what I wanted in terms of the overall format and structure. I think the abstract is pretty solid. There's a lot of ground that is covered in the introduction and background — almost too much, honestly. And then everything in here is what our plan is at RCAC for what it is that we're working on. That's mostly in the discussion. And then our references and now we're on Page 5. So part of the problem is we're over the page limit in the single column manuscript mode. Now if we change this to the camera-ready, we're absolutely fine. We have a page to spare. So I'm not quite sure what to do about that. In fact, I'm thinking — I'm on the committee, so like I kind of have a say here.

**Ashish** `16:12`
Not for the overall structure. I mean, it looks fine, yeah, because I'm looking at it on my end as well. Yep, that should not be an issue. Yeah, I think we can go line by line now.

**Geoffrey** `16:30`
OK, so let's start with the abstract.

**Ashish** `16:33`
Mm-hmm.

**Geoffrey** `16:34`
*"Large language models have evolved from curiosity to copilot in under four years."* I love that opening sentence. I love the cadence of that. That's solid. *"With the emergence of agentic AI systems that reason, plan and execute multistep tasks autonomously"* — obviously there's the telltale em-dash — *"HPC centers face a new category of user need. Researchers want these tools integrated into their workflows, not merely tolerated."* This is a good but a really long sentence. What's good about it? It does a good job sort of framing agentic as a new thing. It explains in layman's terms what agentic means and it immediately is calling out what HPC centers gonna do. So I think this is great.

**Ashish** `17:36`
Right, right. Mm-hmm.

**Geoffrey** `17:38`
*"This paper offers a practitioner's perspective from Purdue's Rosen Center for Advanced Computing, where we have begun deploying system-wide configurations, custom MCP servers and user guidance for agentic tools."* This was mostly from me — like the three pillars here. So the word choice is something we can do, but those three pillars are things that I defined from the outset and they're largely accurate. I just think this wording is a little awkward.

**Ashish** `18:03`
Yeah. Right. Yeah. So let me see. My God, my laptop. Yeah. OK.

**Geoffrey** `18:45`
Do you have the PDF up on your end?

**Ashish** `18:46`
Yes, no, I do have the PDF. It's my laptop has decided to hang on me.

**Geoffrey** `18:52`
Oh, I'm sorry. OK, so if you want — are you able to see it OK on my screen or is it too small?

**Ashish** `18:53`
Yeah, yeah, yeah, yeah. No, no, it's fine. So yes, I'm fine. If you can scroll up a little bit.

**Geoffrey** `19:10`
Oh yeah, here we go. So we are right here.

**Ashish** `19:11`
So I pretty much like everything about the abstract, to be honest. *"Purdue's center where we deployed..."* — OK, I like this. You know about Purdue. My only thing would be... so my only thing is, I know what you tried to do. My only thing is the last line — *"the equal parts love letter and cautionary tale."* I understand it. And I liked it. But that depends upon who's reading it. If they get it and they don't find it cheesy, this is perfect. But yeah, right, right, right.

**Geoffrey** `20:20`
Part of what it's doing in the abstract — some version of this at the end — is like, we're engaged in some kind of a journey, and as an HPC center we are trying to figure this out and we are both eager and cautious at the same time. So again, with the em-dashes, you know, but I like the idea of — this is kind of a strong statement at the end: *"the path forward for facilitators who wish to remain relevant in the agentic era."* I love that we're ending on this. It's the title. We started with HPC right here and then "agentic era" is the last sentence just like in the title. So this calls out a larger theme in the proposal that stems from this. The whole concept of "Hello Computer" is a tongue-in-cheek reference to begin with, and it's supposed to be fun vibes. I often say pun not intended — I absolutely intend this. This whole thing is dripping with puns.

**Ashish** `21:32`
Yes, exactly. Yes.

**Geoffrey** `21:32`
And the longer I work on it, the more that I hate myself. But I don't want to lose it. I imagine we'll get some negative review. We're gonna get some reviewer who is like, "what the hell is this?"

**Ashish** `21:45`
They're gonna hate it, yeah.

**Geoffrey** `21:51`
You know they're gonna hate it. And you know what? Let them hate it. And it's important — I want to keep it. Not the love letter part, but the puns.

**Ashish** `21:56`
Mhm. No, I agree with everything else. Yes, like I agree. I agree with everything else. My only thing is — like you mentioned — I get these puns because that's the whole point. We are doing this, right? My only thing is, it depends on your second reviewer who's gonna ruin everything. Like — hey, this is not ACM standard, you're trying to go in an informal way — and at the same time, like we are in this really grey area. So my question to you is: is it worth getting it rejected for the pun? Now that's the biggest question. Like, are you OK if it gets rejected across the board? But you'll like, "hey, what? Like we tried and I just wanted to keep it."

**Geoffrey** `22:41`
Yeah, I want to keep it because this is kind of the whole point. And honestly, it depends on who you are. I'm going to say if we have a serious reviewer — which is an odd thing to say because I'm being unserious here — but what I actually mean is a reviewer who is actually close to this, who is somebody like us. This is part of the shtick, right? The whole point with this paper is calling out, and yes it's ironic, but part of the irony is: look what we're able to do. This is both technically excellent and whimsical at the same time.

**Ashish** `23:42`
Yes.

**Geoffrey** `23:43`
And that speaks to what it feels like in the current era using agentic tools to do research workflows. There is some uncanniness to how good it is. These puns represent something close to the uncanny valley — where it is too good. And then you know every other reference in here: "Model Context Protocol, not Master Control Program" — that's from Tron. And then "I'm sorry, Dave" as a tongue-in-cheek reference to user support where you can't do something. There's a user experience there. It's self-aware. What I love about — and what I find to be ironically somewhat serious — is these puns worked into the manuscript are a kind of self-awareness that I think is actually relevant to the topic.

**Ashish** `25:07`
Right. Yeah.

**Geoffrey** `25:10`
So if we have a serious reviewer, I think they will appreciate it and move on. This is partly why I want it to be a poster. If they reject that — I am putting a lot of work in here and by the time I'm done with it, this will be — I have read every single abstract for the last two years for posters as the proceedings chair. More than any other human on the planet, I have had privileged access to everything that went to PEARC, and this is better than anything the last two years from the poster session. And if we get rejected, that's actually a signal — that means something. They could reject it because of this silliness, or they could reject it because of this acknowledgment here, right? This is on point — this is right out of ACM's guidelines for use of generative AI. This entire manuscript was developed with — well, now we're using 4.6, so I'm going to have to amend that. But this is part of the conversation. It's self-aware, and the fact that this is the work — that's what makes this whole activity meaningful. And if they reject it: one, it's a poster, right? And if they reject it, that is not due to excellence. That speaks to something else and I'm willing to fall on that sword.

**Ashish** `26:59`
Sure. OK.

**Geoffrey** `27:02`
Yeah. So I think these are good additions. I think this is coming out a little strong. I don't know what else to put here, but I'll think about something. We'll rework this bit right here. And also I am conflicted about the em-dashes — because there's no point trying to hide it. The em-dashes are correct. It's a technically correct use of an em-dash and one that I would proudly do in my own writing. The fact that agents have a tendency to use them a lot — I don't know. We're not hiding anything here. Agents wrote every single word of this. That's the point.

**Ashish** `27:39`
I mean, our paper is literally gonna say that down the line — if you look, we are saying that. So you know.

<!-- redacted comments -->

**Geoffrey** `28:35`
It has to be based on the merit, not on "oh, I don't like AI and I'm biased towards anybody who does, so I'm going to give you a one."

**Ashish** `28:38`
Yeah, yeah, yeah.

**Geoffrey** `28:46`
But I'm kind of eagerly awaiting getting that one just to engage with that cause — that's actually part of it.

**Ashish** `28:54`
Yeah. No, yeah, yeah, that's fair.

---

## Introduction Review

**Geoffrey** `28:58`
OK, so moving right along. We've got about half an hour left. *"Shall we play a game?"* This is our introduction: *"On November 30th, 2022, Open AI released ChatGPT as a research preview."* I like the use of dates because it marks the timeline. I remember Sam Altman posted a tweet and everybody inside of Open AI honestly didn't even think it was going to be a big deal. And *"within five days it had a million users. By January 2023, 100 million — the fastest growing consumer application in history."* I think that's a really powerful opening line that speaks to this whole thing.

**Ashish** `29:40`
Yes. Yes. The only thing I would say is — and this depends on the lens — I would say instead of saying *"the game changed overnight,"* I would say maybe something like "this marked a turning point." ChatGPT just beat everyone at this game. I think the biggest turning point was not ChatGPT releasing, but the public access — how an average Joe was able to access it. Like because I remember the date, that was December 1st, I actually used it for the first time and I was blown away. I had friends who actually were on the DeepMind team. So you only hear about it, you never actually saw it happening in person. So that was the thing — like, hey, finally it's accessible to us as well.

**Geoffrey** `31:03`
Mhm. So I agree. I think this kind of is using the wrong specific language here. I think it misses the actual important part of it. It's not merely — this comes on too strong in the wrong direction. It is the public awareness that I agree is what matters for this kind of line in the sand. OK, so *"for those of us supporting researchers on high performance computing systems, the implications arrived slowly and then all at once."* I like that it came up with that phrase — I use this phrase all the time and I think it's accurate for AI. It's like it didn't matter, and then it did.

**Ashish** `31:49`
Yeah, yeah, yeah, yeah, yeah.

**Geoffrey** `32:01`
*"At first, ChatGPT was a curiosity — a toy that could write passable Python functions or explain error messages with varying degrees of accuracy."* On point. *"Then came GPT-4, Claude and their competitors — each iteration more capable than the last. Then came Agentic AI systems that don't just respond to prompts, but reason, plan and execute multi-step workflows autonomously."* So that's not a bad, at a very high level — that's kind of the timeline. It's like every year since 2022 has marked an epoch. It was first 2022, then by 2023 capabilities were better. By 2024, more people recognized what was going on. Then we get GPT-4 and Claude, and by 2025 agentic is everywhere and the systems and tools around them have risen to the level where they're driving the models better. I don't have any big complaints, but it's really choppy. The structure is kind of like there's a lot of places to trip over this if you're reading it left to right. This could be written to be more fluid.

**Ashish** `33:17`
Yes. So I have two comments on this. I read the entire paragraph as well — the later part, the agentic development wrap, cursor, Claude code, you know — OK so we can just talk about the entire paragraph. The only two comments I have are just like you said: it's OK, but it doesn't feel flawless. The two things that I think we are missing, the bigger picture — we started from debugging, figure out the error, do this, do that — and we just jumped directly to GPT-4, Claude. I think the one thing that we are missing, even though it might seem irrelevant, is the change from simple models to multimodal models. Because there was a solid year where image generation or video generation was *the* thing, before Agentic AI. I remembered the initial versions of ChatGPT 2 or 2.5 — they didn't even support the extraction of data from images; that came out one year down the line. So those two things are missing. If we fit those in here, it will become flawless. Otherwise it's feeling like it's missing two to three different milestones.

**Geoffrey** `35:03`
Yeah. That is an important milestone that is missing. It's an important step along the way to get to agentic, because my experience now in 2026 is that I can literally draw a picture of what I want the front-end UI to look like and give that to the agent, and it can replicate my cartoon in React or whatever. And that capability comes from two years earlier, when the models became multimodal. And now they're tool-aware and can use things like Figma or Excalidraw or others where I can draw my cartoon and it can consume that — and not just images but audio and whatnot.

**Ashish** `36:05`
Oh, and speech-to-text and text-to-speech.

**Geoffrey** `36:10`
Right. Yeah, yeah. So those are sort of auxiliary developments at the periphery of this — because usually I'm not going to use Claude to do my speech-to-text, but in the environment where I'm using Claude, there is a special-purpose model that I am using where I have spoken instructions that are fed to Claude. That's important. OK, also meta-point as we're going through here — one thing I care about that it's not doing a good job of right now is I don't semantically agree with the use of paragraphs here. And actually I cheated — I kind of broke the vow of not touching it. I deleted some white space because it had paragraphs everywhere. So that's something for us to work on in the final version: can we get it to do a good job with overall structure — like this is a thought, this is a thought, this is a thought?

**Ashish** `37:11`
OK. Yeah.

**Geoffrey** `37:29`
OK. *"HPC centers now face a question with no precedent in our field: how do we engage with tools that can, in some cases, do our jobs faster than we can? This paper offers one answer from the trenches."* So — my first reaction to this is I like that we're tying it into HPC, and I do like the meta point that it's not just us — some of this is doing the researchers' jobs too, for some definition of "job." I don't hate that part. I don't like "this paper offers one answer." I mean, it kind of is an answer because we're saying: if you can't beat them, join them — engage, build stuff around it, deal with it instead of pretending it doesn't exist. So that's kind of an answer, but it's not really an answer. I think "from the trenches" is a visual that's unnecessary.

**Ashish** `38:36`
Mm-hmm. Yes. I think it can be rephrased better. I know what it's trying to do, but after a certain point, these puns or these clever rephrasings start to get you — you're like, "OK, I get it. I know you're trying to be smart, but at a certain point, OK, let's stop." That's the only thing I would say here.

**Geoffrey** `39:03`
Yeah. So another meta-point — and my one rule above everything else. There's this kind of rule about rules when it comes to writing. It's true in technical writing and it's true in creative writing. You go your whole life learning all of these rules about what you're allowed to do with grammar and syntax and punctuation and spelling and 100 other things that have to do with narrative prose. And the one rule to rule them all — borrowing a pun again — is that you can actually break the rules. The truly great writers are always breaking the rules and it's like, why do they get to break the rules? Because the only real rule is that nobody cares until they notice. The moment I notice what you're doing, the spell is broken.

**Ashish** `40:08`
Yeah. Yeah. OK.

**Geoffrey** `40:24`
And so you're kind of right. This is really laying it on thick. I want to keep, you know — the next thing is "mostly harmless," right? There's a joke from *Hitchhiker's Guide to the Galaxy*. I want to keep as much of this as we can. But overly flowery, clever language and overuse of similes — you know, "from the trenches" — that's a visual comparison that we're just over the top with throughout here. That's just because I think the agent is doing a good job, but it's taking it too far. It's like: "oh, you want to be clever, you want puns? I'll show you puns every single time."

**Ashish** `41:04`
Yes. Yeah. Mhm. Yes. So, you know, Jeffrey, what this reminds me of — when I was preparing for grad school for the master's/PhD, you have to take the GRE. Obviously English is not my first language, so there are a lot of words you don't know. I still remember learning the word "juxtapose" and I was telling my wife, "what is wrong with anyone? Why would anyone say juxtapose? Like just say normal English." That's the same thing that sometimes I know you sound clever or people like to see cleverness. However, whether it's in our paper or in normal life — yes, we know you have a good vocabulary — but sometimes being normal is the best thing. You do not have to make everything flowery or you know, stand out. So to be honest, that's what I feel about "from the trenches" — I understand what the meaning is, but this is pushing it too much.

**Geoffrey** `42:16`
Yeah. There is an important point there. And maybe this is worth capturing: the use of generative AI for scientists to express their scientific research to the community. You know, it started — I don't know if you remember back in the day, in the 90s when Microsoft Word first got their thesaurus and you could just right-click on any word and find the big fancy version of that word, and now suddenly you could go through your entire document and start right-clicking on all your words and inserting more sophisticated versions. It speaks to an overall rift in the scientific community as well. You go read a domain paper and the whole thing is just... I'm going to call it thick. It's like wading through it — I need a machete to cut through the jungle of overly obnoxious language that is unnecessary. And especially in physics — I say this as a physicist — other physicists have a complex where they have to be smart, so their papers are excruciating to read. And then you get somebody from one of the Ivy Leagues and you read their paper and it's like, oh my God, a high school student could understand this. This is wonderful. And I think that speaks to some of the mental compensation. A lot of scientists are trying to compensate for their own self-perceived lack of scientific rigor and it comes across in their writing. And the use of generative AI could be good, could be bad — it amplifies everything. That's what's happening here. The agents are amplifying the whole vibe. Like I'm having a great time with this and the agent is amplifying that pattern. It turned it up to 11.

**Ashish** `44:51`
Yeah, yeah. Yeah.

**Geoffrey** `45:10`
Quite literally. So that's worth paying attention to — making sure it stays on target in a way that isn't too distracting.

**Ashish** `45:15`
Yeah. Mhm. Yeah.

**Geoffrey** `45:26`
OK, great stuff. So *"mostly harmless"* — another joke. *"The Hitchhiker's Guide to the Galaxy famously summarized Earth in two words: mostly harmless. We adopted this as our working hypothesis for agentic AI in HPC workflows at Purdue's Rosen Center."* We don't need to say Rosen Center every single time. *"But we chose proactive engagement over prohibition."* Again, overly kind of cumbersome structure — I'm tripping over all the punctuation. *"Users will bring these tools regardless of policy. A graduate student debugging a CUDA kernel at 2:00 AM will reach for ChatGPT whether or not we endorse it."* So — I'm going to stop right here. I don't necessarily like what this is spelling out. It's saying: mostly harmless — and then: people are going to do it regardless of whether or not we want them to, so we should engage. That actually doesn't line up. There's a misalignment between this notion of "mostly harmless." Because "mostly harmless" means mostly harmless. It doesn't mean "well, they're gonna get..." — you know, it's often said about C++ as if it were a loaded gun. AI is a loaded gun. It is a very powerful tool that can do wonderful things or terrible things, and "mostly harmless" suggests it's harmless — not that they're going to use this loaded gun whether we ask them to or not. So we should put safety mechanisms in place — that doesn't actually align with this statement. What I actually mean by "mostly harmless" is we don't need to doom-and-gloom this. I honestly feel that in 2026, the models are capable enough that, to be quite frank, I trust Sonnet and especially Opus better than I trust graduate students. Graduate students are more harmful than the AI model.

**Ashish** `48:18`
Like, I'm not sure if you remember — remember that one graduate student that pushed you to the limit, that you had to create that strong-worded email because he was pushing you too much — "give me root access" — and you were like, "I'm gonna be polite, but like you are a nut case and we're not gonna give you root access because you're gonna blow up everything."

**Geoffrey** `48:40`
Yeah, I did not hold back in fully articulating the manner and form with which he would cause mayhem and destruction. Yeah, I remember that quite well.

**Ashish** `48:46`
Yeah. Yeah. Yeah.

**Geoffrey** `49:00`
OK, so I love this — I didn't even program this, this right here is magic. *"A graduate student debugging a CUDA kernel at 2:00 AM will reach for ChatGPT."* Yes, of course they will. 100%. So I don't hate what's in here, but I think there's a misalignment and we should work on that. OK, rest of it — *"whether we help them use it effectively or leave them to discover hallucinations the hard way. This paper documents our early experience: system-wide configurations that expose cluster metadata to agentic tools."* Yep, so like that's where I've written into the instructions for the MCP servers and whatnot — for Gemini to pick up — I have this `etc/agents.d` folder that I'm going to push that has information like: here's how to figure out what storage spaces you have access to; Data Depot actually means this; Scratch is actually a Lustre filesystem — structural things that are specific to us.

**Ashish** `49:53`
Yeah.

**Geoffrey** `50:27`
There is something in here about dog-fooding that we need to include. Are you familiar with that word? Do you know what I mean when I say dog-fooding?

**Ashish** `50:35`
Yeah. No, I was gonna ask.

**Geoffrey** `50:41`
Yeah, so real quick — software companies like to use this term "dog-fooding." Historically, companies that make dog food save money because nobody cares, because a dog cannot tell you "this food is disgusting, I'm starving." It's like the quintessential meme of terrible nutritionally. So if I'm an employee at a company that makes dog food and I feed my own dog — who is my best friend — the food that we make at my company, it means I trust it. In this context it means we use the tools that we tell users to use, so that we have a visceral understanding of it. If you're a software company and you make a ticketing system, you use that ticketing system so you're a canary in the coal mine. Slack uses Slack — every software company that sells a product should use their own product so that they are aware of how good or bad it is. And so part of this speaks to the notion that we ourselves should engage deeply in agentic tools because our users will, and if we want to facilitate and guide scientists who use the HPC system with AI, we should understand every angle of that.

**Ashish** `52:47`
Yeah. OK.

**Geoffrey** `52:51`
But it needs to be shaped up and there's an alignment problem. It mostly doesn't match this.

**Ashish** `52:53`
Yeah. Yeah. Yeah, yeah.

---

## Background Review

**Geoffrey** `53:04`
OK, background. *"The trajectory from research curiosity to practical tool was swift."* I mostly agree with that. I would say technology generally expands over the course of decades. People who grew up in the 90s are used to technology changing quickly. But I think most people agree there have been seismic shifts in capability every single year, and now on timescales of six months, it's like...

**Ashish** `53:27`
Yeah. Right.

**Geoffrey** `53:42`
We have categorically — like I don't know. Like this morning I was watching something — is it "Sea Dance"? I think it's playing on Sundance. Sea Dance 3 — I watched a 20-minute like action thing this morning that actually had actors I recognized, and then the president was at the end. And I was like, wow, this is freaky.

**Ashish** `54:08`
Yes. Yeah, yeah. Yeah, and they have been sued just today in the morning by Disney. So I mean — look at how much time. Look at Claude Bot — a guy whiteboarded something starting in November. That was his 44th after his 43 failed projects. The 44th one took and I acquired it yesterday. So like, come on. You went from — yes, things are — at this point you're being generous even by 6 months. We're talking about month-to-month changes now. Like the YouTube short that you sent me — "by this time, that has been the industry standard for the last 20 minutes." I mean, like, we had Opus 4.6 and then we had Sonnet today and who knows what they're gonna release tomorrow.

**Geoffrey** `55:17`
Yeah. "Opus 4.6? What are you talking about? GPT-53 Codex has been industry standard for 20 minutes." Yeah, yeah. So I think this is more than fair to say "swift."

**Ashish** `55:36`
Yeah, exactly, exactly. Yeah.

**Geoffrey** `55:36`
*"2017 — the 'Attention Is All You Need' paper introduced the transformer architecture, replacing recurrence with attention mechanisms. By 2020, GPT-3's 175 billion parameters demonstrated that scale alone could yield emergent capabilities. ChatGPT's November 2022 launch brought these capabilities to the general public — 100 million users in two months."* So this kind of echoes something earlier in the paper. I actually find value in the right kind of repetition. I don't hate that it repeated itself here.

**Ashish** `56:20`
Yeah, so I agree with this. But you know, what would be a better statement is that yes, when ChatGPT came out initially in 2022, the talking point was that it took Facebook 13 years or Twitter some number of years, and they're like "we got to 100 million users in two months." Now, since time has passed, there are so many other AI products — agent AI products or otherwise — that have achieved this number within a month or even less. Like Lovable is one of them. So I think instead of repeating, we can build on top of that — hey, using this AI stuff as a foundation, building upon technologies that have been improving day by day, tools have surprised everyone by achieving growth which once was unimaginable. In 20 days or 30 days you can have 100 million people.

**Geoffrey** `57:35`
So I don't know that we have room for a really important conversation about software at large in the agentic era. You were referring to what's now "Open Claw" a moment ago — and yeah, that guy getting bought out by Open AI. He is very upfront that the whole thing is vibe-coded and I follow him on X now. He is constantly like, "oh yeah, I had to fix that bug and redeploy the website" and he's talking to it from his phone. So OpenClaw is kind of writing itself now. And your point about now there are some products that are not vibe-coded but are built on top — they're like a layer on top of this foundation — and there is an important larger discussion worth spending more than one sentence on. It has to do with software generally. Software is not dead.

**Ashish** `58:39`
Exactly. Yeah.

**Geoffrey** `58:56`
Software is going to experience an explosion and a renaissance. And I honestly think at the end of the day it's going to be awkward, it's going to be messy, it's going to be fuzzy, it's going to be frustrating. It's going to be a lot of things over the next two years. But I think there's going to be an explosion of amazing, lovable software. Like Scott Hanselman — he's like the czar of open source at Microsoft — last week he created this whole thing called Tiny Tool Town. It's like an online website of all the vibe-coded stuff that people make and you can just put your GitHub up there. Scott Hanselman himself vibe-coded this whole thing called Tiny Tool Town and it's adorable. And just this morning I saw a screensaver where a guy made — it's like a merger of the green text from the Matrix movie and Tetris. Like the Matrix and Tetris made a baby and it's a screensaver. The guy totally vibe-coded that and it doesn't have to be anything. So that speaks to part of this which is: platforms built on top of these seismic shifts in AI capability can experience rapid adoption. If you can get 100 million users in a month, it's because it's good. Software has never been this good.

**Ashish** `1:00:43`
Yeah. Mhm. Yeah. Yeah.

**Geoffrey** `1:01:01`
You know it used to be a thing 10 years ago, the early 2000s — "I'm gonna be the Uber of this." Like your software startup is gonna be "oh, we're gonna be the Uber for pizza delivery." And that was a recognition of what was possible with the tech, with the magic of smartphones being in everybody's pocket, Google Maps being accurate and up to date, plus some good software — and you could unlock something that is like a phase change in greatness. This is kind of the same thing. Right on top of GPT or Gemini, you can do something that the entire world will want to use tomorrow morning.

**Ashish** `1:01:43`
But — no, I have a little bit of a different opinion on this. I agree that yes, it has sped up the process by 10X, 100X. The ideas are coming to life pretty quickly. But also — any idea, whether it was Google's page ranking when they started in the late 90s, or Uber, or Google Maps — that was just not an idea. There was a lot of work going behind it. What I'm feeling now is that the ideas coming up because everyone wants to beat everyone — there's no time advantage anymore because anyone can catch up, because you have thousands of agents deployed. My thinking is the ideas are going to be more shallow now. They're not going to be well-thought-out. It's going to be like: just churn out stuff and see what sticks to the wall. And — no shade — but if you look at that guy's GitHub, that was like his 45th or 46th project. He was vibe-coding and throwing out stuff to see what sticks. I'm not saying things are not going to stick, but it's also enabling people to just start churning out without actually deeply thinking: can I take it to the next level or not? And you know, what happened with me — the moment Google came up with an upgrade, it killed 50% of my features and I'm like, I'm giving up on it. Because if a Google update can kill half of your idea, technically it was not an idea. So people whose ideas are still brilliant will still work. But unless you're part of a big corporation, you're behind the 8-ball now.

**Geoffrey** `1:04:01`
Mm-hmm. So I'm not sure what 2027 will bring. I see advertisements all the time — YouTube is just smacking me in the face with an ad for this company called Base44. Are you tired of those yet?

**Ashish** `1:04:37`
Oh my God, I like that. Do you know the story about that? About the owner?

**Geoffrey** `1:04:44`
Well, real quick — and we're actually running low on time so we're going to have to split this in half — in the commercial, the idea is: anything you can think of you can deploy. And even as bullish as I am on this agentic stuff — and I use it myself and I am doing all kinds of things and so is everybody else — as it stands now, agentic AI for the masses is not there because it still requires technical rigor to understand what to build. When I build a platform, I know what OAuth authentication is. I know what CSS is. I know what a view controller is. I know what Rust and WebAssembly are. So you can kind of — there's a way of working that makes amazing things possible very quickly. And so you're right about companies. If you have an amazing idea and you can get to market quickly now, so can Google, so can Microsoft, so can Meta, so can IBM. If somebody comes up with a great idea, Microsoft and IBM are going to be right on your heels tomorrow morning.

**Ashish** `1:06:25`
Um, yes, I know.

**Geoffrey** `1:06:25`
And I'm not quite sure what to do about that.

**Ashish** `1:06:30`
No, that's exactly my point. And I'm glad finally someone said this, right? That just because you have Agentic AIs — don't even get me started on X.com and the garbage you see about Agentic AI: "Oh, I gave it like $50 and I made $1,000,000." Yeah, buy my course. Like all those courses. So that's what I'm talking about — because the guy who created Base44 has no technical knowledge. He vibe-coded everything and he sold it for $80 million and he's out. It's a single-person platform. And that's exactly what you said. Because I used it for my idea and I ended up spending more money fixing the stuff it produced than if I had just coded it myself from scratch. So yes, on paper it looks good, but eventually unless you know what you're doing — I went through a Google Ads process using Cursor. I have not done it before myself. I sat down, learned it myself, fixed it faster than Cursor or any of those things. Because like you mentioned, you need some kind of technical background. I know coding in general, so if I put my mind into it, I'm not going to become an expert, but I can figure things out. And this is where it will separate you. Your idea, yes, you might be able to work it, but you still need those foundational technical things. Otherwise, you know, good luck. And I'm just going to summarize it with one line: you know what's going to be the biggest career moving forward? Vibe-coding fixing.

**Geoffrey** `1:08:41`
Yeah. I mean, so yes. And you know there's that meme on social media of some director-level person who's like, "hey, you know, I vibe-coded this over the weekend, go put it in production," and the guy who's the actual senior software developer is like, "my God." What will actually happen — what I hope happens — is vibe-coding kind of... and by the end of this year and into 2027, I'm not quite sure how high we'll climb in what somebody's able to one-shot. But I think it's pretty high, and what you might see — if we can get the environments right, if the tooling can change around this for the masses — is: I can prototype something and be like, "yes, I love what this is. I vibe-coded it, but take this." And that's what we used to do for storyboards — you whiteboard it, right? So I'm actually more optimistic. And you're right, people will still have to pay for experts to take their idea and do it "for real."

**Ashish** `1:09:45`
No, exactly. Yeah. Yeah.

**Geoffrey** `1:10:01`
And I'm a bit less negative about that. I think things will be better in the end. I'm optimistic. All right, so...

**Ashish** `1:10:10`
I think we are just going through this phase of exploration and it's gonna settle — it's gonna reach an inflection point, just like the Internet. The Internet came out around '96. I think we're about to hit that inflection point because at a certain point — how high is it gonna go? Like, OK, what next? What are you gonna do? In one second you're gonna produce an app with a database connected? I mean, there are AI apps and everything that do it for you. But everything will break down eventually unless...

**Geoffrey** `1:10:51`
Yeah. So we got halfway through. I want to touch on this section first and then we'll call it halfway. Section 3 is more to do with what we're doing at RCAC, and then there's some discussion which is kind of the same deal, and then the conclusion. So maybe we grab another hour and do this later.

**Ashish** `1:10:57`
Yeah. Sure.

**Geoffrey** `1:11:07`
I think we're right here. So *"a parallel development transformed chatbots into agents. The ReAct framework formalized the shift: agentic systems interleave reasoning traces with task-specific actions, interfacing with external tools and knowledge sources rather than relying solely on training data."* That's the shift — anything the model can do has to exist within its own neural network, and this creates a problem where if the model was trained in 2023, it only knows things from 2023 and before. *"Today's agentic development environments implement this pattern — reading files, executing commands, editing code, and iterating based on observed results."* So yeah, *"the infrastructure for Agentic AI has matured rapidly."*

**Ashish** `1:12:16`
OK.

**Geoffrey** `1:12:16`
That's an understatement. *"Anthropic's Model Context Protocol"* — this one is really important to me. And what a lot of people disagree on, and I think more importantly — not only the fact that everybody has adopted Model Context Protocol — so 2024 standardized interface for AI systems to connect with external data sources, tools, analogous to how the Language Server Protocol unified IDE tooling. I remember this from a few years ago, that was a big deal. Like one LSP could service any IDE front-end. The important part is: in 2025, OpenAI and Google joined forces and said, yep, MCP is it. And then just 12 weeks ago this was donated to the Linux Foundation. And not only that, but we've got this new — it's kind of like the High Performance Software Foundation — it's like a child entity underneath Linux. The Agentic AI Foundation is now a thing under Linux, so Anthropic donated it to that. *"With over 10,000 active public servers."* I don't know how important this last thing is because honestly this is a drop in the bucket — I can stand up a new MCP server in one hour if there's something I want to do. So I don't know that that number even matters.

**Ashish** `1:13:35`
Yeah. Mhm. Yeah.

**Geoffrey** `1:13:44`
But I think this one is really straightforward — there's no weirdness here. It is very technically direct and to the point. And it's very important that we add this final crescendo: MCP is now under the Linux Foundation, because that is what enables HPC. Something being part of the Linux Foundation is what signals academia and the Department of Energy to be like: "OK, this is stable enough for us to build on now." *"For HPC, this convergence is consequential. Dealman et al. argue that high performance computing stands at a crossroads."* That's literally from their paper. And finally the Genesis Mission executive order — that was in November while we were literally sitting at Supercomputing when it popped up on my phone. I was sitting in our booth reading. *"This charges the Department of Energy with uniting national laboratories, supercomputers and AI capabilities for scientific discovery."* This is an active topic of conversation every single day in our organization.

**Ashish** `1:14:40`
Yeah. Yeah.

**Geoffrey** `1:14:54`
*"The question is no longer whether AI will integrate with HPC workflows, but how — and who will shape that integration?"* I think this is a really powerful sentence. I like this. Because the fact that MCP is part of the Linux Foundation, and it's literally the most important — this is a self-proclaimed successor to the Manhattan Project — to say that it is in the national interest that we build agentic research workflows. It's literally written down on paper and the Department of Energy is moving full steam ahead. So whatever the DOE does, HPC will follow. This is no longer a toy.

**Ashish** `1:15:33`
Yeah. Yeah.

**Geoffrey** `1:15:43`
This is a first-class citizen and the number one priority of the Department of Energy. So — get on board, man.

**Ashish** `1:15:44`
Yeah. Mhm. Yeah.

**Geoffrey** `1:15:54`
Yeah. So I don't have any problem with this last sentence. I think largely this stuff is pretty straightforward. This is very dense — the signal-to-noise ratio here is really dense.

**Ashish** `1:15:59`
Yeah, this is fine. Yeah, this is good.

---

## Wrap-up

**Geoffrey** `1:16:10`
OK. All right. So I'm going to stop sharing there and we are over by 15 minutes. I'm going to transcribe that and bring it over. And then if you have time later this week for me to steal an hour of your time...

**Ashish** `1:16:17`
Right. Yep. I love it.

**Geoffrey** `1:16:30`
I don't wanna steal any of your personal time, but like, even if it's in the evening.

<!-- redacted comments -->
