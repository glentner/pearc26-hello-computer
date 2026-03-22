---
source: reviews/review_phase_2.md
reviewed_by: [Geoffrey R. Lentner]
date: 2026-03-22
---

# Review Feedback: Phase 2

## Meta: Review Approach

### [FB-P2.00] Review conducted from outline markdown, not PDF
- **Type**: meta
- **Severity**: consider
- **Quote/context**: Geoffrey: "what I'm going to do instead of reading from the LaTeX compiled PDF for my read-through is instead go through the second draft by reviewing the markdown files because I'm considering those ground truth."
- **Action**: Confirms outline files as the canonical source. A separate LaTeX fidelity audit is planned (see FB-P2.14).

## Section: Abstract

### [FB-P2.01] "Not merely tolerated" — awkward construction
- **Type**: word-choice
- **Severity**: must-fix
- **Quote/context**: Geoffrey: "I don't know how I feel about this colon and then 'researchers want these tools integrated in their workflows, not merely tolerated.' I'd be open to something different at the end of that sentence... it's an awkward construction of a sentence. I'm stumbling over the punctuation and 'not merely tolerated.'"
- **Action**: Workshop alternative phrasing. The intent is correct (users want real integration, not grudging tolerance) but the construction is clumsy. Find something stronger and smoother.

### [FB-P2.02] Abstract overall approved as strong
- **Type**: meta
- **Severity**: consider
- **Quote/context**: Geoffrey: "I think that is way stronger than the first draft of the abstract. I think the opening is fantastic." ... "if we leave this abstract here, I think it's strong."
- **Action**: No structural changes. Only FB-P2.01 needs addressing.

## Section: Introduction — "Shall We Play a Game?"

### [FB-P2.03] Add parenthetical labels to pop-culture section titles
- **Type**: structure
- **Severity**: should-fix
- **Quote/context**: Geoffrey: "putting the parenthetical label after the pun. I think would be good because we can have our cake and eat it too... maybe make a note that we should include those in the section titles just as an aid to the reader." Examples given: "I'm Sorry, Dave" (User Support), "Tea, Earl Grey, Hot" (Context Engineering), "I Know Kung Fu" (User Expectations), "The Answer is 42" (AI Outcomes), "Don't Cross the Streams" (Cautionary Notes).
- **Action**: Add `"Title" (Descriptor)` format to all pop-culture section headings. Keeps whimsy while anchoring the reader.

### [FB-P2.04] Introduction approved — no changes
- **Type**: meta
- **Severity**: consider
- **Quote/context**: Geoffrey: "That's solid. I have nothing to add. That's a strong opener." ... "This is pretty strong. Yeah, I don't have a problem with it." ... "So I think this introduction is great."
- **Action**: No content changes to introduction.

## Section: Background

### [FB-P2.05] "Who will shape that integration?" — too combative
- **Type**: tone
- **Severity**: should-fix
- **Quote/context**: Geoffrey: "that is potentially barbed in a way that's unnecessary... We need to be more sort of hand-open, friendly invitation to join the game. Not, you know, 'ready player two'... 'are you getting on or are you being left behind?' I mean, maybe there's some truth to that, but I don't like the 'don't get left behind' thing. It's unnecessarily combative."
- **Action**: Soften closing of background section. Replace "who will shape that integration?" with language that invites rather than challenges. Align with the "ready player two" welcoming tone used in the conclusion.

### [FB-P2.06] "AI capabilities" → "AI systems" in Genesis sentence
- **Type**: word-choice
- **Severity**: should-fix
- **Quote/context**: Geoffrey: "yes, 'AI capabilities,' but maybe a better word choice would be 'systems.' National laboratories, supercomputers, and AI systems."
- **Action**: Replace "AI capabilities" with "AI systems" in the Genesis Mission Executive Order sentence.

### [FB-P2.07] Consider quoting "stands at a crossroads"
- **Type**: style
- **Severity**: consider
- **Quote/context**: Geoffrey: "Maybe it's not necessary to quote them there. We do cite them. I'm not sure if it's better or worse if we put literal quotes at it. Maybe we could quote 'stands at a crossroads.' I think that might be better."
- **Action**: Add quotation marks around "stands at a crossroads" to attribute the phrase to Deelman et al. more clearly.

### [FB-P2.08] Background opening paragraphs approved
- **Type**: meta
- **Severity**: consider
- **Quote/context**: Geoffrey: "very straightforward, matter-of-fact timeline marching through 2017 through 2026" ... "this is really good."
- **Action**: No content changes to first three paragraphs of background.

