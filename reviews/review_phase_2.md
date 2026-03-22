# PEARC26 Paper Review: Phase 2

**Meeting Recording** — March 22, 2026
**Duration:** ~1h 7m
**Participants:** Geoffrey R. Lentner

---

## Opening

**Geoffrey** `0:05`
All right, March 22nd again, now just about 4:00 PM Eastern Time and we have now finished our review cycle and second integration. A lot of great changes in this phase.

**Geoffrey** `0:29`
I've done a little bit of a proofread, but I'm going to do a complete read-through again now.

**Geoffrey** `1:09`
So one of the things that I'm worried about that we're going to address — we're going to do a 0.5.0 release just now. We're going to keep the integration that we just did, but I am deeply concerned and have a lot of anxiety about the LaTeX integration from the outline. I'm looking at the outlines and they look fantastic. I'm just looking at them on GitHub right now and what I'm going to do instead of reading from the LaTeX compiled PDF for my read-through is instead go through the second draft by reviewing the markdown files because I'm considering those ground truth.

**Geoffrey** `2:30`
And then in a 0.5.1 release, we're going to go through another session, not as a review session, but as a polish session and audit how that content gets pulled into the LaTeX. Because there's a little bit of differences — like we don't have any figures like we do in the Markdown, and the citations are correct, but what's interesting is they exist in the LaTeX but they do not exist in the Markdown. And that illustrates a kind of discrepancy, right? It's not precisely a one-to-one relationship between the markdown files in the outline with the actual draft content. And what shows up in the LaTeX — because we're using an AI agent, we're using Claude to pull those in — that is honestly a rather precise thing. Like that's not a fuzzy thing, that's a "take these words and pull them into the `.tex` file" and I have some concerns from the first integration that we're not doing this well.

**Geoffrey** `3:51`
I'm going to go ahead and do the read-through, but I'm not going to read from the PDF. And then afterwards I'm going to try to audit that process and see if we're actually getting in the PDF what is in the markdown.

**Geoffrey** `4:10`
And then we'll do another review with our co-author Ashish and see if we have time for a Phase 3 before the deadline. All right, so taking it from the top.

---

## Abstract

**Geoffrey** `4:26`
Hello Computer: HPC in the Agentic Era, starting with the abstract.

**Geoffrey** `4:35`
*"Large language models have evolved from curiosity to copilot in under four years. With the emergence of agentic AI systems that reason, plan, and execute multi-step tasks autonomously, HPC centers face a new category of user need. Researchers want these tools integrated into their workflows, not merely tolerated. This paper offers a practitioner's perspective from Purdue's Rosen Center for Advanced Computing, RCAC, where we have begun deploying system-wide configurations, custom MCP servers, and user guidance for agentic tools. As a demonstration, every word of this manuscript was produced through an agent-first workflow, over 60 commits of iterative collaboration between human authors and AI agents documented in a public GitHub repository. We argue that proactive engagement, not prohibition, is the path forward for facilitators who wish to remain relevant in the agentic era."*

**Geoffrey** `5:39`
OK, comments. I think that is way stronger than the first draft of the abstract. I think the opening is fantastic. I don't know how I feel about this colon and then "researchers want these tools integrated in their workflows, not merely tolerated." I'd be open to something different at the end of that sentence. I mean, it's not bad, but I don't know that "not merely tolerated" is what I want to go for. I don't really have an alternate suggestion, I just feel like that could be stronger. That's a little bit — first of all, it's an awkward construction of a sentence. I'm stumbling over the punctuation and "not merely tolerated." Yeah, not sure.

**Geoffrey** `6:45`
Practitioner's perspective, yeah. RCAC, yeah. Our three pillars with the configuration, the MCP servers and the user guidance. Yeah, I think the ending of this about this being a demonstration piece — that not only are we writing about it, but we're dogfooding the process ourselves as we've gone through this process and learned to architect agentic loops ourselves. So I think in the first review we said something about wanting to include this. Ashish and I had a back and forth about whether or not to neglect that fact in the abstract and only reveal at the very end. But I actually want to include this in the abstract because I want to catch people's attention with this. It's not just that we used AI, but this — the statement here, you know, "agent-first workflow, over 60 commits of iterative collaboration between human authors and AI agents documented in a public GitHub repository." Like, that really paints a picture of there being more material than just what's in this abstract. And I wanted to lead forward with that to call it out up front and center. So I think this was the right move.

**Geoffrey** `8:14`
Last sentence — *"we argue that proactive engagement, not prohibition, is the path forward for facilitators who wish to remain relevant in the agentic era."* That last stanza is so powerful. I love the phrase "agentic era." I want to really hashtag "agentic era." That's great. OK, you know, if we leave this abstract here, I think it's strong. I don't have anything else to say about that. Maybe in Phase 3, Ashish will have something to add there, but I'm pretty happy with it.

---

## Section 1: Introduction — "Shall We Play a Game?"

