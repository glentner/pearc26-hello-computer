# PEARC26 Paper Review: Phase 1 (Part 3)

**Meeting Recording** — March 22, 2026  
**Duration:** ~1h 5m  
**Participants:** Geoffrey R. Lentner

---

## Opening

**Geoffrey** `0:04`
All right, recording has started. It is Sunday, March 22nd, quarter after 10:00 AM Eastern Time and we are going to finish up our review of the PEARC paper. In part one and part two, we did not actually get through all of the sections. I'm actually going to start over and after nearly four weeks of not looking at it, I'm going to start at the beginning and do a complete read through, but the point is also that I will get to Section 4, which is the discussion section. And Section 5, the conclusion, so-called end of line. But I need to start from the beginning, otherwise I'm not going to have the right context for myself, no pun intended.

**Geoffrey** `1:15`
OK here we go.

---

## Abstract

**Geoffrey** `1:22`
Hello Computer, HPC in the Agentic Era, myself and Ashish.

**Geoffrey** `1:31`
Here goes the abstract. *"Large language models have evolved from curiosity to copilot in under four years with the emergence of agentic AI systems that reason, plan and execute multistep tasks autonomously, HPC centers face a new category of user need. Researchers want these tools integrated into their workflows, not merely tolerated. This paper offers a practitioner's perspective from Purdue's Rosen Center for Advanced Computing"* — here in RCAC — *"where we have begun deploying system-wide configurations, custom MCP servers and user guidance for agentic tools. We discuss the balance between enablement and caution, share productivity gains and lessons learned from writing this very paper with agentic assistance."*

**Geoffrey** `2:27`
Interjection here. I'm commenting that I don't really want to say "agentic assistance." I want to say something a bit more bold. I think we really need to be punchy with the fact that this entire paper was written as part of a documented agentic workflow hosted on GitHub, so it's not an assistant. I didn't ask it to proofread my paper. Every letter of this paper was added to the LaTeX manuscript as part of a workflow. I spent a lot of time writing, but not directly. I was guiding the agent and I think we need to have something a bit more punchy. I don't want to say agentic assistance. I mean, I do call my agents assistants — TTS Assistant — but um.

**Geoffrey** `3:29`
Yeah, I think we need to be a bit more on point with that. OK, continuing — *"and outline an emerging framework for HPC centers navigating this transition."* OK, I don't know that we actually did that. Maybe. Outline an emerging framework — I think maybe we should lean into this a bit more, right? OK, so continuing with my interjection here, this is not part of the paper. I think we need to say what we're doing around, you know, configuration and MCP-based solutions to enable access to HPC and storage systems for agents. That's a thing, but part of this is a meta conversation with other facilitators and institutional leadership to engage head on this coming wave of innovation around — like this isn't just about language, this is about how we work, how research is done and at every level, like all the way up through the Department of Energy and filtering down through — now the Gemini mission has published a solicitation for HPC centers like ours and others to make themselves available as part of this ecosystem.

**Geoffrey** `5:01`
Agentic research. What does that even mean? That's kind of what I want to — part of why I want this to be a poster is that this needs to be a like a conversation and it's not a done deal. It's not that I've figured it all out. It's that I'm calling attention to the fact that this is fundamentally changing the way that we work and that we need to address it head on. And so this — carrying on now the sentence here — *"outline an emerging framework for HPC centers navigating this transition"* — maybe we can put a few sentences in here that speak to — not in the abstract, but later on. I need something that ties into that sentence, right? I think it's not hallucinated, it's just — I love this abstract, but some of the things that it says, um, I don't know. They're — I don't know that we fully tie into those, right? It's not — it's not as coherent as it could be because we're saying this stuff in the abstract, but at times maybe we don't address them in the body of the paper correctly. Anyways.

**Geoffrey** `6:10`
Continuing on again — *"equal parts love letter and cautionary tale. We argue that proactive engagement, not prohibition, is the path forward for facilitators who wish to remain relevant in the agentic era."* OK, strong sentence. I love it. We've already talked about this in part one in Ashish and I's conversation that I think "love letter and cautionary tale" are, um, that's a little bit too forward. We need to rephrase that. I do like where it's going, but that's not — I don't think that's the right word choice for us here. And also a note that we used these em dashes twice in this abstract. I don't hate em dashes, but it's a tell. And not that we're — again, not that we're hiding that we're using agents, but the golden rule here is that the moment that I stop reading and engaging with the content and start noticing punctuation and structure, you've lost the reader. And so to the extent this isn't a rule, but if there was a rule, it would be — the only rule would be if you become a distraction with the structure and form and syntax and punctuation of your writing, then now you've lost the attention of the reader and we want to hold that attention. And so I think being mindful of the very AI-ness of the writing — we need to be watchful of that.

**Geoffrey** `7:39`
OK, so that's the abstract. I shared some thoughts. I shared some thoughts in the part one on that.

---

## Section 1: Introduction — "Shall We Play a Game?"

**Geoffrey** `7:47`
Continuing on with the introduction. Section one, "Shall we play a game?" OK. *"On November 30th, 2022, OpenAI released ChatGPT as a quote research preview. Within five days it had 1,000,000 users. By January 2023, 100 million — the fastest growing consumer application in history."* Citation 7. *"The game changed overnight."* I love that. That's the great opener — again with the em dashes.

