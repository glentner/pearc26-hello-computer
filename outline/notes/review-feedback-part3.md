---
source: reviews/review_phase_1_part_3.md
reviewed_by: [Geoffrey R. Lentner]
date: 2026-03-22
---

# Review Feedback: Part 3

## Section: Abstract

### [FB-3.01] "Agentic assistance" — third occurrence flagged
- **Type**: word-choice
- **Severity**: must-fix
- **Quote/context**: Geoffrey: "I don't really want to say 'agentic assistance.' I want to say something a bit more bold... every letter of this paper was added to the LaTeX manuscript as part of a workflow. I spent a lot of time writing, but not directly. I was guiding the agent."
- **Action**: Reinforces FB-1.12 and FB-2.04. Replace "agentic assistance" with agent-first workflow language.

### [FB-3.02] Abstract claims not fully tied to paper body
- **Type**: structure
- **Severity**: should-fix
- **Quote/context**: Geoffrey: "some of the things that it says, I don't know that we fully tie into those... It's not as coherent as it could be because we're saying this stuff in the abstract, but at times maybe we don't address them in the body of the paper correctly."
- **Action**: Ensure every claim in the abstract (emerging framework, productivity gains, lessons learned) is substantively addressed in the paper body.

### [FB-3.03] "Love letter and cautionary tale" — reconfirmed for replacement
- **Type**: word-choice
- **Severity**: should-fix
- **Quote/context**: Geoffrey: "I think 'love letter and cautionary tale' are, um, that's a little bit too forward. We need to rephrase that."
- **Action**: Reconfirms FB-1.01. Rephrase with less overwrought wording.

### [FB-3.04] Em-dash overuse — two in abstract, pattern throughout
- **Type**: tone
- **Severity**: should-fix
- **Quote/context**: Geoffrey: "we used these em dashes twice in this abstract... the moment that I stop reading and engaging with the content and start noticing punctuation and structure, you've lost the reader."
- **Action**: Reconfirms FB-1.02. Systematic em-dash audit paper-wide.

## Section: Introduction

### [FB-3.05] "Minimal human intervention" — reads wrong for academia
- **Type**: content
- **Severity**: should-fix
- **Quote/context**: Geoffrey: "'minimal human intervention' — I think parts of the industry are there. I don't think academia is there. Most of academia is asleep... 'minimal human intervention' may be a technically accurate statement, but won't read as an accurate statement to the people reviewing this."
- **Action**: Soften or reframe "minimal human intervention" to avoid antagonizing reviewers unfamiliar with frontier agentic capabilities.

### [FB-3.06] Citation numbering out of order — alphabetical bibliography
- **Type**: factual
- **Severity**: consider
- **Quote/context**: Geoffrey notices citations appear as 7, 8, 1, 13 — "we must be by alphabetical order in the bibliography." Just observing, not flagging as a problem.
- **Action**: No action required — this is standard `acmart` behavior with alphabetical bibliography.

### [FB-3.07] Short 2-sentence paragraph — waste of vertical space
- **Type**: structure
- **Severity**: should-fix
- **Quote/context**: Geoffrey: "this is 2 sentences that showed up as its own paragraph there, and it's very distracting and it's a waste of vertical white space we're already struggling for."
- **Action**: Merge the 2-sentence paragraph ("HPC centers now face..." / "This paper offers one answer from the trenches") into the preceding or following paragraph. Reinforces FB-1.09.

### [FB-3.08] "Agentic assistance" in intro — second occurrence
- **Type**: word-choice
- **Severity**: must-fix
- **Quote/context**: Geoffrey: "Second occurrence of our mention of the fact that this paper is written agentically. I don't like calling it 'agentic assistance.' We need to rephrase it to call out the kind of more comprehensive and all-encompassing aspect of the workflow being fully agentic."
- **Action**: Reinforces FB-1.12, FB-2.04. Same systematic replacement.

### [FB-3.09] "The game is afoot" closing — overly provocative
- **Type**: tone
- **Severity**: should-fix
- **Quote/context**: Geoffrey: "I don't actually think it's true... 'HPC centers that engage early will shape the rules' — this is a very weird statement. It seems like overly — like it's dripping with this, um, pizzazz."
- **Action**: Tone down the closing of the "Mostly Harmless" subsection. The confidence is appealing but the specific claim about "shaping the rules" is overstated.