**Geoffrey** `8:55`
All right, introduction. "Shall We Play a Game?" I want to call out before I start reading the draft that we're using these fun, whimsical nerd puns from computing and AI and technology in pop culture as similes for different sections of the paper, like "Shall We Play a Game?" being a substitute for the word "introduction." I think it would be helpful — because I see that I recognize "Shall We Play a Game?" as being the introduction, and I like the non-traditional kind of illustrative thing we're doing with that, not rigidly abiding by the structure of a conventional paper with words like "abstract" and "background," though we are using them. I'm wondering if we put words like "introduction" — and every other place that there's a section, like when we do, I think it's — if I look at discussion: "I'm Sorry, Dave" means user support, and "Tea, Earl Grey, Hot" is a simile for prompt engineering or context engineering, and "I Know Kung Fu" similarly for user expectations.

**Geoffrey** `10:34`
And then "The Answer is 42" speaking on AI outcomes, and "Don't Cross the Streams" being cautionary notes — putting the parenthetical label after the pun. I think would be good because we can have our cake and eat it too, as it were. So yeah, maybe make a note that we should include those in the section titles just as an aid to the reader, because I love the puns, but maybe the pun would be more powerful if we actually had that there.

**Geoffrey** `11:18`
OK, so continuing on with the introduction, "Shall We Play a Game?" *"On November 30th, 2022, OpenAI released ChatGPT as a 'research preview.' Within five days it had 1,000,000 users. By January 2023, 100 million — the fastest growing consumer application in history. The inflection point was not the technology itself, but its sudden public accessibility. For the first time, anyone could converse with a frontier language model."*

That's solid. I have nothing to add. That's a strong opener. I think it's great.

**Geoffrey** `11:55`
All right, second paragraph. *"For those of us supporting researchers on high-performance computing systems, the implications arrive slowly and then all at once. At first, ChatGPT was a curiosity, a toy that could write passable Python functions or explain error messages with varying degrees of accuracy. Then came GPT-4, Claude, and their competitors, each iteration more capable than the last. Models became multimodal, processing images, audio, and video alongside text. Then came agentic AI — systems that don't just respond to prompts, but reason, plan, and execute multi-step workflows autonomously."*

**Geoffrey** `12:36`
*"Today's agentic development environments — Warp, Cursor, Claude Code — can read files, run shell commands, edit code, and iterate toward solutions with increasing sophistication. HPC centers now face a question with no precedent in our field: how do we engage with tools that can, in some cases, do our jobs faster than we can?"*

And I think that is also equally strong. I think we did a pretty good job. There's some — it feels like we have some, like we're repeating ourselves by mentioning — we mentioned GPT-4 and then Claude, and then we mentioned Warp, Cursor, and Claude Code. We're not actually repeating ourselves, but I don't know — there might be some more elegant way of flowing this that doesn't — I don't even know what I'm trying to say. This is pretty strong. Yeah, I don't have a problem with it.

---

## Section 1 (continued): "Mostly Harmless"

**Geoffrey** `13:45`
Continuing on. "Mostly Harmless." *"The Hitchhiker's Guide to the Galaxy famously summarized Earth in two words: 'mostly harmless.' We adopt this as our working hypothesis for agentic AI and HPC. Our assessment at Purdue's Rosen Center for Advanced Computing, RCAC, is that these tools are in fact mostly harmless — frontier AI systems following instructions more reliably than many users do. They request queue policies, observe resource limits, and avoid dangerous operations when properly configured. The greatest risk lies in disengagement."*

**Geoffrey** `14:20`
*"A graduate student debugging a CUDA kernel at 2:00 AM will reach for ChatGPT, whether or not we endorse it. If we don't shape the context in which that interaction occurs, we leave both the student and the cluster exposed to preventable mistakes. We choose proactive engagement. We use these tools ourselves daily so we have a visceral understanding of their capabilities and limitations. This paper is itself a product of that practice."*

**Geoffrey** `14:52`
*"An agent-first workflow comprising rules files, session logs, annotated references, and iterative revision, all documented in a public GitHub repository. This paper documents our early experience deploying system-wide configuration, custom MCP — Model Context Protocol — servers and user guides. We offer this as both evidence and invitation."*

I think that last sentence is powerful.

**Geoffrey** `15:27`
A note on structure. Semantically, the separation of the paragraphs I think makes sense. Again, I'm deeply concerned about vertical space in our draft. I'm going to have to look into the conference guidance to see if it's a hard requirement that we submit with single column format. Because I'm really, I don't know about fitting in that four page — we have a four page limit and we're occupying 5 pages with our references. So this is a problem, and overuse of all of our section headings and judicious use of paragraph separation is eating away at our vertical space, so we need to be mindful of that.

