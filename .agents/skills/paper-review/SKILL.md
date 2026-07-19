---
name: paper-review
description: >-
  Ingest EXTERNAL peer feedback and route it back into the paper pipeline — the in-review phase of
  the factory. Takes a raw human review (call transcript/VTT, email, committee notes) plus a phase
  number N and turns it into the tracked feedback spine: CAPTURE the review verbatim into
  reviews/review_phase_N.md, DISTILL each point into outline/notes/review-feedback-<part>.md as an
  [FB-N.NN] item (Type / Severity must-fix|should-fix|consider / verbatim Quote / Action, mapped to a
  section id and any C-ID), SYNTHESIZE cross-cutting themes into outline/notes/review-synthesis.md,
  then DRIVE the paper back to revising — write plans/N-revision.md, bump the review cycle, set the
  verdict, and reopen the affected sections. Re-runnable once per external review cycle. The slot
  hs-publish occupied, reinterpreted for a human-paced, cyclic research loop (see
  .agents/factory/methodology.md and .agents/factory/review-rubric.md).
disable-model-invocation: true
argument-hint: "<path/to/raw-review> <phase N> [part <label>] [status]"
allowed-tools: Read, Write, Edit, Grep, Glob, AskUserQuestion, Bash(git status *), Bash(git branch *), Bash(git add *), Bash(git commit *), Bash(git log *), Bash(git rev-parse *), Bash(git diff *), Bash(python3 .agents/factory/bin/*), Bash(date -u *)
---

# paper-review — distill external feedback, loop the paper back to revising

## When to Use

Invoke `/paper-review` when a real human review lands: a Zoom/VTT transcript of a co-author read,
an emailed critique, PC/committee notes, or a shepherd's comments. This is the **external**
verification phase — distinct from `/paper-draft` pass B, which is the *internal* blind audit. This
skill does not judge the prose itself; it turns someone else's judgment into the tracked spine
(`reviews/` → `[FB-N.NN]` → `review-synthesis.md` → `plans/N-revision.md` → reopened sections) and
advances the FSM to `revising` so `/paper-outline` and `/paper-draft` can act on it.

Run it **once per external review cycle** (`review.cycle` bumps each time). It is re-runnable: phase 1
was the three-part Geoffrey+Ashish read; phase 2 was the solo re-read; a phase 3 committee review
would be the next invocation. It never rewrites prose and never ships — it captures, distills, and
routes, then STOPS for the human to work the revision plan.

## References

Read before distilling; stay consistent with them:

- [`../../factory/review-rubric.md`](../../factory/review-rubric.md) — the refutation protocol and the
  shared **severity vocabulary** (`must-fix` / `should-fix` / `consider`). The `/paper-review`
  distillation contract is spelled out there.
- [`../../factory/invariants.md`](../../factory/invariants.md) — map each feedback item to the
  invariant it touches (venue/format, LaTeX prose, citation integrity, fidelity).
- [`../../factory/methodology.md`](../../factory/methodology.md) — where this phase sits in the cyclic
  lifecycle and why `revising` re-enters `outlining`/`integrating`.
- [`../../factory/claims.md`](../../factory/claims.md) — the C-IDs a feedback item may implicate.
- Templates: `../../factory/templates/REVIEW-FEEDBACK.md`, `../../factory/templates/REVIEW-SYNTHESIS.md`,
  `../../factory/templates/REVISION-PLAN.md` (and `CONTRACT.md` for the `PAPER.md` shape).
- Worked examples in this repo — match their shape exactly: `outline/notes/review-feedback-part1.md`,
  `outline/notes/review-synthesis.md`, `reviews/review_phase_1_part_1.md`, `plans/first-revision.md`.
- **Portability:** [`portability.md`](../../factory/portability.md) — this skill runs on any harness; if the *Current state* commands aren't auto-injected, run them yourself in Step 1, and if `AskUserQuestion` is unavailable, ask in plain text and STOP.

## User Instructions

Additional instructions provided with the invocation: $ARGUMENTS

## Current state (injected at load)

- Branch: !`git branch --show-current`
- Tree: !`git status --porcelain | head -n 20`
- Existing captures: !`ls reviews/ 2>/dev/null`
- Existing feedback notes: !`ls outline/notes/review-feedback-*.md 2>/dev/null`
- Paper status: !`python3 .agents/factory/bin/paper_status.py 2>&1 | head -c 1400`

## Argument Parsing

Parse `$ARGUMENTS` case-insensitively. If it is self-contradictory or a required piece is missing,
STOP and ask (AskUserQuestion) rather than guess.

- A filesystem path (the raw review: `.md`, `.txt`, `.vtt`, `.eml`, …) → the **raw review source**.
  Required. If absent, STOP and ask for the path (do not fabricate a review).
- `phase N` / a bare integer `N` → the **phase number**. Required — it names the capture file
  (`reviews/review_phase_N.md`) and prefixes every feedback id (`FB-N.NN`). If absent, infer the next
  cycle from `paper_status.py`'s `review.cycle`, then **confirm it** before writing.
- `part <label>` → the feedback-note suffix when a phase arrives in multiple sessions
  (`review-feedback-<label>.md`, e.g. `part1`, `phase2`); default `part1` for a phase's first review,
  or the next free `partM` if earlier parts of this phase already exist.
- `status` → report the current `review` block (`cycle`, `verdict`), the existing captures and
  feedback notes, and the open `must-fix` count from `paper_status.py`; **do no work**.

## Safety Principles

- **Run `paper_status.py` first; mutate only via `set_status.py`.** Never hand-edit `PAPER.md`
  frontmatter or a section file's `status:` — `set_status.py` owns the serialization and keeps the
  outline files in sync (methodology principle 2).
- **Capture is verbatim.** `reviews/review_phase_N.md` preserves the reviewer's words. Fix **only**
  transcription errors (mis-heard words, ASR garble, timestamps), and note every such fix inline
  (e.g. `[transcription: "sbatch" not "s batch"]`). Do not summarize, reorder, or soften in the
  capture — the synthesis is where interpretation happens.
- **Distill honestly, refute before recording.** Follow the rubric's refutation protocol: quote the
  exact reviewer sentence and locate the exact section/claim it hits. Assign severity from the shared
  vocabulary; do not inflate a `consider` to `must-fix` to look thorough, and do not manufacture
  action items the reviewer did not raise. A reviewer who approves a section is a valid, recorded
  result (`consider` / no-change), not a prompt to invent gaps.
- **Never guess.** When a point is ambiguous ("who does this map to?", "is this a must-fix?"), emit a
  literal `[NEEDS CLARIFICATION: …]` in the feedback item and ask the human. An unresolved marker is
  fine to record but should be surfaced, not silently resolved.
- **One review per invocation.** Bump the cycle once. Do not re-distill an already-captured review; if
  `reviews/review_phase_N.md` exists and differs, STOP and ask (append a new `part`, or overwrite only
  on explicit confirmation).
- **This skill writes notes and reopens sections — it does not edit prose or `manuscript.tex`.** The
  actual rewrites are `/paper-outline`'s and `/paper-draft`'s job.
- **Session logging is mandatory** (`rules/session_logs.md`): this orchestrator writes
  `logs/<UTC-ISO>-<slug>.md` at the end, from the live conversation, with the VERBATIM user input in
  the frontmatter. Use `/bin/rm` (never the Warp-era `del` alias) for any file deletion
  (`rules/file_deletion.md`).
- **Bounded loop.** `paper_status.py` warns when `review.cycle` exceeds ~2–3. A paper's external loop
  is human-paced, but flag the human if cycles are climbing without convergence.

## Procedure

### Step 1 — Pre-flight and enter `in-review`
1. Confirm on `draft` (the working branch); a dirty tree with unrelated changes → STOP and ask. The raw
   review file being adopted may be untracked; that is expected.
2. Run `python3 .agents/factory/bin/paper_status.py` and read the current `macro_phase`, `review`
   block, section statuses, and `feedback_by_severity`. Resolve `N` and the `part` label (Argument
   Parsing); confirm the phase number with the human if it was inferred.
3. Move the paper into the review phase (idempotent):
   `python3 .agents/factory/bin/set_status.py PAPER.md --macro-phase in-review --touch`.
   If it is already `in-review` (or a later cyclic phase), just note it — do not fight the FSM.

### Step 2 — CAPTURE (verbatim)
Read the raw review. Write `reviews/review_phase_N.md` (for a multi-session phase, `review_phase_N.md`
holds the whole phase, or use `review_phase_N_part_M.md` matching the existing repo naming). Preserve
the reviewer's words; fix only transcription errors and annotate each fix inline. Add a short YAML
header (`source:`, `reviewed_by:`, `date:`) mirroring the existing captures. This file is the
public-record ground truth the distillation traces back to.

### Step 3 — DISTILL into `[FB-N.NN]` items
Create `outline/notes/review-feedback-<part>.md` from `../../factory/templates/REVIEW-FEEDBACK.md`,
matching `outline/notes/review-feedback-part1.md` exactly. Group items by section (`## Section:
<name>`). For each discrete point emit one item:

```
### [FB-N.NN] <short title>
- **Type**: <content | structure | framing | tone | word-choice | meta | citation | format>
- **Severity**: must-fix | should-fix | consider
- **Quote/context**: "<verbatim reviewer words>"
- **Action**: <concrete, single revision instruction>
```

Number sequentially within the phase (`FB-N.01`, `FB-N.02`, …). Map each item to a **section id**
(`00-abstract` … `06-acks`) and, when it touches a headline claim, the **C-ID** (per `claims.md`).
Assign severity from the rubric: factual errors, unsupported claims, dangling/incorrect citations,
page/ACM-policy violations, and fidelity breaks are `must-fix`; real weaknesses are `should-fix`;
optional polish and judgment calls are `consider`. Where a point touches an invariant
(`invariants.md`), name it (e.g. em-dash overuse → §2). Add the same YAML header as the example
(`source:`, `reviewed_by:`, `date:`).

### Step 4 — SYNTHESIZE cross-cutting themes
Update (or create) `outline/notes/review-synthesis.md` from
`../../factory/templates/REVIEW-SYNTHESIS.md`, matching the existing file. Group `FB-N.NN` items that
recur across sections/phases into numbered **themes**, each listing its FB-IDs, the sections affected,
a resolution status tag (`[MUST-FIX]` / `[RESOLVED]` / `[PARTIALLY RESOLVED]`), and the consolidated
revision action. Fold this phase's new items into existing themes where they belong; open a new theme
only for genuinely new cross-cutting concerns. End with a **revision priority by section** ordering
(most-blocking first) that `/paper-outline` will follow, plus any **open questions** (e.g. page-budget
format) carried forward.

### Step 5 — DRIVE the paper back to `revising`
1. Write `plans/N-revision.md` from `../../factory/templates/REVISION-PLAN.md` (see
   `plans/first-revision.md` for shape): problem statement, current state, resolved/open questions,
   and phased tasks — distill → revise outline → re-integrate — with the section-priority order from
   Step 4 and explicit `must-fix` gates. Reference the `FB-N.NN` ids and section ids so the trace
   holds.
2. Advance the FSM and reopen affected sections with `set_status.py`:
   ```
   python3 .agents/factory/bin/set_status.py PAPER.md --macro-phase revising --bump-cycle --verdict changes-requested --touch
   python3 .agents/factory/bin/set_status.py PAPER.md --section <id> --status review   # per section a should-fix touches
   python3 .agents/factory/bin/set_status.py PAPER.md --section <id> --status draft    # per section needing substantive rework
   ```
   Reopen a section to `review` for targeted edits, or to `draft` when the feedback demands substantive
   rewriting. Sections the reviewer approved stay `integrated`. Run `paper_status.py` again to confirm
   the new `review.cycle`, `verdict`, and reopened sections.
   If a reviewer asks for a **new section** (e.g. "add a Limitations section") or a **new contribution
   claim**, create it through the CLI — NEVER hand-edit `PAPER.md` frontmatter: `set_status.py PAPER.md
   --add-section <id> --status draft --target-words N --order N` (then create `outline/<id>.md`), or
   `set_status.py PAPER.md --add-claim <Cn> --satisfied-by <section-ids>`.
   Note: reopening a section makes any prior pass-B audit **STALE**, so the next `/paper-draft` run
   re-audits it from scratch; the `reviewed_commit` gate (in `/paper-release`) will correctly show the
   manuscript changed since the last audit.

### Step 6 — Meta-note (silence by default)
Before committing, ask ONE question: *did the skill itself (not you, not the task) cost something this
run?* Almost always the answer is no — **silence is the default; most runs add nothing.** If yes AND it
clears the bar in `.agents/factory/templates/META.md`, append a `## F<n>` finding to the **repo-root
`META.md`** (create it from `.agents/factory/templates/META.md` if absent): a metadata line
`origin=paper-review:<step> severity=<high|medium|low> category=<instruction|steering|tooling|template|missing-guidance> status=open target=<best-guess file>`
plus the **What happened / Skill cause / Recommended fix / Confidence · Effort** bullets. Keep it to ≤3
findings; if an equivalent finding exists, append "· seen again" to its title rather than duplicating. A
content/task issue is NOT a finding — it belongs in `PAPER.md` **Clarifications**, a `reviews/` note,
or a `[NEEDS CLARIFICATION]` marker. Add `META.md` to that step's `git add`. You only *record*;
the human-gated `/paper-harness` is what later applies these.

### Step 7 — Commit + session log
1. Stage the artifacts and commit on `draft` with the `DRAFT:` prefix and the configured co-author trailer:
   ```
   git add reviews/review_phase_N.md outline/notes/review-feedback-<part>.md outline/notes/review-synthesis.md plans/N-revision.md PAPER.md outline/ META.md
   git commit -m "DRAFT: Distill phase N review; reopen sections for revision" -m "Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
   ```
   (`set_status.py` also rewrites the reopened outline files' `status:`, so stage `outline/`; stage
   `META.md` only if Step 6 wrote a finding.) Do not push; `/paper-release` ships to `main`.
2. Write the mandatory session log to `logs/<UTC-ISO>-<slug>.md` (timestamp via
   `date -u +"%Y-%m-%dT%H-%M-%S"`), capturing the VERBATIM user input in the frontmatter and
   summarizing the capture/distill/synthesize/drive actions from the live conversation.

### Step 8 — Report and hand off
Report: the phase number and new `review.cycle`; the capture path; the count of `[FB-N.NN]` items by
severity, **leading with the `must-fix` count**; the themes touched; the sections reopened (and to
which status); and any `[NEEDS CLARIFICATION]` markers or open questions (e.g. page budget). Tell the
human the gate: review `plans/N-revision.md`, then run **`/paper-outline`** per reopened section to
fold the fixes into the `## Draft` prose, then **`/paper-draft`** to re-integrate into
`manuscript.tex`. Stop.

## Examples

- `/paper-review reviews/incoming/pc-transcript.vtt phase 3` — capture the committee call into
  `reviews/review_phase_3.md`, distill to `outline/notes/review-feedback-part1.md` as `FB-3.NN`,
  synthesize, write `plans/3-revision.md`, bump to cycle 3 / `changes-requested`, reopen sections.
- `/paper-review ~/mail/shepherd-notes.eml phase 3 part phase3b` — a second session of phase 3;
  distill into `outline/notes/review-feedback-phase3b.md`, fold into the existing synthesis.
- `/paper-review status` — show current `review.cycle`, `verdict`, existing captures, and the open
  `must-fix` count; make no changes.

## Notes

- **Capture vs. distill vs. synthesize are three files by design.** The capture is verbatim evidence,
  the feedback note is the atomized `FB-N.NN` items, the synthesis is the cross-cutting interpretation.
  Keeping them separate is what makes the trace auditable (methodology, traceability chain).
- **This is the external counterpart to `/paper-draft` pass B**, sharing the rubric's severity scale
  and refutation protocol but *not* its blindness — an external reviewer is the ground truth, so you
  record their judgment rather than manufacture your own.
- **`revising` re-enters the outline/integrate loop.** After this skill runs, the paper is not
  "in review" any more — it is being revised; the next external `/paper-review` bumps the cycle again.
- Some `git`/`set_status.py` calls may prompt for permission depending on `settings.local.json`; that
  is expected and safe. `check_paper.py` (`make check`) and the human gate still guard `/paper-release`.