**Geoffrey** `8:24`
Continuing on. *"For those of us supporting researchers on high-performance computing systems, the implications arrived slowly and then all at once. At first, ChatGPT was a curiosity — a toy that could write passable Python functions or explain error messages with varying degrees of accuracy. Then came GPT-4"* — citation 8 — *"Claude"* — citation 1 — *"and their competitors, each iteration more capable than the last. Then came agentic AI"* — with emphasis on agentic — *"systems that don't just respond to prompts, but reason, plan and execute multi-step workflows autonomously."* Citation 13.

**Geoffrey** `9:02`
*"Today's agentic development environments — tools like Warp, Cursor, Claude Code — can read files, run shell commands, edit code, and iterate towards solutions with minimal human intervention."* I don't know about "minimal human intervention." I certainly — so now I'm commenting. Hinting on this last paragraph, couple of things. "Minimal human intervention" — I think parts of the industry are there. I don't think academia is there. Most of academia is asleep, as it were, and like — months. This agentic stuff is evolving on timescales of months, not years, and so most of academia has been left behind and has no clue what these systems are capable of yet. And "minimal human intervention" may be a technically accurate statement, but won't read as an accurate statement to the people reviewing this. But I think it's true.

**Geoffrey** `10:00`
I'm also noticing that our citations must be in alphabetical order in the bibliography, because the number order in which they appear are like — we start with seven in the first paragraph and then in the second paragraph we go citation 8, 1, 13. So I think we must be by alphabetical order in the bibliography and that's why these are out of order in the paragraph. I don't know if that's a problem. I'm just noticing it. Also with the em dashes — again, every paragraph we've got an em dash. I don't know if that's good. Um.

**Geoffrey** `10:42`
Yeah, I already have — we already have comments on this in part one. *"HPC centers now face a question with no precedent in our field. How do we engage with tools that can, in some cases, do our jobs faster than we can? This paper offers one answer from the trenches."*

**Geoffrey** `10:58`
OK, interjecting again for comment. Very short paragraph. I'm noticing — I want to say we may need to be more careful and provide specific guidance to the agent on how to integrate our thoughts because the paragraphs — I don't know. I'd have to spend more time here to see whether or not this paragraph actually merits — like this is 2 sentences that showed up as its own paragraph there, and it's very distracting and it's a waste of vertical white space we're already struggling for. Space on the page. We are over our four page limit and a new line break here I don't think made any sense.

---

## Section 1 (continued): "Mostly Harmless"

**Geoffrey** `11:39`
Continuing on. *"Mostly harmless. The Hitchhiker's Guide to the Galaxy famously summarized Earth in two words: 'mostly harmless.'"* Sorry for the pause right there. *"'Mostly harmless.' We adopt this as a working hypothesis for agentic AI in HPC workflows at Purdue's Rosen Center for Advanced Computing, RCAC. We choose proactive engagement over prohibition. Our reasoning was simple. Users will bring these tools regardless of policy. A graduate student debugging a CUDA kernel at 2 AM will reach for ChatGPT whether or not we endorse it. The question is whether we help them use it effectively or leave them to discover its hallucinations the hard way. This paper documents our early experience — system-wide configuration that exposes cluster metadata to agentic tools, custom MCP"* — called Model Context Protocol — *"servers that provide contextual help and the lessons learned from using these tools ourselves, including writing this very paper with agentic assistance. We offer this as both practical guidance and invitation. The game is afoot and HPC centers that engage early will shape the rules."*

**Geoffrey** `12:55`
This is very provocative, like it's a very strong, confident paragraph. So I'm commenting now on the last paragraph of Section 1, and let me go in reverse order here, and I think we've already commented some to this extent. Last sentence — *"we offer this is both practical guidance and invitation. The game is afoot and HPC centers that engage early will shape the rules."* I don't know that that's true. Like that's a very — I like the confidence of that statement, but I don't actually think it's true. Like somehow the HPC centers that engage early, like dictate what we're going to be doing 6 months from now or 12 months from now or 18 months from now. Well, we can always change the rules. I don't think — like this is — I don't — this is a very weird statement. It seems like overly — like it's dripping with this, um, I don't know, pizzazz, right? This cachet. But it seems a bit much.

**Geoffrey** `14:02`
I don't know. And then again with the previous statement before that — *"and the lessons learned from using these tools ourselves, including writing this very paper with agentic assistance."* Second occurrence of our mention of the fact that this paper is written agentically. I don't like calling it "agentic assistance." We need to rephrase that to be more — we need to rephrase it to call out the kind of more comprehensive and all-encompassing aspect of the workflow being fully agentic, not just "hey, ChatGPT, can you help me with a sentence?" or "can you write my abstract for me?" Like we're not one-shotting this. We built an entire like research writing harness and the entire thing is documented on GitHub. That's not assistance, that's agent-first.

**Geoffrey** `15:10`
OK, and then the sentence before that — or two sentences. Let's say I love this. I love this sentence. *"A graduate student debugging a CUDA kernel at 2:00 AM will reach for ChatGPT whether or not we endorse it."* OK, I love the example. I think we should keep that verbatim. What I like about it is that there's nothing you can do to stop a graduate student from using AI to help them write their scientific software. They're going to be using the fruits of AI labor on our systems. And so it is like there's nothing you can do or say to like have a policy against the use of AI on HPC systems. Some HPC centers may try, but I think that's a fool's errand and we would be better served hardening our system to be resilient.