**Geoffrey** `16:16`
I think in the second paragraph, the bit about the graduate student — again, the graduate student debugging the CUDA kernel, they're gonna do that regardless. And so in a world where agentic AI is unavoidable, and our 5,000 users are going to to some degree leverage these in their work, the greater risk actually comes from disengagement, not from engagement. So we're better off — and I guess the thrust of this, I do personally, I certainly think that it's mostly harmless, at least at this stage. In 2026 I'm having a great time, and I think this is mostly harmless. So I think our approach at jumping in feet first and directly engaging this head on and meeting our users where they are and proactively building and doing that context engineering for them is good.

So I think this introduction is great. Yeah, I think this introduction is great.

---

## Section 2: Background

**Geoffrey** `17:50`
So that was the introduction. Moving on to background. There's a lot of material in here, but we kept it pretty concise. I'll go ahead with the draft.

*"The trajectory from research curiosity to practical tool was swift. In 2017, Vaswani et al. introduced the transformer architecture, replacing recurrence with attention mechanisms. By 2020, GPT-3's 175 billion parameters demonstrated that scale alone could yield emergent capabilities. ChatGPT's November 2022 launch brought these capabilities to the general public, reaching 100 million users in two months."*

**Geoffrey** `18:30`
*"A parallel development transformed chatbots into agents. The ReAct framework formalized the shift — agentic systems interleaving reasoning traces with task-specific actions, interfacing with external tools and knowledge sources rather than relying solely on training data. Today's agentic development environments implement this pattern — reading files, executing commands, editing code, iterating based on observed results."*

**Geoffrey** `19:02`
*"The infrastructure for agentic AI has matured rapidly. Anthropic's Model Context Protocol, MCP, released November 2024, provides a standardized interface for AI systems to connect with external data sources and tools, analogous to how the Language Server Protocol unified IDE tooling. By March 2025, OpenAI and Google had adopted MCP. By December, Anthropic donated it to the Linux Foundation's Agentic AI Foundation with over 10,000 active public servers."*

**Geoffrey** `19:37`
*"For HPC, this convergence is consequential. Deelman et al. argue that high-performance computing 'stands at a crossroads.' The Genesis Mission Executive Order, November 2025, charges DOE with uniting national laboratories, supercomputers, and AI capabilities for scientific discovery. The question is no longer whether AI will integrate with HPC workflows, but how — and who will shape that integration."*

**Geoffrey** `20:07`
OK, comments, again in reverse order. "Who will shape that integration?" I think that might be a little sharper than necessary. This isn't like a cool kids club, right? "The question is no longer whether AI will integrate with HPC workflows, but how and who will shape that integration?" I mean, maybe there's something to be said for the people who understand this most, who have dived in and fully immersed themselves in this, are going to shape that integration early on. That's appropriate — that people who spent the most time with it should shape that integration. But you know, it makes it overly personal. Yeah, with like "are you going to be part of this or not?" On the one hand, there's a positive form of this that is recurring in this manuscript where we are saying like "come join us," as it were. But this kind of has a negative connotation. You know, "who will shape that integration?" — that is potentially barbed in a way that's unnecessary. I don't know that we have to quite say it like that. We need to be more sort of hand-open, friendly invitation to join the game. Not, you know, "ready player two." If we, the authors of this paper, are player one, we need a "ready player two" kind of invitation that says "come join us," not "are you getting on or are you being left behind?" I mean, maybe there's some truth to that, but I don't like the "don't get left behind" thing. It's unnecessarily combative in a way that — I don't think we need to go down that road. Our closing sentences and our sections don't need to be unnecessarily combative.

**Geoffrey** `22:07`
OK, walking it back. The Genesis Mission Executive Order, DOE, national labs, supercomputing. It says "and AI capabilities for scientific discovery." Let's — yes, "AI capabilities," but maybe a better word choice would be "systems." National laboratories, supercomputers, and AI systems. Yeah, minor word choice. Maybe systems would be better. Maybe infrastructure would be better. Supercomputers are infrastructure though. So yeah, there could be some word choice there.

**Geoffrey** `22:42`
Also, in "DOE," is the "O" capitalized? I think so. I'm not the right person to know whether DOE is supposed to be all caps or if the "O" should be lowercase. I don't know. With the national laboratories immediately following, I think it's obvious that DOE means Department of Energy.

**Geoffrey** `23:06`
I think the start of that last paragraph — "this convergence is consequential" — I like the alliteration. This happens a lot in the manuscript where we have a kind of repeat-letter alliteration that I think reads — it's very poetic the way that it reads. "Convergence is consequential." That's good.

**Geoffrey** `23:25`
And then "Deelman et al. argue that high-performance computing stands at a crossroads." I think that's actually the title of their paper. It's certainly something they say in the paper. Maybe it's not necessary to quote them there. We do cite them. I'm not sure if it's better or worse if we put literal quotes at it. Maybe we could quote "stands at a crossroads." I think that might be better.

**Geoffrey** `23:58`
Taking it back, the opening three paragraphs of this section I think are very straightforward, matter-of-fact timeline marching through 2017 through 2026, now the end of 2025. With Vaswani et al. — that's "Attention is All You Need." Most people, even if they haven't read the paper personally, would recognize the title of that influential work. There may — I don't think it's necessary for us to put that. It may be more powerful because I think everybody quotes "Attention is All You Need." Maybe it's better that we don't — just say Vaswani et al. but people would recognize it.

