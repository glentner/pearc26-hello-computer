---
sources:
  - outline/notes/review-feedback-part1.md
  - outline/notes/review-feedback-part2.md
  - outline/notes/review-feedback-part3.md
total_items: 52
---

# Review Synthesis: Cross-Cutting Themes

This document groups all feedback from the three review sessions into
actionable themes. Each theme lists the FB-IDs it consolidates, the
sections affected, and the revision action. Themes are ordered by
severity and breadth of impact.

---

## Theme 1: "Agentic assistance" → "agent-first workflow" [MUST-FIX]

**FB-IDs**: FB-1.12, FB-2.02, FB-2.04, FB-3.01, FB-3.08, FB-3.23
**Sections**: Abstract, Introduction, Conclusion (3 occurrences)
**Parts**: 1, 2, 3 (raised in every session)

The phrase "agentic assistance" appears three times and fundamentally
misrepresents the paper's process. The workflow was agent-first — not
AI proofreading or one-shot generation. Every word was produced through
a documented agentic workflow with rules, session logs, commits, and
planning documents on GitHub.

**Revision action**: Replace all three occurrences with language
conveying agent-first, comprehensive workflow. In the abstract, make
it a punchy, enticing invitation ("come see what an agent-first paper
looks like"). In the conclusion, pair the reframe with expanded
workflow narrative (see Theme 6).

---

## Theme 2: "Mostly Harmless" argument misalignment [MUST-FIX]

**FB-IDs**: FB-1.10, FB-1.11, FB-2.10, FB-3.09, FB-3.10
**Sections**: Introduction ("Mostly Harmless" subsection)
**Parts**: 1, 3

The current argument is: "users will do it anyway, so engage." That's
a fatalism argument ("resistance is futile"), not a "mostly harmless"
argument. The framing should be cautious optimism — the tools themselves
are mostly safe, and frontier AI is arguably more reliable than
unsupervised graduate students.

**Revision action**:
1. Realign the core argument: engagement because the tools are good,
   not because resistance is futile.
2. Add the dog-fooding angle: HPC staff should adopt these tools
   themselves for visceral understanding. Don't be the ostrich — engage
   or risk being outpaced by users and colleagues.
3. Work in the point that agents follow policy more reliably than users
   (FB-2.10).
4. Tone down the closing ("the game is afoot" / "shape the rules" is
   overstated per FB-3.09).
5. Tie "hallucinations the hard way" to the documentation/guidance
   pillar or rephrase (FB-3.10).

---

## Theme 3: "Tea, Earl Grey, Hot" framing error [MUST-FIX]

**FB-IDs**: FB-3.17, FB-3.18
**Sections**: Discussion ("Tea, Earl Grey, Hot" subsection)
**Parts**: 3

The paragraph falsely implies the authors discovered context engineering
as amateurs while writing this paper. Geoffrey learned these lessons
through a year of practice (July 2025). The two footnotes cherry-pick
fragments from a larger workflow and misrepresent the prompt engineering
process.

**Revision action**: Completely reframe. Keep the Picard/specificity
tie-in and the lesson about context engineering, but attribute the
learning to prior experience. The paper is a *demonstration* of
expertise, not a discovery narrative. Remove both footnotes.

---

## Theme 4: "Don't Cross the Streams" reframe [MUST-FIX]

**FB-IDs**: FB-3.21, FB-3.22
**Sections**: Discussion ("Don't Cross the Streams" subsection)
**Parts**: 3

The current framing implies agents introduce novel dangers. The correct
framing: agents accelerate existing risk patterns. HPC centers already
harden systems (cgroups, node health checks, root-squash, quota
systems, filesystem protections). These confinement mechanisms contain
blast radius — worst case, a user destroys their own environment, not
the system. Agents raise the pace, so existing hardening must be
strengthened, not invented from scratch.

**Revision action**: Reframe around "accelerating existing risk
patterns." Keep the Ghostbusters reference and the enumeration of
specific dangers, but pivot the argument to strengthening existing
confinement rather than inventing new guardrails. Keep reproducibility
as a secondary concern, not the main point.

---

## Theme 5: Missing agentic workflow narrative [MUST-FIX]

**FB-IDs**: FB-2.05, FB-3.24, FB-3.02
**Sections**: Introduction or early Approach + Conclusion
**Parts**: 2, 3

The paper's unique contribution — the actual agent-first workflow
process — is underrepresented. Between the historical retrospective
and the enumeration of RCAC initiatives, the paper doesn't explain
what "agentic workflow" actually means in practice: 68+ commits,
6 hours on rules of engagement before writing a single word, 30+
hours of research and planning, session logs, markdown reference
files, YAML frontmatter for content continuity.

**Revision action**: Add a paragraph (Introduction or early Approach)
describing the actual process. In the conclusion, expand the
second-to-last paragraph to concretely describe the methodology and
its outputs. Ensure abstract claims about "lessons learned" and
"emerging framework" are substantively addressed in the body.

---

## Theme 6: AI-authorship disclosure strategy [MUST-FIX]

**FB-IDs**: FB-2.02, FB-2.03, FB-2.06
**Sections**: Abstract, Conclusion, Acknowledgments
**Parts**: 2

**Resolved**: Punchy, enticing statement in the abstract (invitation,
not admission). Detailed workflow/harness/GitHub narrative in closing
statements. ACM policy compliance in acknowledgments (secondary
vehicle — most readers won't look there).

This theme is addressed through Themes 1 and 5 above.

---

## Theme 7: Em-dash overuse [SHOULD-FIX]

**FB-IDs**: FB-1.02, FB-3.04, FB-3.12, FB-3.27
**Sections**: All (flagged in abstract, intro, background, conclusion)
**Parts**: 1, 3

Em dashes appear in nearly every paragraph. While technically correct,
the frequency is an AI-tell that distracts the reader. The golden rule:
"nobody cares until they notice."

**Revision action**: Paper-wide em-dash audit during each section
revision. Replace with colons, commas, parentheses, or restructured
sentences where another punctuation choice is equally good. Keep em
dashes only where they are genuinely the best option. Target: no more
than one em dash per paragraph, and aim for several paragraphs in a
row without any.

---

## Theme 8: Overly flowery / clever language [SHOULD-FIX]

**FB-IDs**: FB-1.01, FB-1.03, FB-1.04, FB-1.08, FB-3.03, FB-3.05
**Sections**: Abstract, Introduction
**Parts**: 1, 3

The agent "turned it up to 11." Pop-culture section titles stay (they're
intentional, thematic, self-aware). Inline cleverness gets trimmed.

Specific items to address:
- "Love letter and cautionary tale" → rephrase (FB-1.01, FB-3.03)
- "From the trenches" → remove (FB-1.08)
- "Minimal human intervention" → soften (FB-3.05)
- General: reduce similes and overly artful phrases

**Revision action**: During each section revision, apply the golden
rule: if the reader notices the style over the content, trim it. Keep
the voice and energy; lose the verbal gymnastics.

---

## Theme 9: Paragraph structure / vertical space [SHOULD-FIX]

**FB-IDs**: FB-1.09, FB-3.07, FB-3.13, FB-3.15
**Sections**: Introduction, Approach
**Parts**: 1, 3

Too many short paragraphs waste vertical space in single-column format.
The 2-sentence paragraph in the Introduction is especially wasteful.
Section 3's subsection headers eat significant space.

**Revision action**:
1. Merge short paragraphs where logical (especially the 2-sentence
   paragraph in Introduction).
2. Consider compressing Section 3 subsection formatting — e.g., bold
   inline labels (`\paragraph{}`) instead of `\subsection{}` headers.
3. Compress Section 3.2 from three paragraphs to fewer; hyperlink to
   repos to offload detail.

---

## Theme 10: "The Answer is 42" — tighten [SHOULD-FIX]

**FB-IDs**: FB-3.20
**Sections**: Discussion ("The Answer is 42" subsection)
**Parts**: 3

Big paragraph with lower information density than other discussion
subsections. The 42/question framing is good but the middle is flabby.

**Revision action**: Compress. Keep the Deep Thought opening and the
"only if you ask the right question" closing. Trim the middle examples
and tighten the prose.

---

## Theme 11: Approach section updates [SHOULD-FIX / MUST-FIX]

**FB-IDs**: FB-2.07, FB-2.08, FB-2.09, FB-3.14, FB-3.15
**Sections**: Approach (all subsections)
**Parts**: 2, 3

The three-pillar structure is confirmed and accurate. Updates needed:
- MCP repos are now public/beta, not pre-alpha (FB-3.14, must-fix)
- Word choice in 3.1 could be stronger and more direct (FB-2.08)
- Consider name-dropping `/etc/agents.d` convention (FB-2.09)
- Compress Section 3.2 prose (FB-3.15)

**Revision action**: Update status, tighten prose, add hyperlinks
to public repos. Consider `/etc/agents.d` name-drop.

---

## Theme 12: Introduction flow and content [SHOULD-FIX]

**FB-IDs**: FB-1.05, FB-1.06, FB-1.07
**Sections**: Introduction (opening paragraphs)
**Parts**: 1

- "The game changed overnight" misframes the inflection point — should
  emphasize public accessibility, not technical release (FB-1.05)
- Multimodal milestone missing from the timeline (FB-1.06, must-fix)
- Overall narrative is choppy; needs smoother flow (FB-1.07)

**Revision action**: Reword opening paragraph framing, add brief
multimodal mention, smooth narrative arc.

---

## Theme 13: Background is solid — formatting only [CONSIDER]

**FB-IDs**: FB-1.13, FB-1.14, FB-2.01, FB-3.11, FB-3.12
**Sections**: Background
**Parts**: 1, 2, 3

All three sessions confirm Section 2 is tight, high signal-to-noise,
with a strong timeline. Content approved by both reviewers. Only needs
em-dash audit (Theme 7) and minor formatting.

**Revision action**: Em-dash audit only. No content changes. Keep the
Linux Foundation crescendo.

---

## Theme 14: Conclusion — keep strong ending [CONSIDER]

**FB-IDs**: FB-3.25, FB-3.26
**Sections**: Conclusion
**Parts**: 3

The final lines ("shape its trajectory / shaped by it" + "we choose
engagement") are approved and strong. "Proactive engagement, not
prohibition" is confirmed as accurate.

**Revision action**: Keep final sentences verbatim. Changes to the
conclusion come from Themes 1 (agent-first reframe) and 5 (workflow
narrative expansion).

---

## Approved sections (no changes needed beyond formatting)

- **"I'm Sorry, Dave"** (FB-3.16): Approved. Minor prose polishing only.
- **"I Know Kung Fu"** (FB-3.19): Approved. Keep as-is.
- **Citation numbering** (FB-3.06): Standard `acmart` alphabetical bibliography. No action.

---

## Open question

- **Page budget** (FB-1.15): Single-column vs. dual-column format — awaiting committee guidance.

---

## Revision priority by section

When revising in Phase 3, address themes in this order per section:

**Abstract** (00-abstract.md):
- Theme 1: "agent-first" reframe
- Theme 6: AI-authorship disclosure (punchy invitation)
- Theme 8: Rephrase "love letter/cautionary tale"
- Theme 7: Em-dash audit

**Introduction** (01-introduction.md):
- Theme 2: "Mostly Harmless" realignment + dog-fooding
- Theme 5: Add agentic workflow narrative paragraph
- Theme 12: Fix timeline framing, add multimodal, smooth flow
- Theme 8: Remove "from the trenches," soften "minimal human intervention"
- Theme 9: Merge short paragraphs
- Theme 1: "agent-first" reframe (second occurrence)
- Theme 7: Em-dash audit

**Background** (02-background.md):
- Theme 13: Em-dash audit only

**Approach** (03-approach.md):
- Theme 11: Update MCP status, tighten prose, compress spacing
- Theme 9: Consider subsection → paragraph formatting
- Theme 7: Em-dash audit

**Discussion** (04-discussion.md):
- Theme 3: Reframe "Tea, Earl Grey, Hot" + remove footnotes
- Theme 4: Reframe "Don't Cross the Streams"
- Theme 10: Tighten "The Answer is 42"
- Theme 7: Em-dash audit

**Conclusion** (05-conclusion.md):
- Theme 1: "agent-first" reframe (third occurrence)
- Theme 5: Expand workflow/harness/GitHub narrative
- Theme 14: Keep strong final lines
- Theme 7: Em-dash audit