**Geoffrey** `16:04`
Like the ultimate fear is that the graduate students do more harm than good using this. Graduate students were already a kind of burden on the HPC system because they're still learning and doing weird stuff with their code, right? They write scripts that fork processes endlessly, right? That write data unbounded and crash a node. And now the support team has to build — well, if they're doing a good job, then they're not just themselves returning a node to service and answering tickets and explaining to the graduate student and teaching them why what they did was messed up. They're building tools that automatically detect the fault, document what the issue was, clean and return the node to service.

**Geoffrey** `16:59`
I guess the issue here is if we're using AI, the graduate student didn't even — I mean, the graduate student didn't even know why the thing they did was wrong, but at least they know what they did. They didn't understand the ramifications or the unintended consequences. But they authored the bad code, and in this case the, you know, ChatGPT authored the CUDA kernel.

**Geoffrey** `17:26`
My hunch is by the time this becomes a real problem, it is — I think it's already the case that these frontier AI systems, if you know they're not using the like lower distilled models that are still kind of not great at something as complicated as a CUDA kernel, but if universities and computing centers proactively give the advanced — like larger frontier AI, like the Claude 4.6 Opus and the GPT 5.3 Codex, or whatever may come six months from now — the frontier systems are already far and away more capable than the graduate students are. Like this isn't an artificial graduate student. It's better than the graduate student at writing code.

**Geoffrey** `18:19`
The ideal scenario is that we get less problems coming from these graduate students. If the graduate students are doing a good job as graduate students, they are learning as they go along. So I like this statement.

**Geoffrey** `18:34`
But the follow up — *"the question is whether we help them use it effectively"* — again with the em dash — *"or leave them to discover its hallucinations the hard way."* That's an interesting, punchy sentence. Again with the cachet — *"or leave them to discover its hallucinations the hard way."* The writing is very kind of elegant, like the way that the prose are weaved together. I like the sentence, but the problem is "leave them to discover the hallucinations the hard way." Maybe you could tie that into the part where we talk about documentation and user guides for using agentic tools. I mean, my complaint was going to be — "leave them to discover the hallucinations the hard way." The hard way — what is it? What does it mean, the hard way? Like is it going to hallucinate or not? If it does hallucinate, like what are we doing to prevent hallucinations? We're not. I mean, I don't think we're really building — we're not building their agentic workflows. They are. We're giving them the tools and the environment that it's effective. This last bit — "leave them to discover hallucinations the hard way" — that's kind of a weird, I don't — I don't know. Like I don't fully subscribe to that ending and if we were going to keep it, I think we should somehow tie that in to the bit where we say that we're working on, uh, like education and user guides for using these tools effectively. Maybe that's true. I guess maybe that's valid. You know, OK, OK, fine, that's valid.

**Geoffrey** `20:19`
OK, and there were other thoughts again in part one. So moving on back to the paper.

---

## Section 2: Background

**Geoffrey** `20:24`
Section 2 background. I'm going to read a whole paragraph here. *"The trajectory from research curiosity to practical tool was swift. In 2017, Vaswani et al. introduced the transformer architecture, replacing recurrence with attention mechanisms."* Citation 10. *"By 2020, GPT-3's 175 billion parameters demonstrated that scale alone could yield emergent capabilities."* Citation 4. *"ChatGPT's November 2022 launch brought these capabilities to the general public"* — again, em dash — *"100 million users in two months."* Citation 7.

**Geoffrey** `21:05`
Fine sentence. Historical timeline. Roger, carrying on.

**Geoffrey** `21:13`
*"A parallel development transformed chatbots into agents"* — emphasis on the agents. *"The ReAct framework formalized this shift. Agentic systems interleave reasoning traces with task-specific actions, interfacing with external tools and knowledge sources rather than relying solely on training data."* Citation 13.

**Geoffrey** `21:37`
*"Today's agentic development environments implement this pattern"* — again with the em dash — *"reading files, executing commands, editing code, iterating based on observed results."* Citation 11. OK, yeah, that's fine.

**Geoffrey** `21:54`
*"The infrastructure for agentic AI has matured rapidly. Anthropic's Model Context Protocol, herein MCP, released November 2024, provides a standardized interface for AI systems to connect with external data sources and tools, analogous to how Language Server Protocol unified IDE"* — not described, but meaning Integrated Development Environment — citation 2. *"By March 2025, OpenAI and Google had adopted MCP"* — citation 12. *"By December, Anthropic donated to the Linux Foundation's Agentic AI Foundation with over 10,000 active public servers"* — citation 3.

**Geoffrey** `22:38`
That 10,000 number — so now I'm commenting on the last paragraph. Continuing with the timeline, I like the tight timeline. We have a very difficult budget for page length here, but on the background section I think these three paragraphs stitched together are like — I don't know, I don't think we can really trim much here. It's very signal to noise. It's doing a good job on the signal to noise, stitching together a complete timeline from 2017 till this last winter, crescendo in December following the Supercomputing Conference where MCP is donated to the Linux Foundation's new Agentic AI Foundation. That's great. No complaints here on any of this.