**Geoffrey** `24:54`
Otherwise, I think this is really good. I like, again from our earlier review, the crescendo there with Model Context Protocol joining the Linux Foundation as part of this new Agentic AI Foundation with all the big players. I think Anthropic is the founding member and then Block — I don't know if anybody knows the company called Block, but that's Jack Dorsey from back in the day on Twitter. That's his company, and some other notable AI companies are behind that foundation. I think that's the point here. Yeah, this is already shaping up very good.

---

## Section 3: Approach

**Geoffrey** `25:50`
Moving on. Section 3, Approach. The title is "Approach." This is supposed to be our work — what are we doing? I mean, I guess this is formally analogous to a methodology section. This is what are we actually engaging in practice-wise? This is our practice. To call out PEARC's mission — "approach" is fine.

**Geoffrey** `26:30`
Reading: *"Our approach at RCAC combines 3 complementary strategies: system-wide agent configurations, purpose-built MCP servers, and user documentation that acknowledges the reality of agentic tool adoption."*

That's fine.

---

### Section 3.1: System-wide Configurations

**Geoffrey** `26:48`
*"System-wide configurations. Modern agentic tools — Warp, Cursor, Claude Code — look for rule files in well-known locations. We deploy cluster-wide configurations through an `/etc/agents.d` directory hierarchy, injecting HPC-specific context: which commands to use for quota checks and interactive sessions, how to load software via environment modules, which file systems serve which purposes. These configurations also encode prohibitions: don't run computationally intensive work on login nodes, don't store sensitive data in world-readable locations, don't submit jobs without time limits. The agent absorbs the cluster's policies before the user asks their first question."*

**Geoffrey** `27:39`
I'm going to stop for comment there before I go on to the other subsections. So that last sentence, again, I think we're doing a good job with our sort of mic-drop last sentences there. "The agent absorbs the cluster's policies before the user asks their first question." I think that's fantastic. The preceding sentence about prohibitions — I think those examples are all great.

**Geoffrey** `27:59`
Starting at the beginning of this paragraph, though, here's my criticism. "Warp, Cursor, Claude Code" — we've already had that trio. That's like the third time we iterate or we sort of list tools. That's maybe not bad. I'm just — I don't know an alternative. I just don't like listing those. We've already said that — that's what the agentic tools are. Maybe we don't need to enumerate Warp, Cursor, Claude Code because there are others. Right, Gemini CLI, OpenCode. Now JetBrains has a new thing they've dropped just in the last couple of weeks called JetBrains Junie. That is analogous to Warp. So maybe we don't need to list those, we can just leave it at "modern agentic tools... We deploy cluster-wide configurations through `/etc/agents.d` directory hierarchy, injecting HPC-specific context."

**Geoffrey** `29:05`
So those two sentences together — that these tools look for rules files in well-known locations — technically a more precise statement would say that we're using this `/etc/agents.d` as a centralized location for a unified context engineering setup. And what we're actually going to do is — like Gemini CLI and Claude Code do not look in the same locations for their context and for their rules and for their settings in the system-wide locations. But what we can do is judiciously use symbolic links and references. Some of these allow for imports — you can sort of refer to files inside of these files. And in the case of our MCP server, it doesn't matter because we literally reach in there, enumerate, rip those files out, and inject them directly into the system instructions when you first connect as context for everything that the agent does.

**Geoffrey** `30:15`
But if you are sort of just vanilla SSHing yourself into the cluster, we have to take additional steps to kind of smuggle ourselves into the context. We're still exploring exactly how that works. These two sentences are not as technically correct as they could be. Further, the examples used about injecting HPC-specific context, like which commands to use for quota checks — `myquota`, that's correct — but interactive sessions — `sinteractive`. So `sinteractive` is a cool thing that is — like that is in some ways a good illustrative example because both `myquota` and `sinteractive` are things that are specific to RCAC that the agent would not know a priori. It's not like all Slurm clusters and all Linux servers have these commands, but we do, and so that's really relevant context.

**Geoffrey** `31:21`
But the agents shouldn't be running interactive sessions, really. They should be using the batch system, right? Humans use `sinteractive` as a wrapper around the `salloc` command. But the agent — I don't think that's a good example for the agent, right? Because why would the agent run an interactive session? The agent should use `srun` or `sbatch`. Like the recommendations — the actual recommendations in our markdown files are not to use `sinteractive`. So this opening part of that paragraph could be more technically correct about the actual wiring of how these things connect to each other, and certainly use a better example than `sinteractive`.

**Geoffrey** `32:11`
Maybe we could say something about best practice for the options for `sbatch`, or we could maybe tighten this up and save some space because we call out the idea of "which file systems serve which purposes." `myquota` kind of builds on that, but there might be something else we can include in there other than `sinteractive`.