## Section: Approach

### [FB-P2.09] Repeated tool enumeration in Section 3.1
- **Type**: structure
- **Severity**: must-fix
- **Quote/context**: Geoffrey: "'Warp, Cursor, Claude Code' — we've already had that trio. That's like the third time we iterate or we sort of list tools... Maybe we don't need to list those, we can just leave it at 'modern agentic tools.'" Notes that Gemini CLI, OpenCode, JetBrains Junie also exist — listing specific tools dates quickly.
- **Action**: Remove "Warp, Cursor, Claude Code" from Section 3.1 opening. Use "modern agentic tools" or similar generic phrasing. The specific tools are already enumerated in the introduction.

### [FB-P2.10] `sinteractive` is a bad example for agents
- **Type**: factual
- **Severity**: must-fix
- **Quote/context**: Geoffrey: "the agents shouldn't be running interactive sessions, really. They should be using the batch system, right? ... the actual recommendations in our markdown files are not to use `sinteractive`... So this opening part of that paragraph could be more technically correct."
- **Action**: Replace `sinteractive` example with something agents actually use — `srun`/`sbatch` options, or batch job best practices. `myquota` is fine to keep.

### [FB-P2.11] Section 3.1 closing sentence approved
- **Type**: meta
- **Severity**: consider
- **Quote/context**: Geoffrey: "'The agent absorbs the cluster's policies before the user asks their first question.' I think that's fantastic."
- **Action**: Keep closing sentence verbatim.

### [FB-P2.12] Section 3.2 first paragraph could reflow
- **Type**: structure
- **Severity**: should-fix
- **Quote/context**: Geoffrey: "maybe we could reflow this first paragraph of the subsection to kind of at once enumerate RCAC-MCP and Globus-MCP as the two things that we've built. Overall better than the first draft."
- **Action**: Reflow Section 3.2 opening to introduce both MCP servers more cleanly as a pair.

### [FB-P2.13] Section 3.3 approved
- **Type**: meta
- **Severity**: consider
- **Quote/context**: Geoffrey: "I think that's short and concise enough and I think it's solid."
- **Action**: No changes to Section 3.3.

## Section: Discussion — "I'm Sorry, Dave" (User Support)

### [FB-P2.14] Section 4.1 approved
- **Type**: meta
- **Severity**: consider
- **Quote/context**: Geoffrey: "I think this is super strong. It's better than the first draft... Yeah, it's great."
- **Action**: No changes needed.

## Section: Discussion — "Tea, Earl Grey, Hot" (Context Engineering)

### [FB-P2.15] Closing sentences imply users get magic for free
- **Type**: framing
- **Severity**: must-fix
- **Quote/context**: Geoffrey: "I don't actually — I think this could be improved by not suggesting that the users can get magic for free with no effort... It's not 'we can do this for them' — it's 'we can help them along and sort of provide scaffolding for them to operate at a higher level.'"
- **Specific lines**: (1) "that precision must be engineered into the system, not left to the user" and (2) "every user benefits without crafting expert prompts themselves."
- **Action**: Rebalance both closing sentences. The system-wide configuration provides scaffolding, but users still need to be specific. The goal is augmented capability, not effortless magic. Frame as partnership: we provide the foundation, users still bring domain specificity.

### [FB-P2.16] "Token budgets" may be misconstrued
- **Type**: clarity
- **Severity**: must-fix
- **Quote/context**: Geoffrey: "'manage token budgets' might be misconstrued to mean like how much money do we have in our bank account with OpenAI, and not what I actually mean, which is: we have 200,000 tokens in our context window for this AI model, and we need to meaningfully manage the phases of our workflow."
- **Action**: Clarify "token budgets" to unambiguously refer to context window management (staying in the 30–60% sweet spot), not API billing. A brief parenthetical or substitution may suffice.

### [FB-P2.17] Section 4.2 overall improved
- **Type**: meta
- **Severity**: consider
- **Quote/context**: Geoffrey: "This is way better than the first draft. It largely addresses the misframing that we talked about before."
- **Action**: Address FB-P2.15 and FB-P2.16; otherwise approved.

## Section: Discussion — "I Know Kung Fu" (User Expectations)

### [FB-P2.18] Two paragraphs could merge to save space
- **Type**: structure
- **Severity**: should-fix
- **Quote/context**: Geoffrey: "I don't know that it needs to be two separate paragraphs... This is just an extended abstract. Wasting a lot of vertical space. We could probably join these two paragraphs together."
- **Action**: Merge the two paragraphs in Section 4.3 into one. Content is approved; only the paragraph break is wasteful.