**Geoffrey** `23:28`
With the 10,000 number though, it's a good number to have. It's technically correct. As we move into the middle of 2026, I don't think that number is really meaningful because the emerging pattern is that we run MCPs as local ephemeral things with, you know, HTTP proxy and SSH proxy to resources. It's no longer meaningful to like — we don't need to host this thing. I mean, you could host it as a thing on the Internet, but like we don't need to. We don't need to host them. A lot of people, including myself, are running the MCP server as it were on localhost lazily as necessary. The harness spins it up as needed, holds on to it, times out after a while, and it just uses standard IO instead of streaming HTTP. Either is valid.

**Geoffrey** `24:38`
Anyhow, continue on with the last paragraph of Section 2. Section 2 is very short. I think Section 2 is basically perfect for HPC. *"This convergence is consequential. Dielman et al. argue that high performance computing stands at a crossroads"* — their words — citation 5. *"The Genesis Mission Executive Order, November 2025, charges the Department of Energy, herein just DOE, with uniting national laboratories, supercomputers and AI capabilities for scientific discovery."* Citation 9. *"The question is no longer whether AI will integrate with HPC workflows, but how — and who will shape that integration?"*

**Geoffrey** `25:15`
That is a strong, confident statement. It's got that same cachet of the other statements that I've commented about earlier in the paper. But I like this one. I think I want to keep it as is — again with the em dash. Em dash, em dash, em dash. It's so many em dashes. Come on, man. Um.

**Geoffrey** `25:39`
But yeah, I think Section 2 — Section 2 on the content is perfect in terms of the length, right? Again with the budget, but you know, the number of words that are in Section 2 I think is appropriate and it's got a really tight timeline walking us from, you know, "Attention is All You Need" in 2017 to ChatGPT in 2022. All of the iterations that we got from scale, ultimately leading to MCP and then the Genesis Mission and HPC. I really like our references and I really like our timeline there. My only complaint about Section 2 is going to be formatting.

---

## Section 3: Approach

**Geoffrey** `26:21`
All right, moving on to Section 3, approach. *"Our approach at RCAC combines 3 complementary strategies: system-wide agent configurations, purpose-built MCP servers and user documentation that acknowledges the reality of agentic tool adoption."*

**Geoffrey** `26:40`
Comments there in that last bit. I think maybe we could tie into the hallucination thing from earlier I was complaining about. I mean, we could stick with that. Yeah.

---

### Meta-comment on Structure

**Geoffrey** `26:55`
OK, Section 3.1 system — so we're very section — I'm going to preemptively make a meta comment about structure. We're making a concerted effort to weave these, you know, puns and nerd jokes in, which I love. I, you know, that was the first thing I did when I was forming the idea of what this paper would be. I was like, oh, you know, what if we included this for like a section title? And that's great. In this case, system-wide configuration for Section 3.1 and MCP servers for Section 3.2 is fine and then documentation guidance 3.3. Those subsections are meaningful, but because of how sort of structure-heavy we are with so many labeled — I like the idea of labeled subsections, I'm a very structured guy, but it's really eating us alive with the page budget here because of the vertical space. It's tough. We might consider a way of weaving those sections in more as like paragraph labels. Yeah, just to save on the budget. It's not the right choice. Sections matter for readability, but my goodness, we're really struggling on the vertical space here.

---

### Section 3.1: System-wide Configuration

**Geoffrey** `28:16`
OK, Section 3.1, continuing on. Section 3.1, system-wide configuration. *"Modern agentic tools"* — em dash — *"Warp, Cursor, Claude Code"* — em dash — *"look for rules files in well-known locations. We deploy cluster-wide configurations that inject HPC-specific context — which commands to use for quota checks"* — myquota, which is an us thing, that's not a Linux thing, that's an RCAC thing — *"and interactive sessions"* — sinteractive. I'm interjecting too often here. I should just read it. But myquota and sinteractive are just things that we do. Not Slurm or Linux things.

**Geoffrey** `29:00`
Generally, continuing on — *"how to load software via environment modules"* — so Lmod, again my own interjection — continuing — *"and which file systems serve which purposes. These configurations also encode prohibitions. Don't run computationally intensive work on login nodes. Don't store sensitive data in world-readable locations. Don't submit jobs without time limits. The agent learns the cluster's policy before the user asks their first question."*

**Geoffrey** `29:34`
So this is still very much a work in progress and evolving quickly. By the time the conference comes around, we'll have a much stronger case here. I have — so again, I'm commenting. This is not in the paper. I have a working version of server-wide settings JSON files and context. Whether it's loaded in by Claude or coming through the MCP, it's sort of dynamically loaded from some `/etc/agents.d` directory. I don't know if `/etc/agents.d` is going to be a thing, but I'm making it a thing and our Puppet configuration management setup is going to manage that deployment and we'll have these markdown files and version control that contains the do's and don'ts and whether you're directly on the system and those get included in the standard location. Wherever Gemini CLI looks, we'll sort of import those as it were.