---

### Section 3.2: MCP Servers

**Geoffrey** `32:42`
OK, moving on. MCP servers. *"We developed MCP servers — the Model Context Protocol, not the Master Control Program, though the naming coincidence feels appropriate. RCAC-MCP exposes Slurm operations: job submission, queue queries, resource monitoring, file system navigation, and cluster-specific tools like `myquota` and `jobinfo`. Globus-MCP provides agentic data transfers between storage endpoints. Both are publicly available on GitHub."*

**Geoffrey** `33:16`
So let me just carry on with the second paragraph in that subsection.

*"Both servers implement a local-first architecture (Figure 1). The MCP server runs as a subprocess of the user's IDE, communicating via standard in/standard out. Commands execute remotely through the user's existing SSH configuration. No new credentials, no hosted infrastructure, no additional attack surface — if you can SSH to the cluster, your agent can too. For environments requiring centralized control, we also support hosted deployments with JSON Web Tokens and OIDC authentication and identity delegation."*

**Geoffrey** `33:54`
Comments — that last bit about JWT (JSON Web Tokens) and OIDC authentication — that's maybe similar to how you might run something yourself. CI Logon is — it exists and it's there, although I haven't finished going through that. So that part is still a work in progress. I think that last paragraph is really solid now, and it's important because honestly, for most users, I think the right approach is to do this SSH bridge for exactly the reasons that are mentioned. No new credentials, no hosted infrastructure, no additional attack surface.

**Geoffrey** `34:42`
Because the alternative would be a centrally hosted HTTP web service that needs authentication. That's less portable to other centers because that's more of a customizable thing. And the way that's implemented — if you read the figure, which is not included in the manuscript — is to run the service as root and then have a user mapping file the way that Globus does. We at Purdue have a mapping file that maps your identity to the local Linux user account and then does a fork to run the process as the user. You'd either have to run that on the login node or host something that walks and talks like a login node as an auxiliary node adjacent to the cluster. There are just so many moving parts to that it becomes rickety and complicated — an additional maintenance burden, an additional attack surface.

**Geoffrey** `36:11`
And frankly, these agents are acting as surrogates to the user. I think it's way more elegant and way simpler of a solution just to have the MCP server hold an SSH bridge. And in our user guides we have specific recommendations for user SSH configurations to set up how to access our clusters already with the master — again, that's a repeat thing. SSH has these parameters that you can put in your user SSH config that use sockets to create an existing — once the first connection is made, it multiplexes across that existing connection over a socket so that every subsequent command has millisecond delay. There's no handshake or anything. It's the same existing connection, all commands traverse that single bridge and it's just way more elegant and requires no additional burden.

**Geoffrey** `37:22`
So I think having that paragraph in there is great, and honestly we can't have the figure in the extended abstract in the manuscript, but having a figure that illustrates these different architectures would be good for the poster. Now that first paragraph for this subsection, I think is good. It's a little clumsy how we list the — so maybe we could reflow this first paragraph of the subsection to kind of at once enumerate RCAC-MCP and Globus-MCP as the two things that we've built. Overall better than the first draft.

---

### Section 3.3: Documentation and Guidance

**Geoffrey** `38:23`
OK, last subsection — documentation and guidance.

*"Perhaps most importantly, we update our user documentation to address agentic tools directly. We don't pretend they don't exist or discourage their use. We explain what they can and cannot do, how to verify their suggestions, and how to report issues when AI-generated commands go wrong. We treat agentic AI as we would any other tool in the HPC ecosystem — useful and requiring appropriate guidance."*

**Geoffrey** `38:51`
I think that's short and concise enough and I think it's solid. I don't have any strong complaints. Again, while the two MCP tools are now publicly accessible, the user documentation is not yet generally available on our public documentation site, so that's something that we'll have to get done before the conference opens. I agree. So we can't really document everything. I don't think it's really our place to be the end-all, be-all source of information about agentic AI and agentic workflows, but specifically how that intersects with high-performance computing — I think that is our job. And I have a new training that I'm developing, a workshop for Purdue and the larger ACCESS and NAIRR ecosystem around agentic workflows in HPC that will be included on that website — RCAC's public documentation.

**Geoffrey** `40:10`
Yeah, I think user education is a huge pillar at avoiding problems.

---

## Section 4: Discussion

**Geoffrey** `40:45`
Moving on to Section 4, the discussion section, 5 subsections with pop culture references as the subsection headings. As I said in the introduction, it might be helpful to include their more traditional section titles alongside the puns. So for section 4.1, "I'm Sorry, Dave" — you know, including the full 4.1 "I'm Sorry, Dave" and then "(User Support)" in parentheses. I think that might actually be an improvement and an aid to the reader because we have our fun and our whimsy, and we're sort of — maybe the utility of having the pop culture reference and nerd pun kind of speaks to the mental perspective, like where are we coming from? I can't pretend to not have that pop culture reference going all the way back to the '80s, which is where a lot of the great examples for human-computer interaction and artificial intelligence come from.

