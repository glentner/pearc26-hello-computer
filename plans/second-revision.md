---
created: "2026-03-22"
status: "in-progress"
related_logs: []
---

# Second Revision: Phase 2 Review Distillation and Third Draft

## Problem Statement

The second draft (v0.5.0) has been integrated and a complete Phase 2 review transcript
exists (~1h 7m, Geoffrey solo). This transcript reviews the revised outline markdown
files — the ground-truth source documents — not the compiled PDF. Feedback is generally
positive ("way stronger than the first draft"), with fewer must-fix items and more
polish-level concerns. We need to distill this transcript, commit structured notes,
revise the outline sections, and produce a third integration.

## Current State

- **Second draft**: All 6 sections revised and integrated (v0.5.0, tag on `main`); `wip` is one commit ahead with Phase 5 housekeeping
- **Outline files**: All at `status: draft` after first revision cycle; these are now the ground-truth source for the manuscript
- **Phase 1 review artifacts**: Complete — `review-feedback-part[1-3].md` and `review-synthesis.md` in `outline/notes/`
- **Phase 2 transcript**: `~/Downloads/PEARC26 Paper Review_ Phase 2.vtt` (~4,150 lines VTT format, Geoffrey solo, reading from outline markdown files on GitHub)
- **Key gap**: Raw VTT transcript has not been converted to a readable review document or distilled into feedback items

## Resolved Questions

1. **FB-ID naming**: Using `FB-P2.NN` prefix for Phase 2 review feedback (avoids `FB-4.NN` which falsely implies a fourth part of the Phase 1 review).
2. **Section title parenthetical format**: `"I'm Sorry, Dave" (User Support)` — parenthetical after quote, no dash separator.
3. **"Not merely tolerated"**: Will workshop alternative phrasing during Phase 4 revision.
4. **Phase 3 review with Ashish**: Handled in a separate plan/cycle. Not included here.

## Remaining Open Question

- **Page budget**: Single-column vs. dual-column — still awaiting committee guidance. This may require aggressive compression if single-column is mandatory.

---

## Phase 1: Convert VTT Transcript to Review Document

Parse the VTT file into a clean markdown review document, matching the format of
`reviews/review_phase_1_part_3.md`. Output: `reviews/review_phase_2.md`.

- Speaker: Geoffrey R. Lentner (solo)
- Date: March 22, 2026
- Duration: ~1h 7m
- Preserve verbatim comments, correct transcription errors (e.g., "perk" → "PEARC",
  "Agentec" → "agentic", "Gauche" → "Gautschi", "cloud code" → "Claude Code",
  "Etsy agents D" → "`/etc/agents.d`", "deal omit at all" → "Deelman et al.",
  "Vaswamy" → "Vaswani")
- Organize by section headers matching the paper's structure
- Separate Geoffrey's paper readings from his commentary

### Tasks

- [x] 1.1: Convert VTT transcript → `reviews/review_phase_2.md`
- [x] 1.2: Commit — `WIP: Convert Phase 2 review transcript`

## Phase 2: Distill Review Feedback

Extract discrete feedback items from the converted review document into
`outline/notes/review-feedback-phase2.md`. Use `FB-P2.NN` IDs (P2 = Phase 2 review
cycle, avoids confusion with the Phase 1 three-part numbering `FB-1.NN` through
`FB-3.NN`).

### Key Findings (from planning research)

**Must-Fix:**
1. "The Answer is 42" — false "one session" claim (was ~15 sessions / 8 hours)
2. "Tea, Earl Grey, Hot" — closing sentences imply users get magic for free
3. "Token budgets" ambiguity (API billing vs. context window management)
4. Repeated tool enumeration (Warp, Cursor, Claude Code) — 3rd occurrence in 3.1
5. `sinteractive` is a bad example — agents should use `srun`/`sbatch`
6. Abstract "not merely tolerated" — awkward construction, workshop alternative

**Should-Fix:**
7. Section title parentheticals — add `"Title" (Descriptor)` format
8. Background "who will shape that integration?" — too combative
9. Background "AI capabilities" → "AI systems" in Genesis sentence
10. Background: consider quoting "stands at a crossroads"
11. "I Know Kung Fu" paragraphs could merge (vertical space)
12. Vertical space / page budget remains critical
13. "Don't Cross the Streams" — mention user confirmation as mitigation
14. Outline → LaTeX fidelity audit needed in integration phase

### Tasks

- [x] 2.1: Distill `reviews/review_phase_2.md` → `outline/notes/review-feedback-phase2.md`
- [x] 2.2: Commit — `WIP: Distill Phase 2 review feedback`

## Phase 3: Update Review Synthesis

Update `outline/notes/review-synthesis.md` with Phase 2 feedback. Most themes will
have status updates (e.g., "addressed in second draft, approved in Phase 2 review").
New items get added. The synthesis becomes the revision checklist for the third draft.