**Geoffrey** `30:40`
And from MCP, we kind of force it into the system prompt by loading them and joining them together. We can proactively improve the experience and also safeguard the system by forcibly injecting this into the context. It's important for us to be good stewards and not pollute their namespace or cause any harm to their workflow. But that's an evolving thing, right? So this is good for a poster because it's an evolving thing and I'm OK saying that "we deploy" instead of "we're going to deploy" because I've already got it and it will very much be there by the time 4th week of July comes around.

---

### Section 3.2: MCP Servers

**Geoffrey** `31:22`
Continuing on, Section 3.2, MCP servers. *"We developed MCP servers"* — em dash — *"the Model Context Protocol, not the Master Control Program."* Love that Tron reference. OK, continuing. *"Though the naming coincidence feels appropriate when discussing systems that mediate between users and computational resources. RCAC MCP exposes Slurm operations like job submission, queue queries, resource monitoring, file system navigation, cluster-specific tools like myquota and jobinfo. And Globus MCP mirrors the Globus command-line interface, enabling agentic data transfers between storage endpoints."*

**Geoffrey** `32:11`
I added some words there that aren't actually in the paper that I think would be good. I'm trying to read it, but it's very structured again with the em dashes, parentheses and whatnot.

**Geoffrey** `32:24`
Continuing on. *"Both servers implement a local-first architecture. The MCP server runs as a subprocess of the user's IDE, communicating via standard in, standard out. The commands execute remotely through the user's existing SSH configuration. No new credentials, no hosted infrastructure, no additional attack surface. This pattern respects the authentication investments HPC centers have already made. If you can SSH to the cluster, your agents can too. For environments requiring centralized control, we also support hosted deployments with JSON web tokens or OIDC authentication and identity delegation via pseudo, but we default to local-first, betting that most users prefer the AI assistant on their laptop talking to the cluster rather than a shared service mediating every interaction."*

**Geoffrey** `33:23`
So comments now on these — again, there's three paragraphs. We could probably squish them into one. I don't like making big blocks, but again, the vertical space is killing us.

**Geoffrey** `33:39`
I want to add that when we first wrote this, our RCAC MCP — which could easily be adopted by and adapted by any HPC center that uses Slurm — and the Globus MCP server were very much early, like pre-alpha. We're fully beta now. They're fully cooked in the sense that they're public on our Purdue RCAC GitHub on github.com. They're live. Anybody can use these today.

**Geoffrey** `34:16`
The Globus MCP has the core capabilities right now, but there are other things that we want to implement, including more facility for Globus Compute, which kind of blurs the lines between what role each MCP service offers, but you know, going all in on Globus there and so we should kind of clean up this Section 3 to — I think we say more than maybe is necessary. We could probably compress this a little bit and get the same point across. And we could try hyperlinking to — we could hyperlink to both of those repos when we mention the MCP server names.

---

### Section 3.3: Documentation and Guidance

**Geoffrey** `35:17`
Continuing on, Section 3.3, documentation and guidance. *"Perhaps most importantly, we updated our user documentation to address the agentic tools directly. We don't pretend they don't exist or discourage their use. We explain what they can and cannot do, how to verify their suggestions, and how to report issues when AI-generated commands go wrong. We treat agentic AI as we would any other tool in the HPC ecosystem — powerful, useful and requiring appropriate guidance."*

**Geoffrey** `35:52`
Yeah, I think this — that stands on its own. I don't think we need to say anything more with documentation. It's just saying one of the — not attack surfaces — one of the surfaces with which we support agentic AI is by talking about it. This is the last thing that's lagging behind the — I have thoughts on what I want to include there. Those are not live on the Internet, but hopefully they'll be live on the Internet by the time the conference comes around. So I'm happy with that.

**Geoffrey** `36:32`
OK, so therein is everything we already reviewed in part one. Let's move on to the discussion section, Section 4, which is very heavy with these puns. We're gonna do Section 4, which from here on out we have not actually — we don't have any transcript of a review, so I'm gonna do the review for the first time on the recording.

---

## Section 4: Discussion — "I'm Sorry, Dave"

**Geoffrey** `37:08`
All right, Section 4, discussion. "I'm sorry, Dave." *"The support dynamic is shifting. Users increasingly arrive at our help desk having already consulted an AI, sometimes with correct solutions, sometimes with confident hallucinations. We've seen tickets where the user's first message includes an AI-generated Slurm script that would work perfectly on a cluster we don't operate. The irony isn't lost on us — when HAL refused to open the pod bay doors, the problem was an AI saying no. Our challenge is different — AI that says yes too readily without understanding the constraints of a particular environment. The solution isn't to compete with AI for first response"* — em dash — *"it's to ensure the AI has the context to respond correctly. Hence our investment in system prompts and MCP servers that know our clusters."*

**Geoffrey** `38:01`
I like this. I like this a lot. Commenting now on that first paragraph. "I'm sorry, Dave." Uh, I think it's on point. Yeah, I don't have any strong — you know, em dashes — but I think this framing is good. Yeah, I agree that this is kind of the evidence we were talking about. You know, the graduate student at 2:00 AM is going to reach for ChatGPT to help him author that CUDA kernel. Graduate students are already in our ticketing system, proactively — sometimes they're telling us that they're using AI. This started about two years ago. Sometimes now it's like it's sort of a foregone conclusion and I recognize that I myself use AI for everything now and the little snippets of code and scripting and tooling and whatnot that is leaking into the ticketing system conversation there. It's obvious when I go engage with it and try to understand and diagnose the issue — the user has engaged with AI.