**Geoffrey** `42:02`
So I think there's actually some utility in these puns, but giving them specific numbers — the 4.1 in front of it would give it that sort of anchor. But then putting "(User Support)" in parentheses gives it — it ties it back to a traditional purpose.

---

### Section 4.1: "I'm Sorry, Dave" (User Support)

**Geoffrey** `42:42`
OK, "I'm Sorry, Dave." *"The support dynamic is shifting. Users increasingly arrive at our help desk having already consulted an AI, sometimes with correct solutions, sometimes with confident hallucinations. We've seen tickets where the user's first message includes an AI-generated Slurm script that would work perfectly on a cluster we don't operate. The irony isn't lost on us — when HAL refused to open the pod bay doors, the problem was an AI saying no. Our challenge is different: AI that says yes too readily without understanding the constraints of a particular environment. The solution isn't to compete with AI for first response — it's to ensure that AI has the context to respond correctly. Hence our investment in system prompts and MCP servers that know our clusters."*

**Geoffrey** `43:37`
I think this is super strong. It's better than the first draft. I think the "I'm Sorry, Dave" / user support angle — I think this is great. Yeah, it's great.

---

### Section 4.2: "Tea, Earl Grey, Hot" (Context Engineering)

**Geoffrey** `43:54`
OK, 4.2 "Tea, Earl Grey, Hot." *"Captain Picard never asked the replicator for 'a beverage.' He specified exactly what he wanted: 'Tea, Earl Grey, hot.' Effective use of agentic AI demands similar precision, and that precision must be engineered into the system, not left to the user."*

**Geoffrey** `44:12`
OK, I'll continue reading and then I'll provide my comments. *"Context engineering is the practice of structuring information, rules, and reference material so that an agent produces reliable output from the outset. We developed this discipline through a year of iterative practice before beginning this paper, learning which context formats yield consistent results, how to manage token budgets across long workflows, and how to decompose complex tasks into verifiable steps."*

**Geoffrey** `44:47`
*"The same principles apply to HPC. 'Submit a job' fails, where 'submit a GPU job to the Gautschi cluster using my lab's allocation' succeeds — but the real leverage comes from embedding that specificity into system-wide configuration so that every user benefits without crafting expert prompts themselves."*

**Geoffrey** `45:12`
OK, comments. This is way better than the first draft. It largely addresses the misframing that we talked about before. I like that we're sort of calling out the definition of context engineering. It's not necessarily the case that our reviewers and our readers are gonna have a good working definition of what we mean when we say "context engineering." And I like the called-out examples of which formats are we using, how do we manage our token budgets.

**Geoffrey** `45:43`
That specifically — "manage token budgets" might be misconstrued to mean like how much money do we have in our bank account with OpenAI, and not what I actually mean, which is: we have 200,000 tokens in our context window for this AI model, and we need to meaningfully manage the phases of our workflow with specific actionable steps that fit within that context window. To maintain — you know, we want to be somewhere between 30% and 60% of our context window to be in that golden region of outcome success, before we get into the danger zone. As we approach 80–90% of our context window, things go sideways — it starts to hallucinate and do weird things. So speaking to that illustrates our point that we've been doing this for a while now, and this very paper was constructed using a similar workflow that's on full display for everybody to go look at.

**Geoffrey** `47:05`
But what I'm going to criticize is both the opening two sentences where it says "that precision must be engineered into the system, not left to the user" and then similarly the last sentence of the second paragraph: "the real leverage comes from embedding that specificity into system-wide configurations so that every user benefits without crafting expert prompts themselves."

**Geoffrey** `47:34`
The good news is that there's some grain of truth to this, and it has obvious parallels — when anybody who has any experience with agentic workflows, your investments in context engineering compound over time. And you become more and more effective over shorter and shorter time horizons by taking and distilling out the kinds of prompt engineering that you're doing, whether that's across an entire system or in a specific project. You take your lessons learned and distill them into a rule or some kind of stored procedure.

**Geoffrey** `49:14`
So these closing sentences on both of those paragraphs do speak to that in some sense — this notion of sort of taking larger and larger chunks and distilling them out into capabilities that you can reach for at a moment's notice. And there is some of that that we can do on behalf of users — like we can make every user more effective when they log into our system.

**Geoffrey** `50:07`
But the bad news, and what I don't like about these closing sentences of these two paragraphs in this subsection, is this "without crafting expert prompts themselves." There's some truth to that — like they're not going to craft expert prompts themselves — but we want them to. The goal — like they should be — somebody in their lab should understand this. And we should be showing them how to do this. So I don't actually — I think this could be improved by not suggesting that the users can get magic for free with no effort. The whole "Tea, Earl Grey, Hot" — specificity matters. The users still need to be specific. We can help them in that endeavor, but I don't know that I like the way that we've left off these paragraphs by suggesting that the user won't need to, if we do a good job of our context engineering in the system instructions. It's balance, right? It's both. It's not "we can do this for them" — it's "we can help them along and sort of provide scaffolding for them to operate at a higher level."

