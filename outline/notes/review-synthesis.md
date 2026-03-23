---
sources:
  - outline/notes/review-feedback-part1.md
  - outline/notes/review-feedback-part2.md
  - outline/notes/review-feedback-part3.md
  - outline/notes/review-feedback-phase2.md
total_items: 78
phase4_status: complete
---

# Review Synthesis: Cross-Cutting Themes

This document groups all feedback from Phase 1 (three-part review with
Geoffrey and Ashish) and Phase 2 (Geoffrey's solo review of the second
draft outline files) into actionable themes. Each theme lists the FB-IDs
it consolidates, the sections affected, and the revision action.

Phase 2 reviewed the second draft (v0.5.0) from the outline markdown
files. Most Phase 1 themes were addressed; Phase 2 confirmed those fixes
and raised new items. Status tags below indicate what remains for the
third draft.

---

## Theme 1: "Agentic assistance" → "agent-first workflow" [RESOLVED]

**FB-IDs**: FB-1.12, FB-2.02, FB-2.04, FB-3.01, FB-3.08, FB-3.23
**Sections**: Abstract, Introduction, Conclusion (3 occurrences)
**Parts**: 1, 2, 3 (raised in every session)

The phrase "agentic assistance" appeared three times and fundamentally
misrepresented the paper's process. The workflow was agent-first — not
AI proofreading or one-shot generation.

**Phase 2 status**: ✅ Addressed in second draft. All three occurrences
replaced. Phase 2 approved the abstract as "way stronger," the
introduction as "great," and the conclusion as "super powerful." No
further action needed.

---

## Theme 2: "Mostly Harmless" argument misalignment [RESOLVED]

**FB-IDs**: FB-1.10, FB-1.11, FB-2.10, FB-3.09, FB-3.10
**Sections**: Introduction ("Mostly Harmless" subsection)
**Parts**: 1, 3

The first draft used a fatalism argument ("resistance is futile"). The
correct framing is cautious optimism — the tools are mostly safe, and
frontier AI follows policy more reliably than unsupervised users.

**Phase 2 status**: ✅ Addressed in second draft. The introduction was
reframed around cautious optimism with dog-fooding angle, policy
compliance, and softened closing. Phase 2 approved: "I think this
introduction is great." No further action needed.

---

## Theme 3: "Tea, Earl Grey, Hot" — closing imbalance [RESOLVED]

**FB-IDs**: FB-3.17, FB-3.18, **FB-P2.15**, **FB-P2.16**
**Sections**: Discussion ("Tea, Earl Grey, Hot" subsection)
**Parts**: 3, P2