**Geoffrey** `39:22`
Both in the work that they were doing and in trying to diagnose the issue. And I guess the problem for us is when it doesn't do a good job, it is a huge time sink and I think the industry is recognizing this if you've been paying attention at all about drive-by PRs on GitHub with AI agents run amok, sucking the time out of open source projects, just polluting the queue with slop. Our solution here is to just make it less sloppy, right? If we can improve the context, if we can do context engineering on behalf of the user without the user even necessarily needing to know that it's there, it will improve their outcomes and so stem the tide of slop in our ticketing system. Maybe we can weave something to that effect into the written section.

---

## Section 4 (continued): "Tea, Earl Grey, Hot"

**Geoffrey** `40:30`
Moving on. *"Tea, Earl Grey, hot. Captain Picard never asked the replicator for quote 'a beverage.' He specified exactly what he wanted: 'Tea, Earl Grey, hot.' Effective use of agentic AI demands similar precision. We've learned this lesson firsthand writing this paper. Early prompts like 'help me write the background section' produced generic prose. Prompts that referenced specific files and established conventions produced drafts we could actually use."*

**Geoffrey** `41:00`
*"The same principle applies to HPC workflows. 'Submit a job' fails where 'submit a GPU job to the Gautschi cluster using my lab's allocation' succeeds. Specificity is the difference between useful assistance and plausible sounding noise."*

**Geoffrey** `41:20`
OK, comments. I like the thrust of what the paragraph is trying to say. I love the tie-in to Captain Picard. But with the specific reference, I actually — I don't like the picture. I want to reframe. I want to reword this because I don't like the framing. Ironic as it is, the last sentence says "specificity is the difference between useful assistance and plausible sounding noise." This paragraph is kind of noise because I never started out like — "early prompts like 'help me write the background section'" suggests, you know, because it follows the sentence where we say "writing this paper." I never prompted it to say that.

**Geoffrey** `42:14`
All of the logs are in the GitHub repo. I have some experience with crafting agentic workflows and building agent harnesses. Um, you know, with tests and requirements and long-time-horizon task mechanisms. And so that is an important lesson to be learned by users and by the community. But I don't like the framing in this paragraph that we ourselves discovered this the hard way in writing this paper. I discovered that the hard way through trial and error a year ago, you know, in July of 2025, when I was first really digging into a lot of this stuff. That's when I really got mileage, learning the lesson about specificity and context engineering and how to structure things to drive success and avoid hallucinations. Managing your context window so that you know you stay in the smart zone and avoid the dumb zone of your context window.

**Geoffrey** `43:31`
Like I learned all of that last year and so it's an incorrect framing to suggest in this paragraph that we sort of just now discovered like amateurs trying to write this paper by like — part of the whole point of this paper about like what is it — even the meta point of authoring the paper as part of a fully formed agentic workflow is to be a thought-provoking conversation piece about what agentic research even means. And to suggest that we started this by saying "help me write the background section" — that never happened. That's not the way that we structured this at all. And so ironically the agent is — it's not really hallucination, but it's like plausible sounding noise here.

**Geoffrey** `44:26`
And it's got two footnotes there — "prompts that reference specific files and establish conventions." Footnote one and footnote 2 continuing — "produced drafts we could actually use." So footnote one is "synthesize outline/02-background.md with deep-dive notes in outline/notes/refs" and footnote 2 is "use the sample sentences from each reference summary." So those are traces of actual steps in a phase of an agentic workflow that did happen. But I — I don't even want to include the footnotes because I think it's too — like that was part of a much larger thing and just like — that was not the prompt. Like the quotations in the footnotes suggest those are our prompts, but our prompts are way longer than that.

**Geoffrey** `45:27`
So I want — so this whole paragraph. First of all, "Tea, Earl Grey, hot" — Captain Picard, specificity — beautiful, perfection. Like I want to leave that tie-in and I want to have a paragraph about context engineering. This paragraph is speaking to the long-form sort of requirements-based context engineering necessary to drive agentic workflows. I want that, but I hate the way that it suggests that we learned that lesson writing this paper. We learned that lesson last year.

**Geoffrey** `46:03`
So like that needs to be completely reformed and get rid of those footnotes because they're not a lie, but they're kind of a lie when they hit the reader's ear. If they don't have any experience there, even if they do, it's a lie because it's incorrectly suggesting the kind of strength and tone and brevity of the prompts. That is not accurate.

---

## Section 4 (continued): "I Know Kung Fu"

**Geoffrey** `46:28`
OK, rant over. Moving on. Third paragraph of Section 4. *"I know Kung Fu. Neo's instant Kung Fu download is a fantasy that dies hard. Users sometimes expect AI to make them instant experts"* — em dash — *"to transform a novice into an HPC specialist through conversation alone. The reality is more nuanced. AI makes you faster at what you already understand, not expert at what you don't. This creates what we call the expertise paradox. You need domain knowledge to verify whether AI output is correct, but the people most likely to rely heavily on AI are those without that knowledge. Our documentation explicitly addresses this: use AI to accelerate your learning, not to bypass it. Ask it to explain why, not just what. The goal is augmented expertise, not outsourced understanding."*