### [FB-3.10] "Hallucinations the hard way" — vague ending
- **Type**: content
- **Severity**: consider
- **Quote/context**: Geoffrey: "'leave them to discover hallucinations the hard way' — that's kind of a weird... Like I don't fully subscribe to that ending." After reflection, concedes it could tie into documentation/user guides work.
- **Action**: Either tie "hallucinations the hard way" more explicitly to the documentation/guidance pillar, or rephrase to be more specific about what "the hard way" means in HPC context.

## Section: Background

### [FB-3.11] Section 2 content is "basically perfect"
- **Type**: meta
- **Severity**: consider
- **Quote/context**: Geoffrey: "Section 2 — Section 2 on the content is perfect in terms of the length... really tight timeline... My only complaint about Section 2 is going to be formatting."
- **Action**: Reconfirms FB-1.13, FB-2.01. Content approved; only formatting (em dashes, paragraph spacing) needs attention.

### [FB-3.12] Em dashes in every paragraph of Section 2
- **Type**: tone
- **Severity**: should-fix
- **Quote/context**: Geoffrey: "Em dash, em dash, em dash. It's so many em dashes. Come on, man."
- **Action**: Em-dash audit in Section 2 specifically. Reduce without breaking technically correct usage.

## Section: Approach

### [FB-3.13] Section structure eating vertical space
- **Type**: structure
- **Severity**: should-fix
- **Quote/context**: Geoffrey: "we're making a concerted effort to weave these puns and nerd jokes in, which I love... but it's really eating us alive with the page budget here because of the vertical space." Suggests paragraph labels instead of full subsection headings.
- **Action**: Consider compressing Section 3 subsection formatting — e.g., bold inline labels instead of `\subsection{}` headers to save vertical space.

### [FB-3.14] MCP servers now public/beta — update status
- **Type**: factual
- **Severity**: must-fix
- **Quote/context**: Geoffrey: "We're fully beta now. They're fully cooked in the sense that they're public on our Purdue RCAC GitHub on github.com. They're live. Anybody can use these today."
- **Action**: Update Section 3.2 to reflect public/beta status of RCAC MCP and Globus MCP servers. Add hyperlinks to repos.

### [FB-3.15] Section 3.2 says more than necessary — compress
- **Type**: structure
- **Severity**: should-fix
- **Quote/context**: Geoffrey: "I think we say more than maybe is necessary. We could probably compress this a little bit and get the same point across."
- **Action**: Tighten Section 3.2 prose. Three paragraphs could be compressed into fewer. Hyperlink to repos to offload detail.

## Section: Discussion — "I'm Sorry, Dave"

### [FB-3.16] "I'm Sorry, Dave" paragraph approved
- **Type**: meta
- **Severity**: consider
- **Quote/context**: Geoffrey: "I like this. I like this a lot... I think this framing is good."
- **Action**: Keep mostly as-is. Minor prose polishing only.

## Section: Discussion — "Tea, Earl Grey, Hot"

### [FB-3.17] "Tea, Earl Grey, Hot" — false framing of amateur discovery
- **Type**: framing
- **Severity**: must-fix
- **Quote/context**: Geoffrey: "I don't like the framing... it suggests that we ourselves discovered this the hard way in writing this paper. I discovered that the hard way through trial and error a year ago." The paragraph incorrectly implies the authors stumbled into context engineering as novices. "That never happened. That's not the way that we structured this at all."
- **Action**: Completely reframe this paragraph. Keep the Picard/specificity tie-in and the lesson about context engineering, but attribute the learning to prior experience (July 2025), not to writing this paper. The paper is a *demonstration* of expertise, not an account of discovering it.

### [FB-3.18] Misleading footnotes about prompts
- **Type**: factual
- **Severity**: must-fix
- **Quote/context**: Geoffrey: "the quotations in the footnotes suggest those are our prompts, but our prompts are way longer than that... they're not a lie, but they're kind of a lie when they hit the reader's ear."
- **Action**: Remove the two footnotes. They cherry-pick fragments from a larger workflow and misrepresent the prompt engineering process.

## Section: Discussion — "I Know Kung Fu"