### [FB-P2.19] Section 4.3 content approved
- **Type**: meta
- **Severity**: consider
- **Quote/context**: Geoffrey: "That was fantastic. I think we did a bang-up job on this one."
- **Action**: Keep content as-is, just merge paragraphs per FB-P2.18.

## Section: Discussion — "The Answer is 42" (AI Outcomes)

### [FB-P2.20] False "one session" claim — MUST-FIX
- **Type**: factual
- **Severity**: must-fix
- **Quote/context**: Geoffrey: "We did not build in one session... I spent a good 12 hours that first day... this was actually 15 sessions, not one session... this was literally — each one of those, we burned an entire context window... So this is a false statement and this is a must-fix."
- **Detail**: The annotated bibliography was built over ~15 sessions (one planning session, 13 individual reference sessions, one wrap-up) totaling ~8 hours of prompting. Each reference consumed an entire 200K-token context window in a deliberate agentic loop.
- **Action**: Replace "in one session" with accurate characterization. Could reference the multi-session agentic loop, the number of context windows consumed, or the total time invested. The positive example should still contrast with the negative (wrong Slurm commands), but must be truthful.

## Section: Discussion — "Don't Cross the Streams" (Cautionary Notes)

### [FB-P2.21] Consider mentioning user confirmation for destructive actions
- **Type**: content
- **Severity**: should-fix
- **Quote/context**: Geoffrey: "for anything destructive like an `rm` command, require user confirmation. And most agent harnesses allow for rules like this." But also: "I feel like we should allow users to take the training wheels off, but that just comes with the increased risk."
- **Action**: Briefly mention that most agentic tools support user confirmation for destructive actions as an out-of-the-box mitigation. Keep it light — acknowledge both the safety benefit and the "consenting adults" principle. Don't over-prescribe.

### [FB-P2.22] Section 4.5 approved
- **Type**: meta
- **Severity**: consider
- **Quote/context**: Geoffrey: "I think this is a big improvement... I don't have any major criticisms."
- **Action**: Only FB-P2.21 addition; otherwise keep as-is.

## Section: Conclusion — "End of Line"

### [FB-P2.23] Conclusion approved — "super powerful"
- **Type**: meta
- **Severity**: consider
- **Quote/context**: Geoffrey: "I think this conclusion is super powerful. I think if this is where we left it, I would be OK with that." ... "the closer there — 'we choose engagement, and we invite the community to join us.'" ... "That's good."
- **Action**: No changes to conclusion. Approved as-is.

## Cross-cutting

### [FB-P2.24] Vertical space / page budget remains critical
- **Type**: structure
- **Severity**: should-fix
- **Quote/context**: Geoffrey: "I'm deeply concerned about vertical space in our draft... we have a four page limit and we're occupying 5 pages with our references."
- **Action**: Continue economizing vertical space wherever possible (merge paragraphs, compress subsection headers). Investigate single-column vs. dual-column submission requirement.

### [FB-P2.25] Outline → LaTeX fidelity audit needed
- **Type**: process
- **Severity**: must-fix
- **Quote/context**: Geoffrey: "I am deeply concerned and have a lot of anxiety about the LaTeX integration from the outline... the citations are correct, but they exist in the LaTeX but they do not exist in the Markdown. And that illustrates a kind of discrepancy... that is honestly a rather precise thing... and I have some concerns from the first integration that we're not doing this well."
- **Action**: Conduct a systematic audit during integration (Phase 5) comparing each outline markdown file to the corresponding LaTeX section. Verify prose fidelity, citation presence in both formats, and figure references. This is a process concern for the integration phase, not a content revision.

---

## Summary

**Total items**: 26 (FB-P2.00 through FB-P2.25)
**Must-fix**: 6 (FB-P2.01, FB-P2.09, FB-P2.10, FB-P2.15, FB-P2.16, FB-P2.20, FB-P2.25)
**Should-fix**: 7 (FB-P2.03, FB-P2.05, FB-P2.06, FB-P2.07, FB-P2.12, FB-P2.18, FB-P2.21, FB-P2.24)
**Consider**: 11 (FB-P2.00, FB-P2.02, FB-P2.04, FB-P2.08, FB-P2.11, FB-P2.13, FB-P2.14, FB-P2.17, FB-P2.19, FB-P2.22, FB-P2.23)
