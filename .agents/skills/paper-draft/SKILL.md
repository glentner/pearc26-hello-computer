---
name: paper-draft
description: >-
  Render the outline source-of-truth into manuscript.tex in two passes — the integrating phase of the
  paper factory. PASS A delta-integrates each `review`-bucket section's outline `## Draft` into
  manuscript.tex using the PAPER.md ```anchors``` heading map (never a hard-coded map), preserving
  every \cite and applying the invariants.md LaTeX prose conventions; `make build` must stay green.
  PASS B delegates to a FRESH subagent for two honest regimes — a fidelity cold-read (outline vs tex)
  and a genuinely BLIND claim + citation + invariant audit — which REPORTS and STOPS (no auto-fix).
  On human approval, fixes are applied and cleared sections advance review -> integrated. Absorbs and
  generalizes the legacy latex-integration-{first,second}-pass skills.
disable-model-invocation: true
argument-hint: "[<section-id> | all review sections | audit only | status]"
allowed-tools: Read, Write, Edit, Grep, Glob, Agent, ReportFindings, AskUserQuestion, Bash(git status *), Bash(git branch *), Bash(git rev-parse *), Bash(git log *), Bash(git diff *), Bash(git add *), Bash(git commit *), Bash(make *), Bash(python3 .agents/factory/bin/*), Bash(date -u *)
---

# paper-draft — render the outline into manuscript.tex (integrate, then verify)

## When to Use

Invoke `/paper-draft` once one or more sections have reached `review` status (their `## Draft` prose
is settled by `/paper-outline`) and you want that prose rendered into the single `manuscript.tex`.
This is the **integrating** phase: pass A folds the outline delta into the tex; pass B has a fresh
subagent verify it. Sections advance `review -> integrated` only after pass B is clean and the human
signs off. Re-runnable per section and per revision cycle — after `/paper-review` reopens sections,
run this again on the ones back in `review`.

The outline `## Draft` blocks are the **source of truth**; `manuscript.tex` is derived. Never author
new prose here that is not in the outline (and vice versa) — that divergence is exactly what pass B
catches. Heading placement comes from the `PAPER.md` ```anchors``` block, not memory and not the
deprecated `latex-integration-*` map.

## References

Read before delegating pass B:

- [`../../factory/methodology.md`](../../factory/methodology.md) — the lifecycle and where this phase sits.
- [`../../factory/invariants.md`](../../factory/invariants.md) — §2 LaTeX prose conventions (the
  integration contract), §3 citation integrity, §4 structural fidelity + heading-map accuracy.
- [`../../factory/claims.md`](../../factory/claims.md) — the C-ID convention the blind audit grades against.
- [`../../factory/review-rubric.md`](../../factory/review-rubric.md) — the refutation protocol, the
  severity scale, and the two pass-B regimes (cold-read fidelity vs. blind claim/citation audit). Note
  its `[reviewer-facing]` vs `[orchestrator-only]` section tags — pass B gets only the former.
- `AGENTS.md` (the constitution) for anything not enumerated above.
- **Portability:** [`portability.md`](../../factory/portability.md) — this skill runs on any harness; if the *Current state* commands aren't auto-injected, run them yourself in Step 1, and if `AskUserQuestion` is unavailable, ask in plain text and STOP. Without an `Agent` tool, do pass B as a genuinely fresh cold read yourself (blindness is weaker — compensate per the rubric) or escalate to a human reviewer.

## User Instructions

Additional instructions provided with the invocation: $ARGUMENTS

## Current state (injected at load)

- Branch: !`git branch --show-current`
- Tree: !`git status --porcelain | head -n 20`
- Recent commits: !`git log --oneline -n 8`
- FSM: !`python3 .agents/factory/bin/paper_status.py PAPER.md --summary 2>/dev/null || echo "run paper_status.py in Step 1"`

## Argument Parsing

Parse `$ARGUMENTS` case-insensitively; if ambiguous or self-contradictory, STOP and ask.

- `status` / `report` → run `paper_status.py` (Step 1), summarize the FSM (which sections are in
  `review`, which are `integrated`, `anchors_missing`, `review.cycle`/`verdict`) and stop. No work.
- `audit only` / `verify only` → skip pass A; run **pass B** (Steps 4–6) against the sections already
  `integrated`, or against a named section, to re-check fidelity/claims without re-integrating.
- `<section-id>` (e.g. `03-approach`) → run passes A and B for that one section only. It must be in
  `review`; if it is not, STOP and say so.
- `all review sections` / no arguments → run passes A and B for **every** section currently in the
  `review` bucket (from `paper_status.py`), in `order`.

## Safety Principles

- **`paper_status.py` is the resume ground-truth**, re-read fresh every invocation (Step 1). If it
  exits non-zero (invalid `PAPER.md`) or reports `anchors_missing`, **reconcile before integrating** —
  a stale anchor map means pass A would place prose wrong. Do not guess a heading; fix the ```anchors```
  block in `PAPER.md` first (it is body text, safe to hand-edit) and re-run.
- **On `draft`, clean-ish tree.** Work happens on branch `draft` (never `main`; shipping is
  `/paper-release`). If the tree is dirty with unrelated changes, STOP (commit, stash, or discard
  first). A dirty tree makes the pass-A checkpoint commit unclean.
- **Only integrate `review`-bucket sections.** A `draft` section is not ready (that is
  `/paper-outline`'s job); an `integrated` section is done. Never advance a section to `integrated`
  except via `set_status.py` after pass B is clean and the human approves.
- **The outline is the source of truth; the anchor map is the placement.** Delta-apply the outline
  `## Draft` into the tex; never invent prose, never drop a sentence, never drop a `\cite`. Preserve
  every citation key — reposition one only if its anchor sentence moved.
- **State moves only through the scripts.** Advance sections with
  `set_status.py --section <id> --status integrated`; never hand-edit `PAPER.md` frontmatter. The
  script also syncs the outline file's `status:` — no drift.
- **Pass B is delegated and structurally blind where it can be.** The audit runs in a **fresh
  subagent** (Agent tool), not this context — spawning is the guarantee, not trusting a `/clear`. The
  blind regime is given only the C-ID claims + `references.bib` + `manuscript.tex` **inline**, and must
  NOT read `outline/`, `plans/`, `reviews/`, the `PAPER.md` body, or `META.md` off disk — each leaks
  author intent (`META.md` also leaks harness meta-notes). The cold-read regime needs both sources.
  Hand the subagent only the **`[reviewer-facing]`** rubric sections, never the `[orchestrator-only]`
  ones. Pass B **reports and STOPS**; it never auto-fixes, and the subagent **leaves a clean tree** —
  the orchestrator commits with an explicit `git add <files>` (never `git add -A`) so nothing the
  subagent stranded rides in.
- **Never guess.** On any ambiguity (a section with no anchor, an outline sentence that maps to no
  heading, a `\cite` key absent from `references.bib`), emit a literal `[NEEDS CLARIFICATION: …]` and
  ask the human (AskUserQuestion) rather than inventing.
- **Deterministic gates are hard.** `make build` must succeed after pass A and after fixes;
  `make check` (via `check_paper.py`) must pass — a dangling cite or over-page-limit is a hard blocker
  (exit 1), not a judgment call.
- **Bounded loop (internal ≠ external).** The per-section draft↔audit loop is bounded by the section's
  **`attempts`** counter: record a pass-B RED with `set_status.py --section <id> --record-attempt` (and
  commit it, so the count survives a context reset); at `attempts ≥ 3` `paper_status.py` warns —
  stop-and-re-shape or escalate, do not loop. `review.cycle` is the **separate** external review↔revise
  counter (owned by `/paper-review`); do not conflate the two.
- **File ops:** delete with `/bin/rm` (never the Warp `del` alias). **Commits** are prefixed `DRAFT: `
  and carry the co-author trailer:
  `git commit -m "DRAFT: …" -m "Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"`.

## Procedure

### Step 0 — status / audit-only routing (when requested)
`status`: run `paper_status.py` (Step 1), report the FSM + last commit, and stop. `audit only`: skip
to Step 4 (pass B) against the target section(s), then Steps 5–6.

### Step 1 — Pre-flight
1. Confirm branch `draft` with an otherwise-clean tree (from the injection). STOP otherwise.
2. Run `python3 .agents/factory/bin/paper_status.py PAPER.md` and read its JSON. If it exits 2
   (invalid), STOP and report. If `anchors_missing` is non-empty, reconcile the ```anchors``` block in
   `PAPER.md` against the live `manuscript.tex` before continuing.
3. Determine the target section set from Argument Parsing: the named section, or every id in
   `sections_by_status.review`, processed in ascending `order`. If the set is empty, report "no
   sections in review" and stop.
4. Ensure `macro_phase` is `integrating` (or `revising`, which re-enters integrating). If it is not,
   advance it: `python3 .agents/factory/bin/set_status.py PAPER.md --macro-phase integrating`.
5. **Contract-drift check.** If `review.reviewed_commit` is set (from a prior audit), run
   `git log --oneline <reviewed_commit>..HEAD -- PAPER.md`. If the claims / thesis / non-goals changed
   since that audit **without** a corresponding `/paper-review` cycle bump, surface the drift to the
   human before grading — a C-ID silently rewritten to match what got drafted would let pass B pass a
   moved goalpost.

### Step 2 — PASS A: delta-integrate (per section, in order)
For each target section, one at a time (serial — never parallelize a single manuscript):
1. **Load both sources.** Read `outline/<id>.md` (the `## Draft` block is ground truth) and the
   corresponding region of `manuscript.tex`. Find that region via the `PAPER.md` ```anchors``` map:
   the section's `id | \anchor` line(s) give the exact heading command(s). A section may map to
   several anchors (e.g. `03-approach` → a `\section` plus three `\subsection`s); an id absent from
   the anchors block is a `[NEEDS CLARIFICATION]` — ask before proceeding.
2. **Identify deltas only.** Compare the outline `## Draft` prose against the current tex prose. List
   the passages that differ. If a section is already faithful ("no delta"), confirm and skip to its
   pass-B fidelity check — do not rewrite unchanged tex.
3. **Apply changes surgically.** Update only the changed passages, placing prose under the mapped
   heading command(s). Apply the `invariants.md` §2 LaTeX prose conventions:
   - **No raw em-dashes** (`---`) — use commas or reworded clauses; en-dashes `--` in ranges are fine.
   - **Quotes:** ``` ``…'' ```, never straight `"…"`.
   - **Emphasis / code:** `\emph{…}` for markdown `*…*`; `\texttt{…}` for markdown `` `…` ``.
   - **Non-breaking spaces:** `~` where a break reads badly (`Fig.~1`, `2~AM`, `al.~\cite{…}`).
   - **Wrap** by hand to the manuscript's existing convention (~80 chars).
   - **Preserve every `\cite{key}`**; reposition only if its anchor sentence moved.
4. **Build + check gate.** Run `make build` (must succeed) **and** `make check` (must exit 0 — a
   dangling `\cite` or over-page-limit is a hard STOP, caught here *before* spending a pass-B audit).
   Red → fix and re-run; a persistent red gate is a STOP, not a reason to advance state.

### Step 3 — Checkpoint commit (pass A)
Once all target sections integrate and `make build` + `make check` are green:
```
git add manuscript.tex PAPER.md references.bib
git commit -m "DRAFT: paper-draft pass A — integrate <ids> from outline" \
           -m "Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```
(Explicit add — no `git add -A`, so nothing unrelated rides into the checkpoint.)
This checkpoints the integration **before** the audit, matching the legacy first-pass discipline. Do
NOT advance any section to `integrated` yet — pass B has not run.

### Step 4 — PASS B: delegate verification to a FRESH subagent
Launch a fresh reviewer via the `Agent` tool (a new context removes authoring bias). Per
`review-rubric.md`, it runs **two regimes**; give it the refutation protocol (try to disprove each
finding; CONFIRMED = reproduced with a concrete discrepancy, PLAUSIBLE = plausible but not pinned,
drop when uncertain) and the severity scale (`must-fix` | `should-fix` | `consider`):

- **(i) Fidelity cold-read (NOT blind — needs both sources).** Give it, for each target section, the
  outline `## Draft` AND the corresponding `manuscript.tex` region (located via the ```anchors``` map).
  It re-reads both from scratch, sentence by sentence: no dropped/added/reordered words, no stale text
  from prior drafts, paragraph breaks match, and the §2 LaTeX prose conventions are applied.
- **(ii) Claim + citation + invariant audit (genuinely BLIND).** Give it the C-ID claim statements +
  their `evidence` bibkeys (extracted from `PAPER.md`) **inline**, `references.bib`, and
  `manuscript.tex` — **and nothing else**. Tell it explicitly NOT to read `outline/`, `plans/`,
  `reviews/`, the `PAPER.md` body, or `META.md` off disk — each leaks author intent (`META.md` also
  leaks harness meta-notes). It asks: is each claim actually supported by its cited evidence? Does
  every `\cite` resolve (defer the mechanical pass to `check_paper.py`)? Any `invariants.md` violation
  (page/ACM policy, prose conventions, citation integrity, stale AI-use disclosure)?

Give the subagent only the **`[reviewer-facing]`** sections of `review-rubric.md` (refutation protocol,
severity scale, and the one regime it runs) — never the `[orchestrator-only]` sections, or it will
believe it owns verdicts / state transitions. Instruct it to **report and STOP — no auto-fix, and leave
a clean tree**: findings most-severe-first, each with section + `manuscript.tex` line + severity +
CONFIRMED/PLAUSIBLE + the quoted evidence, emitted via `ReportFindings` (and/or a written list) —
**consume its returned findings, never read its `.output` transcript sidecar** (that floods context).
Also run `make check` yourself and fold the deterministic ERRORs/WARNINGs into the finding set — a
dangling cite or over-page-limit is a hard `must-fix`.

**Later cycles.** If this is a re-run after `/paper-review` reopened sections, **declare the mode**:
default is a fresh blind pass over the reopened sections; the human may scope it to verifying named
`FB-N.NN` items were remediated. Record the choice in the session log (Step 6).

### Step 5 — Present findings + human gate
Collect the subagent's findings; do a light sanity pass (drop anything not backed by quoted evidence).
Present them to the human, grouped by severity, most-severe-first. A CONFIRMED `must-fix` touching a
factual claim, a citation, the AI-use disclosure, or a page/ACM-policy invariant requires explicit
human sign-off before any fix or state change (`review-rubric.md` mandatory gate). If pass B is clean
(no CONFIRMED findings), say so — silence on a clean section is a valid result — and proceed to Step 6.

### Step 6 — Apply approved fixes, advance state, commit + log
On human approval:
1. Apply the approved fixes to `manuscript.tex` (still delta-style, conventions intact).
2. Re-run `make build` **and** `make check` — both must pass (no ERRORs).
3. **Advance clean sections; record stuck ones.** For each section now clean:
   `python3 .agents/factory/bin/set_status.py PAPER.md --section <id> --status integrated` (also syncs
   `outline/<id>.md`). For each section that stayed RED (a CONFIRMED must-fix sending it back), record
   the failed attempt so the breaker survives a context reset:
   `python3 .agents/factory/bin/set_status.py PAPER.md --section <id> --record-attempt`. At
   `attempts ≥ 3` (a `paper_status.py` warning) **stop-and-re-shape or escalate — do not loop.** If
   every section is now `integrated`, consider `--macro-phase in-review` per the human's direction.
4. **Meta-note (silence by default), orchestrator-written.** Did `/paper-draft` *itself* (not you, not
   the task) cost something this run? Almost always no — silence is the default. If yes and it clears
   the bar, append a `## F<n>` finding to the repo-root `META.md` (`origin=paper-draft:<step>` …) per
   `.agents/factory/templates/META.md`. **The pass-B subagent never sees `META.md`** — only the
   orchestrator writes it, here, after the audit. A content/task issue is not a finding.
5. Commit (explicit add — no `git add -A`, so a subagent-stranded file can't ride in):
   ```
   git add manuscript.tex PAPER.md references.bib META.md
   git commit -m "DRAFT: paper-draft pass B — audit fixes; integrate <ids>" \
              -m "Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
   ```
6. **Record the audited commit** (so `/paper-release` can gate on a *current* audit). Now that the
   manuscript state is committed, point `reviewed_commit` at it and commit that one-line PAPER.md
   change (the release gate diffs only `manuscript.tex`/`references.bib`, so a PAPER.md-only follow-up
   doesn't trip it):
   ```
   python3 .agents/factory/bin/set_status.py PAPER.md --reviewed-commit "$(git rev-parse HEAD)" --touch
   git add PAPER.md && git commit -m "DRAFT: paper-draft — record audited commit" \
              -m "Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
   ```
7. **Session log (MANDATORY, orchestrator-written).** Write `logs/<UTC-ISO>-<slug>.md` (UTC via
   `date -u +"%Y-%m-%dT%H-%M-%S"`) with the VERBATIM user_input, what integrated, the pass-B findings +
   their disposition, the later-cycle mode chosen (if a re-run), any `--record-attempt` recorded, and
   the new section statuses. The orchestrator writes this, not the subagent.

### Final report
Sections integrated (ids), sections left in `review` and why, pass-B findings by severity with
CONFIRMED/PLAUSIBLE counts and dispositions, `make build`/`make check` results, the review cycle
count, and the recommended next step (`/paper-outline` to fix a reopened section, or `/paper-release`
once all sections are `integrated` and the paper is clean). Stop.

## Examples

- `/paper-draft` — integrate every section currently in `review`, then delegate the fresh-subagent
  pass-B audit; present findings and stop for sign-off.
- `/paper-draft 03-approach` — passes A and B for just `03-approach` (must be in `review`).
- `/paper-draft audit only` — skip integration; re-run the cold-read + blind audit against the
  currently `integrated` sections and `make check`; report and stop.
- `/paper-draft status` — show which sections are `review`/`integrated`, `anchors_missing`, and the
  review cycle/verdict; no work.

## Notes

- The heading map is **data**, read from the `PAPER.md` ```anchors``` block — this generalizes the
  hard-coded A4 map the legacy `latex-integration-first-pass` carried, so it works for any section
  set. Seed/repair anchors from the live `manuscript.tex`, never from the deprecated map.
- Never advance a section to `integrated` on a green build alone — pass B (fidelity + blind audit) and
  the human gate are the real gate. `make check` ERRORs are hard blockers regardless of the audit.
- Pass A and pass B are separated on purpose (mode-(3) fix from the legacy skills): combining prose
  conversion and fidelity checking in one step compounds errors. Keep the pass-A checkpoint commit.
- This skill never ships to `main`, tags, or builds the TAPS package — that is `/paper-release`. If
  asked to release, STOP and point at it.
- Some `git`/`make` steps may prompt for permission per `settings.local.json`; that is expected.