**Geoffrey** `47:25`
Comments. I like this. I love the reference to Neo's experience, you know, learning Kung Fu in five seconds in human time in the story of The Matrix. I think it's an important thing to be said about how some people use AI that distinguish them from others. Frontier AI in the hands of an expert, used to amplify their own capability, like a bicycle recycling momentum, is like paramount.

**Geoffrey** `48:09`
And in cases where you don't understand the space that you're working in, or some of the technical aspects of the space that you're working in, using AI as an engine for learning and learning fast is good. Using it to outsource your own understanding is bad. We'll see this pattern play out over the next year or two as AI is integrated into the education space from K through 12 up through higher education.

**Geoffrey** `48:52`
At Purdue University, we are the first in the nation to have an AI component to the undergraduate degree requirement and us at RCAC are helping shape what that is and how it plays out and that's going to be key.

**Geoffrey** `49:11`
And I, you know, I'm not sure if the kids are going to be all right here. I'm not sure. I feel lucky to have had AI come online while I've been at the stage that I'm at, having hard won my own expertise before the advent of agentic AI and having the wisdom and the maturity to recognize it for what it is, use it as an agent, use it as a tool to accelerate my own learning where my gaps are, filling in those gaps rapidly and then using it as an amplifying mechanism to replicate my own expertise at scale, doing things that I would do, that I could do, that I should do if I had the time. Now AI can do it, and I can sort of clone myself, as it were.

**Geoffrey** `50:05`
Very powerful. So I like this paragraph. I think it should exist.

**Geoffrey** `50:13`
Um, it says in here somewhere about documentation — says quote: *"Our documentation explicitly addresses this: use AI to accelerate your learning, not to bypass it."* We should include that on our documentation. I've already made a point about our documentation being like preformed, not on the open Internet yet — by the time this makes — it to — I'm curious. Now here's the conundrum. Somebody reviewing this isn't gonna find that part on the open Internet. They're gonna be like, "hey, what are you talking about? It's not there." We'll see. Maybe they'll read the GitHub repo where this transcript is, and then they'll see my comment.

**Geoffrey** `50:55`
Um. We need to get it on the Internet. I'll work on that. We're in the middle of like redoing our entire documentation stack. So you know, there's a question of where does this documentation go? So I think this paragraph is mostly OK.

---

## Section 4 (continued): "The Answer is 42"

**Geoffrey** `51:16`
Moving on. Paragraph 4 of Section 4. *"The answer is 42. Deep Thought computed the answer to life, the universe, and everything: 42. The answer was correct. The question was wrong. We've experienced both extremes. This paper's reference management — 13 sources, each with a structured deep-dive note — emerged from a single prompt asking the agent to create a research workflow. The result was more thorough than anything we would have built manually. Conversely, we've watched the same agent confidently generate Slurm commands for schedulers we don't use, citing documentation that doesn't exist. This pattern — plausible output requiring expert verification — is consistent with recent evaluations of LLMs for HPC software development."* Citation 6. *"Verification isn't optional. It's the core competency that separates productive use from cargo cult computing. The answer may be 42, but only if you ask the right question."*

**Geoffrey** `52:25`
So I don't hate the paragraph. I like the play where we're saying OK, yes, the answer is 42, but we didn't ask the right question. That very much does align with my experience of using AI. But I don't think this entire — this whole paragraph isn't really doing a lot. Like this is a bunch of vertical space on this paragraph and I don't — like there's something here, but what is — like I want to make a statement about this, but we need to be more considered about what words we include in the abstract because we're very low on space. And this is a big paragraph that is maybe less important than the other ones. Maybe we could tighten that up a little bit.

---

## Section 4 (continued): "Don't Cross the Streams"

**Geoffrey** `53:14`
OK, moving on. Final paragraph of Section 4. *"Don't cross the streams. Egon's warning about crossing the streams applies to agentic AI in HPC. Some combinations are dangerous. An agent with shell access can accidentally RM -RF a project directory. An agent managing job submissions can exhaust an allocation in hours. An agent reading environment variables might log API keys to a context window that persists beyond the session. We've implemented guardrails"* — em dash — *"confirmation prompts for destructive operations, rate limits on job submissions, explicit prohibitions on accessing credential files — but no guardrail is complete. The deeper concern is reproducibility. If an AI-assisted workflow produces a result, can another researcher reproduce it? We're still developing practices for capturing the prompts and agent interactions that contribute to scientific outcomes. The streams aren't crossed yet, but we're watching carefully."*

**Geoffrey** `54:29`
OK, comments. So "don't cross the streams" — I love that. And opening with, you know, an agent with shell access can accidentally nuke your project directory with a hasty RM -RF where it thought it was, you know — I don't know what it would be thinking, but we've seen countless examples called out from industry where you know entire cloud configurations were wiped out because an agent wanted to like redo some cloud deployment and took out an entire AWS region or something like that.

**Geoffrey** `55:05`
Like, I think this is a good thing. The larger point to be made with this paragraph, and maybe we can make it with fewer words, is the agents are going to have access to the things that we can do. And over the last decade, working in HPC applications and support, I have seen the very destructive, accidental things that, you know, even experienced faculty can do — deleting whole data sets and then having an existential crisis when we can't get it back because they only put it on the scratch file system and not on the protected file system. So like humans themselves can be an agent of destruction because of their own errant commands when they didn't, you know, they were moving too quickly.