---

### Section 4.3: "I Know Kung Fu" (User Expectations)

**Geoffrey** `51:37`
OK, section 4.3, moving on. "I Know Kung Fu." This is user expectations. *"Neo's instant Kung Fu download is a fantasy that dies hard. Users sometimes expect AI to make them instant experts — to transform a novice into an HPC specialist through conversation alone. The reality is more nuanced: AI makes you faster at what you already understand, not expert at what you don't. This creates what we call the expertise paradox: you need domain knowledge to verify whether AI output is correct, but the people most likely to rely heavily on AI are those without that knowledge."*

**Geoffrey** `52:13`
*"Our documentation explicitly addresses this: use AI to accelerate your learning, not to bypass it. Ask it to explain why, not just what. The goal is augmented expertise, not outsourced understanding."*

**Geoffrey** `52:33`
OK, comments. That was fantastic. I think we did a bang-up job on this one. I don't know that it needs to be two separate paragraphs. Like it's not a problem semantically — I don't think it's an issue — but it's maybe unnecessary for this. This is just an extended abstract. Wasting a lot of vertical space. We could probably join these two paragraphs together. It ties into — yeah, we should speak to this in our user guides, this notion that AI is an amplifying force that replicates your own capabilities — like a bicycle, right? You still need your legs. You're still going to put in just as much force. Riding your bicycle doesn't make you less tired than running, but it amplifies and conserves that momentum and compounds that momentum. And so AI is not a substitute for expertise.

So this is, yeah, this is correct. That's great.

---

### Section 4.4: "The Answer is 42" (AI Outcomes)

**Geoffrey** `53:51`
OK, moving on. Section 4.4, "The Answer is 42," speaking on AI outcomes.

*"Deep Thought computed the answer to life, the universe, and everything: 42. The answer was correct. The question was wrong. We've experienced both extremes — an agent that built our 13-source annotated bibliography in one session, and the same agent confidently generating Slurm commands for schedulers we don't use. Plausible output requiring expert verification is consistent with recent evaluations of LLMs for HPC software development. Verification isn't optional — it's the core competency that separates productive use from cargo-cult computing. The answer may be 42, but only if you ask the right question."*

**Geoffrey** `54:37`
So this is strong. It's a good paragraph. My primary complaint is in the middle. Here we say "we've experienced both extremes — an agent that built our 13-source annotated bibliography in one session, and the same agent confidently generating Slurm commands for schedulers we don't use." I don't actually know what LLM the user was leveraging when they created that — it could have been Gemini or ChatGPT, I don't know. But the what's supposed to be the positive outcome, which is this thing where we say "an agent that built our 13-source annotated bibliography in one session" — this needs to be fixed.

**Geoffrey** `55:31`
We did not build in one session. My definition of a session is a context window. You could define a human session as like sitting down. I spent a good 12 hours that first day setting up the repository, setting up the template for LaTeX, gathering the information, the call for proposal, describing what the goals of our project were, and doing the literature search for all of the references that we wanted. We can't include all references, so we've got a budget of 10 to 15 and we need to pick the seminal papers that dot the timeline.

**Geoffrey** `56:24`
After debating that list and finally aligning on what those now 13 references were going to be, we planned, we researched, planned, and engineered in an agentic loop — just like we have in each of the phases of this project that we're building this manuscript. Each of the 13 had their own phase with concrete steps to pull in all the necessary context. What are our goals? What is it that we want to say in this project? Doing a full independent summary with all of that source's sources and distilling that down into something meaningful for our paper. And then specifically crafting a section of that annotated bibliography for every single entry of how that specific source relates — how does that tie into what we were doing? And sample sentences that we could include and a first attempt at a mini paragraph that may potentially get pulled into the paper related to that reference.

**Geoffrey** `58:08`
Each one of those, we burned an entire context window. So this was literally — right as I think Claude 4.6 Opus had just come out the day before — and I believe we have a 200,000 token context window. The way that we set up our agentic loop was explicitly to wipe the memory and create a new session. As far as Warp is concerned, the agentic development environment that we're using to execute this workflow, we said `/new` — clean slate — and then ran our continuation prompt to go pull everything in, identify the next phase, and then work on that one.

**Geoffrey** `59:05`
So this was actually 15 sessions. We had the first one where we did all our research and planning and built a continuation prompt, and then for each of the 13, that was an entire context window for each. And then we had a last one where we sort of wrapped up. So that was actually 15 sessions, not one session.

**Geoffrey** `59:29`
So this is a false statement and it's misleading. I don't want people to think that we one-shotted our annotated bibliography. It was an 8-hour — I spent 8 hours prompting that and running our agentic loop. So this is a false statement and this is a must-fix.

---

### Section 4.5: "Don't Cross the Streams" (Cautionary Notes)

**Geoffrey** `1:00:07`
All right, I'm back. Continuing on — 4.5, "Don't Cross the Streams." These are cautionary notes.

