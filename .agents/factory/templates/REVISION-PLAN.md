---
created: "{YYYY-MM-DD}"
status: "in-progress"
related_logs: []
---

# {Nth} Revision: Review Cycle {cycle} Distillation and Draft {draft-n}

> **This is the revision driver** for one `/paper-review` cycle — the `plans/N-revision.md`
> file that steers the outline→draft loop until `macro_phase` returns from `revising` to
> `in-review`. It is written by `/paper-review` after it distills a human review, and it is
> **checked off task-by-task** across sessions. It obeys `rules/planning_docs.md`: forward-looking,
> paired with backward-looking `logs/` (link them in `related_logs`). Replace every `{placeholder}`.

## Context

Review cycle **{cycle}** ({reviewer(s)}, {date}, {duration/medium}) has been captured verbatim
in `reviews/review_phase_{cycle}.md` and distilled into `outline/notes/review-feedback-{cycle-tag}.md`
(one `[FB-{cycle}.NN]` per point, per `.agents/factory/review-rubric.md`). Cross-cutting themes and
the section-priority order live in `outline/notes/review-synthesis.md` — **that synthesis is the
authoritative checklist; this plan schedules its execution.**

- **Current draft:** {vX.Y.Z}, all target sections `integrated` on `main`; `draft` is where this
  revision happens (commits `DRAFT: …`).
- **FSM state at plan creation:** `macro_phase: revising`, `review.cycle: {cycle}`,
  `review.verdict: changes-requested`; affected sections reopened to `status: draft` via
  `set_status.py`. Confirm with `python3 .agents/factory/bin/paper_status.py`.
- **Overall tenor:** {e.g. "positive — fewer must-fix items than the prior cycle, mostly polish"}.

## Goals

- Address every **must-fix** `[FB-{cycle}.NN]` item; address **should-fix** items as page budget allows.
- Keep changes traceable: each commit names the FB-IDs it resolves; each resolved item is marked
  **Done** in the mapping table below.
- Produce draft **{draft-n}**: revised `outline/0N-*.md` `## Draft` blocks re-integrated into
  `manuscript.tex`, `make check` clean, page budget honored.
- Return the FSM to `in-review` (or `released` via `/paper-release`) with no open must-fix items.
- **Non-goal:** re-scoping the paper or re-opening C-IDs — this is revision within the existing
  contract, not a new `/paper-start` cycle.

## Feedback → action mapping

Distilled from `outline/notes/review-feedback-{cycle-tag}.md` and `review-synthesis.md`. One row per
`[FB-{cycle}.NN]`; severity per the rubric (`must-fix` \| `should-fix` \| `consider`). Mark **Done**
`[x]` when the outline edit lands and is reflected in the mapping.

| FB-ID | Section | Severity | Action | Done |
|-------|---------|----------|--------|------|
| FB-{cycle}.01 | {0N-name} | must-fix | {concrete edit, e.g. "correct the 'one session' claim"} | [ ] |
| FB-{cycle}.02 | {0N-name} | must-fix | {concrete edit} | [ ] |
| FB-{cycle}.03 | {0N-name} | should-fix | {concrete edit} | [ ] |
| FB-{cycle}.04 | {0N-name} | should-fix | {concrete edit} | [ ] |
| FB-{cycle}.05 | {all} | consider | {optional polish / human judgment call} | [ ] |

## Phase 1: Revise outline sections (draft {draft-n})

Targeted, evidence-driven edits to the `## Draft` blocks — **not** a rewrite. Work section-by-section
in the synthesis's priority order. This phase is `/paper-outline` work: it touches only
`outline/0N-*.md` and their `## Key Points`/`## Notes`, never `manuscript.tex`.

- [ ] 1.1: `/paper-outline {0N-first}` — apply {FB-{cycle}.NN, …}; reopen via `set_status.py --section {0N-first} --status draft` if not already
- [ ] 1.2: `/paper-outline {0N-second}` — apply {FB-{cycle}.NN, …}
- [ ] 1.3: `/paper-outline {0N-third}` — apply {FB-{cycle}.NN, …}
- [ ] 1.4: Cross-section sweep — {e.g. "apply the `"Title" (Descriptor)` parenthetical convention across all section headings"}
- [ ] 1.5: **GATE** — human reviews revised `## Draft` blocks; on approval `set_status.py --section {0N-*} --status review`
- [ ] 1.6: Commit — `DRAFT: Revise outline sections from cycle {cycle} feedback ({FB-IDs})`