### [FB-3.19] "I Know Kung Fu" paragraph approved
- **Type**: meta
- **Severity**: consider
- **Quote/context**: Geoffrey: "I like this. I love the reference to Neo's experience... I think it's an important thing to be said."
- **Action**: Keep as-is. Content is solid.

## Section: Discussion — "The Answer is 42"

### [FB-3.20] "The Answer is 42" — tighten or trim
- **Type**: structure
- **Severity**: should-fix
- **Quote/context**: Geoffrey: "I don't hate the paragraph... But I don't think this entire — this whole paragraph isn't really doing a lot. Like this is a bunch of vertical space on this paragraph... we need to be more considered about what words we include."
- **Action**: Compress "The Answer is 42" paragraph. It's a big block with lower information density than other discussion paragraphs. Keep the 42/question framing, trim the middle.

## Section: Discussion — "Don't Cross the Streams"

### [FB-3.21] "Don't Cross the Streams" — reframe around existing HPC hardening
- **Type**: framing
- **Severity**: must-fix
- **Quote/context**: Geoffrey: "if we update this paragraph, what we should say is something to the effect of the agents have access to whatever the users do, and it was already the case that the users can be destructive unto themselves... mature, modern, major HPC centers build structure around their deployments with things like node health checks, file system protections, root-squashed file system mounts... using Linux cgroups appropriately."
- **Action**: Reframe the paragraph. The point is not "agents introduce new dangers" but "agents accelerate existing risk patterns." HPC centers already build confinement (cgroups, node health checks, root-squash, quota systems). These mechanisms contain blast radius — worst case, a user destroys their own environment, not the system. Agents raise the stakes, so existing hardening must be strengthened, not invented from scratch.

### [FB-3.22] Reproducibility concern — worth keeping but secondary
- **Type**: content
- **Severity**: consider
- **Quote/context**: The paragraph raises reproducibility of AI-assisted workflows. Geoffrey doesn't specifically comment on this but doesn't flag it for removal.
- **Action**: Keep the reproducibility mention but ensure it doesn't dominate. The hardening/confinement reframe is the primary message.

## Section: Conclusion — "End of Line"

### [FB-3.23] "Agentic assistance" in conclusion — third and final occurrence
- **Type**: word-choice
- **Severity**: must-fix
- **Quote/context**: Geoffrey: "it says 'agentic assistance' both here and in the abstract and in the intro... That's not correct. It's not 'with agentic assistance.'" Wants "agent-first" framing.
- **Action**: Reinforces FB-1.12, FB-2.04, FB-3.01, FB-3.08. Replace in conclusion with agent-first language.

### [FB-3.24] Add workflow/harness/GitHub narrative to conclusion
- **Type**: content
- **Severity**: must-fix
- **Quote/context**: Geoffrey wants the conclusion to spell out more of the actual workflow — markdown reference files, YAML frontmatter, systematic session logging, GitHub repo. Currently mentioned briefly but could be stronger.
- **Action**: Expand the second-to-last paragraph to more concretely describe the agent-first methodology and its outputs (rules, commits, session logs, planning docs). Reinforces FB-2.05.

### [FB-3.25] Strong final lines — keep verbatim
- **Type**: meta
- **Severity**: consider
- **Quote/context**: Geoffrey: "'The agentic era has arrived. HPC facilitators who engage early will shape its trajectory. Those who wait may find themselves shaped by it.' Oh. That is sharp. That's good... 'We choose engagement and we invite the community to join us.' I'm fine with that."
- **Action**: Keep the final two sentences exactly as-is. They're approved and strong.

### [FB-3.26] "Proactive engagement, not prohibition" — approved
- **Type**: meta
- **Severity**: consider
- **Quote/context**: Geoffrey: "I think our center leadership mostly agrees here... basically every strategic aspect of what Purdue is doing on the research front is dripping with AI... I think this is an accurate statement."
- **Action**: Keep "proactive engagement, not prohibition" framing in conclusion. Approved.

### [FB-3.27] Em dashes in conclusion — again
- **Type**: tone
- **Severity**: should-fix
- **Quote/context**: Geoffrey: "again with the em dashes."
- **Action**: Em-dash audit in conclusion. Part of paper-wide effort (FB-1.02, FB-3.04, FB-3.12).