*"Egon's warning about crossing the streams applies to agentic AI and HPC: some combinations are dangerous. An agent with shell access can `rm -rf` a project directory. An agent managing job submissions can exhaust an allocation in hours. An agent reading environment variables might log API keys to a context window that persists beyond the session."*

*"But these risks are not new. Users have always been capable of destroying their own data, exhausting their allocations, and exposing credentials. Mature HPC centers already build confinement: cgroups to isolate resources, node health checks, root-squashed file systems, quota enforcement. These mechanisms contain the blast radius so that one user's mistake cannot cascade across the system."*

**Geoffrey** `1:01:07`
*"Agents accelerate the pace of potential errors, which means existing hardening must be strengthened, not invented from scratch. We are also developing practices for capturing agent interactions that contribute to scientific outcomes, because reproducibility in AI-assisted research remains an open question."*

**Geoffrey** `1:01:26`
OK, comments, closing out Section 4. I think this is a big improvement. This is a pretty good — I don't have any major criticisms for anything in these two paragraphs.

**Geoffrey** `1:01:42`
"An agent with shell access can `rm -rf` a project directory." The one thing we could do in here — as we talk about confinement, we've already mentioned in our Section 3 approach about what we're doing. One of the pillars of our approach is on-system configuration. And my hope would be that users, if they're in the loop — which I would recommend for the vast majority of users — is to not try to do this fully autonomously. Let the agents drive your sessions but stay in the loop, and for anything destructive like an `rm` command, require user confirmation. And most agent harnesses allow for rules like this.

**Geoffrey** `1:02:45`
If a user disables that, there's no saving them other than, you know, things like snapshots and disaster recovery, copies of datasets. I mean, there are things that we can do.

**Geoffrey** `1:03:00`
So I think this is strong on its own. I'm pretty happy with Section 4, subsection 4.5. The only thing that we could potentially add is a couple of words that call out from these examples the fact that any of these footguns should come out-of-the-box with user confirmation requirements for destructive actions. Maybe. I don't know how I feel about a lot — I mean, I feel like we should — like we're all consenting adults here. Speaking from the Zen of Python, we should be allowed to do what we want with our tools, so there should be some trade-off here. I feel like we should allow users to take the training wheels off, but that just comes with the increased risk. So I don't, I don't know. This is good. I don't have any complaints there.

---

## Section 5: Conclusion — "End of Line"

**Geoffrey** `1:04:02`
Moving on to our conclusion. "End of Line."

*"We began this paper with a question: how should HPC centers engage with tools that can, in some cases, outperform us at our own jobs? Our answer has been proactive engagement, not prohibition. At RCAC, we are building the infrastructure to make agentic AI a first-class citizen of the HPC ecosystem: system-wide configurations that expose cluster metadata, MCP servers that provide contextual help, and documentation that prepares users for both the capabilities and limitations of these tools."*

*"This work is early. We don't yet know what patterns may emerge, what pitfalls await, or how dramatically these tools will reshape our profession."*

*"As a meta-demonstration, this paper was itself produced through an agentic workflow. No prose was written by hand. Human authors defined rules, curated references, reviewed transcripts, and guided iterative revision. AI agents executed the research, planning, drafting, and integration. The entire process — comprising over 60 commits, session logs, planning documents — is available in the accompanying GitHub repository. The methodology itself may be a contribution worth exploring."*

*"The agentic era has arrived. HPC facilitators who engage early will shape its trajectory. Those who wait may find themselves shaped by it. We choose engagement, and we invite the community to join us."*

*"End of line."*

**Geoffrey** `1:05:48`
OK, comments. I think this conclusion is super powerful. I think if this is where we left it, I would be OK with that. I like the opening of that last couple of sentences — "the agentic era has arrived." That's the title. We leave off the abstract with that phrase. I like that we're leaning into that phrase, "agentic era." And then the closer there — "we choose engagement, and we invite the community to join us."

**Geoffrey** `1:06:23`
This kind of thing where it's like a conversation piece is why this is a really good fit for a poster as opposed to merely a paper, is because at the poster reception, this is where you can kind of foster those community conversations, right? PEARC is a community conference about practice and experience in advanced research computing.

**Geoffrey** `1:06:44`
So that is what I'm talking about when I said earlier about having more of a "ready player two" attitude where we have an open hand of invitation and a friendly welcoming to like "hey, come join us" as opposed to "get on the train or we're leaving you behind and you'll regret it" — which is unnecessarily combative. I think we do a good job of having a positive connotation in the conclusion.

**Geoffrey** `1:07:14`
So that's good. On the third paragraph in the conclusion section where we describe our workflow, I think that's good. This is a marked improvement from just saying "agent-assisted," which was not correct. And then we close out with "End of Line." Classic.

---

## Closing

**Geoffrey** `1:07:38`
OK, we will leave it at that. We need to address everything that I've mentioned here, make some minor adjustments.