## Phase 2: Re-integrate and audit (draft {draft-n})

Fold the approved outline prose into `manuscript.tex` and run the two-regime pass B, per
`.agents/factory/review-rubric.md`. This phase is `/paper-draft` work.

- [ ] 2.1: `/paper-draft {0N-*}` **pass A** — delta-based outline→LaTeX integration for the revised sections
- [ ] 2.2: `/paper-draft` **pass B** — fresh-subagent fidelity cold-read + blind claim/citation/invariant audit; findings via `ReportFindings`, most-severe first
- [ ] 2.3: Triage pass B findings; apply CONFIRMED must-fix, then `set_status.py --section {0N-*} --status integrated`
- [ ] 2.4: `make check` — no ERRORs (dangling cite, over page limit are hard blockers); resolve any `[FB-{cycle}.NN]` still open
- [ ] 2.5: `make build` succeeds; confirm page budget with `check_paper.py --page-limit {N}`
- [ ] 2.6: Commit — `DRAFT: {Nth} integration from cycle {cycle} revision`

## Phase 3: Close the cycle

- [ ] 3.1: Verify no open must-fix rows remain in the mapping table above; every resolved FB-ID is `[x]`
- [ ] 3.2: `set_status.py PAPER.md --verdict none --macro-phase in-review` (revision loop closed; awaits next external review or `/paper-release`)
- [ ] 3.3: Write session log(s) to `logs/<UTC-ISO>-{slug}.md` per `rules/session_logs.md`; add them to this plan's `related_logs`
- [ ] 3.4: Set this plan's frontmatter `status: completed`
- [ ] 3.5: Push `draft`

---

## Progress

**Completed**: {done}/{total}

---

## Session Prompt Template

Ready-to-paste prompt to resume this revision in a fresh session. Each phase is one session's unit of
work: complete its tasks, then **stop at the gate and ask for feedback** before advancing.

```
Continue the PEARC26 paper's {Nth} revision (review cycle {cycle}).

Execution procedure:

1. READ STATE FIRST: run
   `python3 .agents/factory/bin/paper_status.py PAPER.md`
   and confirm macro_phase=revising, review.cycle={cycle}. Then read
   `plans/{N}-revision.md` (this plan) and
   `outline/notes/review-synthesis.md` (authoritative checklist).

2. IDENTIFY CURRENT PHASE: the current phase is the lowest-numbered
   phase with any unchecked `[ ]` task.

3. LOAD PHASE INPUTS:
   Phase 1 → `outline/notes/review-feedback-{cycle-tag}.md`
             + the target `outline/0N-*.md` section file(s)
   Phase 2 → the revised `outline/0N-*.md` files + `manuscript.tex`
             + the section→anchor map in `PAPER.md`
   Phase 3 → finalize logs, close the FSM, push

4. TASK LOOP (current phase only):
   a. Find the next unchecked `[ ]` task.
   b. Execute it — invoke the named `/paper-outline` or `/paper-draft`
      skill; advance FSM state ONLY via
      `python3 .agents/factory/bin/set_status.py PAPER.md …`,
      never by hand-editing frontmatter.
   c. Mark it `[x]` in `plans/{N}-revision.md`; update the
      feedback→action table's Done column.
   d. Commit: `git commit -m "DRAFT: <desc> ({FB-IDs})" \
        -m "Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"`
   e. If unchecked tasks remain in this phase, go to (a).
   f. If a GATE task is next, STOP for human sign-off.

5. PHASE BOUNDARY: write a session log to `logs/` per
   `rules/session_logs.md`, push `draft`, then
   **STOP, report what was completed, and ask for feedback.**
   Do NOT begin the next phase until explicitly told to continue.

Never guess: if a feedback item is ambiguous, emit
`[NEEDS CLARIFICATION: …]` and ask rather than inventing an edit.
Use `/bin/rm` for any file deletion (not the `del` alias).
```