### Tasks

- [x] 3.1: Update `outline/notes/review-synthesis.md` with Phase 2 cross-references and new items
- [x] 3.2: Commit — `WIP: Update review synthesis with Phase 2 feedback`

## Phase 4: Revise Outline Sections (Third Draft)

With the updated synthesis, make targeted revisions. This round is much lighter than
Phase 1 — mostly polish and a few specific fixes.

Revision order follows the paper's flow:

1. `00-abstract.md` — workshop "not merely tolerated" alternative
2. `01-introduction.md` — no changes (approved as "great")
3. `02-background.md` — soften closing, word choice tweaks
4. `03-approach.md` — remove repeated tool list, fix `sinteractive`, reflow 3.2
5. `04-discussion.md` — fix "one session" claim, rebalance Tea/Earl Grey closings,
   clarify token budgets, merge I Know Kung Fu paragraphs, add user confirmation note
6. `05-conclusion.md` — no changes (approved as "super powerful")
7. All sections — add parenthetical labels using `"Title" (Descriptor)` format

### Tasks

- [x] 4.1: Revise `02-background.md` — tone down closing, word choice tweaks
- [x] 4.2: Revise `03-approach.md` — remove repeated tool list, fix `sinteractive`, reflow 3.2
- [x] 4.3: Revise `04-discussion.md` — fix "one session" claim, rebalance Tea/Earl Grey closings, clarify token budgets, merge I Know Kung Fu paragraphs, add user confirmation note
- [x] 4.4: Add parenthetical labels to all pop-culture section titles across outline files
- [x] 4.5: Commit — `WIP: Revise outline sections from Phase 2 review feedback`

## Phase 5: Third Integration

Once outline revisions are reviewed and approved, integrate revised prose into
`manuscript.tex` and rebuild. To avoid the failure modes from prior integrations
(dropped citations, heading mismatches, compounded errors), this phase uses two
stored prompts that split integration from auditing.

### Tasks

- [x] 5.1: **First pass** — delta-based LaTeX integration per `prompts/latex_integration_first_pass.md`
- [x] 5.2: **Second pass** — cold-read fidelity audit per `prompts/latex_integration_second_pass.md`
- [ ] 5.3: Verify `make build` succeeds
- [ ] 5.4: Check page budget — investigate single-column vs. dual-column submission format
- [ ] 5.5: Commit — `WIP: Third integration from revised outline`

## Phase 6: Housekeeping

- [ ] 6.1: Log session(s) to `logs/` per `rules/session_logs.md`
- [ ] 6.2: Push to `wip` branch

---

## Progress

**Completed**: 12/19

---

## Session Prompt Template

Use this prompt to continue the second revision phase. Each phase is one
session's unit of work. Complete all tasks within the current phase, then
**stop and ask for feedback** before advancing to the next phase.

```
Continue our PEARC'26 paper work on the second revision phase.

Execution procedure:

1. LOAD PLAN: Read `plans/second-revision.md`. For resolved design
   decisions and prior context, reference Warp plan
   eb657a5b-57b0-45aa-8858-74538183b4c2 and the first revision plan
   `plans/first-revision.md`.

2. IDENTIFY CURRENT PHASE: Scan task checkboxes. The current phase
   is the lowest-numbered phase with any unchecked `[ ]` items.

3. LOAD PHASE INPUTS:
   Phase 1 → read `~/Downloads/PEARC26 Paper Review_ Phase 2.vtt`
             + `reviews/review_phase_1_part_3.md` (format reference)
   Phase 2 → read `reviews/review_phase_2.md`
   Phase 3 → read `outline/notes/review-feedback-phase2.md`
             + `outline/notes/review-synthesis.md`
   Phase 4 → read updated `outline/notes/review-synthesis.md`
             + target `outline/0N-*.md` section file(s)
   Phase 5 → read revised `outline/0N-*.md` files + `manuscript.tex`
   Phase 6 → finalize logs and push

4. TASK LOOP (within current phase only):
   a. Find the next unchecked `[ ]` task in the current phase.
   b. Execute the task.
   c. Mark it `[x]` in `plans/second-revision.md`.
   d. Commit: `WIP: <description>` with
      `Co-Authored-By: Oz <oz-agent@warp.dev>`
      Include FB-IDs in commit messages where applicable.
   e. If unchecked tasks remain in this phase, go to (a).
   f. If all tasks in this phase are complete, go to step 5.

5. PHASE BOUNDARY: All tasks in the current phase are done.
   Log the session to `logs/` per `rules/session_logs.md`.
   Push to `wip` branch.
   **STOP. Report what was completed and ask for feedback.**
   Do NOT begin the next phase until explicitly told to continue.
```