**Geoffrey** `55:56`
Agents are like a foot gun that replicates itself at scale, right? An agent harness gone wrong can wreak havoc on a user's own data and their resources, whether it's expending all of their service units on an HPC system and running out all of their compute, wasting their time and our time. Something — there is something to be said here about crafting the, um, constraints, right? And I think the way — if we update this paragraph, what we should say is something to the effect of the agents have access to whatever the users do, and it was already the case that the users can be destructive unto themselves and the system at large. So it was already the case that mature, modern, major HPC centers build structure around their deployments with things like node health checks, file system protections, root-squashed file system mounts preventing root SSH between nodes, things that harden the system, both from a cybersecurity standpoint and from a foot gun standpoint for the users themselves and the HPC center at large, right? Like using Linux cgroups appropriately to slice resources between CPU, memory, disk IO.

**Geoffrey** `57:47`
If you can limit the blast radius of any one user, then the worst that could happen with an agent run amok is a user destroys their own environment, not the rest of the system. So that sort of containing the — you know, the confinement is something we already should be doing for the users. Now the pace has accelerated. We must do an even better job of this because the agents accelerate the accidents. So, uh, we just gotta do a good job and documentation and proactive education is where we help the users understand what these things do and can do. That's probably the best we can do to prevent them from hurting themselves. Yeah. OK.

---

## Section 5: Conclusion — "End of Line"

**Geoffrey** `58:55`
Continuing on, final section. Section 5, "End of Line," which is our conclusion. *"We began this paper with a question. How should HPC centers engage with tools that can, in some cases, outperform us at our own jobs? Our answer has been proactive engagement, not prohibition. At RCAC, we're building the infrastructure to make agentic AI a first-class citizen of the HPC ecosystem — system-wide configurations that expose cluster metadata, MCP servers that provide contextual help, and documentation that prepares users for both the capabilities and limitations of these tools."*

**Geoffrey** `59:37`
*"This work is early. We don't yet know what patterns will emerge, what pitfalls await, or how dramatically these tools will reshape our profession."*

**Geoffrey** `59:46`
*"As a meta demonstration, this paper was itself written with agentic assistance. The session logs documenting our process are available in the accompanying GitHub repository. The methodology we developed — markdown reference files, YAML frontmatter for content continuity, systematic session logging — may itself be a contribution worth exploring."*

**Geoffrey** `1:00:09`
*"The agentic era has arrived. HPC facilitators who engage early will shape its trajectory. Those who wait may find themselves shaped by it. We choose engagement and we invite the community to join us."*

**Geoffrey** `1:00:22`
End of line. OK, comments. End of line — love that we're keeping it. Um. Two paragraphs. First paragraph tells what we already told you. As the, you know, military likes to say — we're going to tell you what we're going to tell you, we'll tell you, and then we'll tell you what we told you. I don't know if anybody is going to read this and get that joke, but that opening paragraph, the conclusion section, reiterates sort of in a very concise manner what we're doing — again with the em dashes.

**Geoffrey** `1:01:05`
I'm also considering reframing this. Like "proactive engagement versus prohibition" — it's a very strong statement that I'm making on behalf of the center, but I think our center leadership mostly agrees here. It's very much the new direction and thrust of Purdue. With Purdue's new partnership with Google and everything we're doing around the Purdue Computes Initiative, the Institute for Physical AI, basically every strategic aspect of what Purdue is doing on the research front is dripping with AI and like driving AI innovation. So I think this is an accurate statement.

**Geoffrey** `1:02:00`
I don't know if anybody is actually considering prohibition seriously, but maybe they are. Yeah, I think that's fine. We can leave "proactive engagement, not prohibition." That's good. But again, with the em dash, man.

**Geoffrey** `1:02:17`
OK, last paragraph. Second to last paragraph is again reiterating that this paper was written using agents. I again — it says "agentic assistance" both here and in the abstract and in the intro where we mention "agentic assistance." That's not correct. It's not "with agentic assistance." We need to come up with a new phrase that we put in those three places. With regard to the fact that this is a fully formed agentic workflow, it's agent-first. It's not like we're writing this and we're asking the — like the agent — the agent is not the copilot. In this case, the agent is the engine and we're putting fuel in it.

**Geoffrey** `1:03:16`
And then the last thing — *"the agentic era has arrived."* Strong statement — keeping it. *"HPC facilitators who engage early will shape its trajectory. Those who wait may find themselves shaped by it."* Oh. That is sharp. That's good. OK. *"We choose engagement and we invite the community to join us."* I'm fine with that.

**Geoffrey** `1:03:37`
All right, I'm not going to read the acknowledgment section. Those are very technically crafted. And then last page is the references. Um. Yeah, we had a footnote linking to the GitHub repo. That's correct.

---

## Wrap-up

**Geoffrey** `1:03:57`
OK, there is the end of the first iteration review. We will take this transcript and form it and commit it to the repository and then use this to capture our thoughts, perspective, action items to drive a new iteration of the workflow. To revise the content in our outline and then we'll attempt a second integration where we bring that in and do version 0.5 of a manuscript.