Phase 1 issue (false amateur-discovery framing, misleading footnotes)
was addressed in the second draft — reframed around prior experience,
footnotes removed. Phase 2 approved the reframe ("way better than the
first draft") but identified two new problems:

1. **Closing sentences imply users get magic for free** (FB-P2.15):
   "precision must be engineered into the system, not left to the user"
   and "every user benefits without crafting expert prompts themselves"
   both suggest that system-wide configuration eliminates the need for
   user effort. The correct framing is partnership/scaffolding — we
   provide the foundation, users still bring domain specificity.

2. **"Token budgets" is ambiguous** (FB-P2.16): Could be misconstrued
   as API billing rather than context window management (the 200K-token
   window, staying in the 30–60% sweet spot). Needs clarification.

**Phase 4 status**: ✅ Addressed in third draft. Closing rebalanced to
partnership framing: "System-wide configurations provide the foundation,
but users still bring the domain specificity." "Token budgets" replaced
with "context window capacity." No further action needed.

---

## Theme 4: "Don't Cross the Streams" — add user confirmation [RESOLVED]

**FB-IDs**: FB-3.21, FB-3.22, **FB-P2.21**, FB-P2.22
**Sections**: Discussion ("Don't Cross the Streams" subsection)
**Parts**: 3, P2

Phase 1 issue (framing agents as novel danger) was addressed in the
second draft — reframed around accelerating existing risk patterns with
HPC confinement mechanisms. Phase 2 approved: "big improvement, no
major criticisms."

**Phase 2 addition** (FB-P2.21): Briefly mention that most agentic
tools support user confirmation for destructive actions as an
out-of-the-box mitigation. Keep it light — acknowledge both the safety
benefit and the "consenting adults" principle. Don't over-prescribe.

**Phase 4 status**: ✅ Addressed in third draft. Added: "Most agentic
tools also support user confirmation for destructive actions out of
the box, providing an additional safety net." Light touch as requested.
No further action needed.

---

## Theme 5: Missing agentic workflow narrative [RESOLVED]

**FB-IDs**: FB-2.05, FB-3.24, FB-3.02
**Sections**: Introduction or early Approach + Conclusion
**Parts**: 2, 3

The paper's unique contribution — the actual agent-first workflow
process — was underrepresented in the first draft.

**Phase 2 status**: ✅ Addressed in second draft. The conclusion now
contains a concrete workflow description ("No prose was written by
hand... rules, curated references, reviewed transcripts, and guided
iterative revision... over 60 commits, session logs, planning
documents"). Phase 2 approved: "marked improvement from just saying
'agent-assisted.'" No further action needed.

---

## Theme 6: AI-authorship disclosure strategy [RESOLVED]

**FB-IDs**: FB-2.02, FB-2.03, FB-2.06
**Sections**: Abstract, Conclusion, Acknowledgments
**Parts**: 2

**Resolved in first revision cycle**: Punchy, enticing statement in
the abstract. Detailed workflow narrative in conclusion. ACM policy
compliance in acknowledgments. Addressed through Themes 1 and 5.

**Phase 2 status**: ✅ Confirmed. No further action.

---

## Theme 7: Em-dash overuse [RESOLVED]

**FB-IDs**: FB-1.02, FB-3.04, FB-3.12, FB-3.27
**Sections**: All (flagged in abstract, intro, background, conclusion)
**Parts**: 1, 3

Em dashes appeared in nearly every paragraph. Paper-wide audit was
performed during second draft revisions.

**Phase 2 status**: ✅ Phase 2 did not flag any new em-dash issues.
Audit appears successful. Continue monitoring during third draft
revisions but no dedicated pass needed.

---

## Theme 8: Overly flowery / clever language [RESOLVED]

**FB-IDs**: FB-1.01, FB-1.03, FB-1.04, FB-1.08, FB-3.03, FB-3.05
**Sections**: Abstract, Introduction
**Parts**: 1, 3

"Love letter and cautionary tale," "from the trenches," "minimal human
intervention" — all trimmed or replaced in the second draft.

**Phase 2 status**: ✅ Phase 2 approved all sections where these
appeared. No further action needed.

---

## Theme 9: Paragraph structure / vertical space [PARTIALLY RESOLVED]

**FB-IDs**: FB-1.09, FB-3.07, FB-3.13, FB-3.15, **FB-P2.18**, **FB-P2.24**
**Sections**: Introduction, Approach, Discussion
**Parts**: 1, 3, P2

Phase 1 issues (short paragraphs, subsection headers eating space)
were partially addressed in the second draft.

**Phase 2 additions**:
- FB-P2.18: "I Know Kung Fu" two paragraphs should merge into one
- FB-P2.24: Page budget remains critical (4-page limit, currently 5
  pages with references)

**Phase 4 status**: ✅ "I Know Kung Fu" paragraphs merged into one
(FB-P2.18). Vertical space economized throughout Phase 4 revisions.

**Remaining (Phase 5)**: Page budget investigation (FB-P2.24) —
single-column vs. dual-column format still awaiting committee guidance.
Will be assessed during Phase 5 integration (task 5.4).

---

## Theme 10: "The Answer is 42" — false claim [RESOLVED]

**FB-IDs**: FB-3.20, **FB-P2.20**
**Sections**: Discussion ("The Answer is 42" subsection)
**Parts**: 3, P2

Phase 1 flagged this paragraph as flabby. Phase 2 escalated: the
claim that the annotated bibliography was built "in one session" is
**factually false**.

The bibliography was built over ~15 sessions (1 planning + 13
individual references + 1 wrap-up), totaling ~8 hours. Each reference
consumed an entire 200K-token context window in a deliberate agentic
loop with fresh sessions (`/new`) and continuation prompts.

**Phase 4 status**: ✅ Addressed in third draft. Replaced with accurate
characterization: "fifteen context windows over eight hours of deliberate
prompting." Prose tightened. Positive/negative contrast preserved.
No further action needed.

---

## Theme 11: Approach section updates [RESOLVED]

**FB-IDs**: FB-2.07, FB-2.08, FB-2.09, FB-3.14, FB-3.15, **FB-P2.09**, **FB-P2.10**, **FB-P2.12**
**Sections**: Approach (all subsections)
**Parts**: 2, 3, P2

Phase 1 items (MCP status, word choice, `/etc/agents.d`, compress 3.2)
were partially addressed. Phase 2 found remaining issues:

- **FB-P2.09**: "Warp, Cursor, Claude Code" repeated a third time in
  Section 3.1. Remove — use generic "modern agentic tools" since the
  specific trio is already in the introduction and listing specific
  tools dates quickly (Gemini CLI, JetBrains Junie, etc. now exist).
- **FB-P2.10**: `sinteractive` is a bad example for agents — agents
  should use `srun`/`sbatch`, not interactive sessions. Replace with
  batch job best practices. `myquota` is fine to keep.
- **FB-P2.12**: Section 3.2 first paragraph could reflow to introduce
  RCAC-MCP and Globus-MCP more cleanly as a pair.

**Phase 4 status**: ✅ All addressed in third draft. Tool enumeration
removed from 3.1 (now "Modern agentic tools"). `sinteractive` replaced
with `sbatch`. 3.2 reflows RCAC-MCP and Globus-MCP as a clean pair.
Closing sentence preserved verbatim per FB-P2.11. No further action needed.

---

## Theme 12: Introduction flow and content [RESOLVED]

**FB-IDs**: FB-1.05, FB-1.06, FB-1.07
**Sections**: Introduction (opening paragraphs)
**Parts**: 1

First draft had choppy narrative, missing multimodal milestone, and
misframed inflection point.

**Phase 2 status**: ✅ Addressed in second draft. Phase 2 approved
the opener as "solid" and the full introduction as "great." No further
action needed.

---

## Theme 13: Background — new content tweaks [RESOLVED]

**FB-IDs**: FB-1.13, FB-1.14, FB-2.01, FB-3.11, FB-3.12, **FB-P2.05**, **FB-P2.06**, **FB-P2.07**, FB-P2.08
**Sections**: Background
**Parts**: 1, 2, 3, P2

All four review sessions confirm the opening three paragraphs are
tight and strong. Phase 2 approved them as "very straightforward,
matter-of-fact" and "really good" (FB-P2.08).

However, Phase 2 identified three issues in the **closing paragraph**:

1. **"Who will shape that integration?"** — too combative (FB-P2.05).
   Reads as "get on the train or get left behind" rather than the
   welcoming "ready player two" invitation tone. Soften to align with
   the conclusion's open-hand posture.
2. **"AI capabilities" → "AI systems"** in the Genesis sentence
   (FB-P2.06). Minor word choice improvement.
3. **Quote "stands at a crossroads"** (FB-P2.07). Add quotation marks
   to attribute the phrase more clearly to Deelman et al.

**Phase 4 status**: ✅ All addressed in third draft. Closing softened to
"how centers choose to engage will define the experience for researchers
and facilitators alike." "AI systems" in Genesis sentence. "stands at a
crossroads" properly quoted. First three paragraphs unchanged as
approved. No further action needed.

---

## Theme 14: Conclusion — keep strong ending [RESOLVED]

**FB-IDs**: FB-3.25, FB-3.26, **FB-P2.23**
**Sections**: Conclusion
**Parts**: 3, P2

The final lines ("shape its trajectory / shaped by it" + "we choose
engagement") are approved across both review phases. "Proactive
engagement, not prohibition" confirmed as accurate.

**Phase 2 status**: ✅ Confirmed again — "super powerful" and "if this
is where we left it, I would be OK with that." No changes to
conclusion. Fully resolved.

---

## Theme 15: Abstract "not merely tolerated" [RESOLVED]

**FB-IDs**: **FB-P2.01**
**Sections**: Abstract
**Parts**: P2

New Phase 2 item. The sentence "Researchers want these tools integrated
into their workflows, not merely tolerated" is clumsy. Geoffrey
stumbles over the punctuation and the negation. The intent is correct
(users want real integration, not grudging tolerance) but the
construction needs workshopping.

**Phase 4 status**: ✅ Addressed in third draft. Replaced with
"researchers expect these tools to be supported, not just permitted."
Cleaner construction, same intent. No further action needed.

---

## Theme 16: Section title parentheticals [RESOLVED]

**FB-IDs**: **FB-P2.03**
**Sections**: All pop-culture section headings (Discussion subsections)
**Parts**: P2

New Phase 2 item. Add parenthetical descriptors after each pop-culture
pun to anchor the reader:
- "I'm Sorry, Dave" (User Support)
- "Tea, Earl Grey, Hot" (Context Engineering)
- "I Know Kung Fu" (User Expectations)
- "The Answer is 42" (AI Outcomes)
- "Don't Cross the Streams" (Cautionary Notes)

**Phase 4 status**: ✅ All five Discussion subsection titles updated
with parenthetical descriptors in the outline files. Introduction and
conclusion titles left as-is (optional per original feedback).
No further action needed.

---

## Theme 17: LaTeX fidelity audit [MUST-FIX] (NEW)

**FB-IDs**: **FB-P2.00**, **FB-P2.25**
**Sections**: All (process concern, not content)
**Parts**: P2

New Phase 2 item. Geoffrey has "deep anxiety" about discrepancies
between outline markdown files and the compiled LaTeX. Citations exist
in LaTeX but not in markdown. The integration process (having an AI
agent pull prose into `.tex`) is imprecise and needs a systematic
audit.

**Revision action**: During Phase 5 (third integration), conduct a
section-by-section comparison of each outline file against the
corresponding LaTeX section. Verify: prose fidelity, citation presence
in both formats, figure references, no dropped or added content.

---

## Approved sections (no changes needed beyond specific items above)

- **"I'm Sorry, Dave"** (FB-3.16, FB-P2.14): Approved in both phases. No changes.
- **"I Know Kung Fu"** (FB-3.19, FB-P2.19): Content approved in both phases. Merge paragraphs only (Theme 9).
- **Introduction** (FB-P2.04): Approved in Phase 2 — "great." No content changes.
- **Section 3.3 Documentation** (FB-P2.13): Approved — "short and concise enough."
- **Citation numbering** (FB-3.06): Standard `acmart` alphabetical bibliography. No action.

---

## Open question

- **Page budget** (FB-1.15, FB-P2.24): Single-column vs. dual-column format — awaiting committee guidance. Currently 5 pages with references against a 4-page limit.

---

## Revision priority by section (Third Draft)

✅ **All Phase 4 revisions complete.** Summary of changes per section:

**Abstract** (00-abstract.md):
- ~~Theme 15: Workshop "not merely tolerated" alternative~~ → ✅ Replaced with "supported, not just permitted"

**Introduction** (01-introduction.md):
- No changes needed — approved as "great" in Phase 2 ✅

**Background** (02-background.md):
- ~~Theme 13: Soften closing, word choice, quote attribution~~ → ✅ All three items addressed

**Approach** (03-approach.md):
- ~~Theme 11: Remove tool list, replace sinteractive, reflow 3.2~~ → ✅ All three items addressed

**Discussion** (04-discussion.md):
- ~~Theme 3: Rebalance Tea/Earl Grey closings, clarify token budgets~~ → ✅ Partnership framing, "context window capacity"
- ~~Theme 10: Fix false "one session" claim~~ → ✅ "fifteen context windows over eight hours"
- ~~Theme 9: Merge "I Know Kung Fu" paragraphs~~ → ✅ Merged into single paragraph
- ~~Theme 4: Add user confirmation mention~~ → ✅ Added
- ~~Theme 16: Add parenthetical labels~~ → ✅ All five subsections labeled

**Conclusion** (05-conclusion.md):
- No changes needed — approved as "super powerful" in Phase 2 ✅

**Remaining for Phase 5**:
- Theme 9 (partial): Page budget investigation — single-column vs. dual-column (FB-P2.24)
- Theme 17: LaTeX fidelity audit during integration (FB-P2.25)
