---
name: paper-outline
description: >-
  Fold research into section prose — the drafting phase of the paper factory. Picks one outline
  section (`outline/0N-*.md`), reads its `## Key Points`, the REFNOTEs for the C-IDs it `satisfies`
  and its topic (`outline/notes/refs/*.md`), and any `outline/snippets/`, then writes the section's
  `## Draft` prose: every Key Point covered, each non-obvious claim cited to a source, one voice,
  target_words as a soft cap. Advances the section `draft → review` via set_status.py, DRAFT-commits,
  and writes a session log. Strictly serial and single-voice, RE-RUNNABLE per section, one section
  per invocation by default. NO LaTeX here — that is /paper-draft; the `## Draft` block is the source
  of truth (see .agents/factory/methodology.md).
disable-model-invocation: true
argument-hint: "[<section-id> | next | status | dry run]"
allowed-tools: Read, Write, Edit, Grep, Glob, Bash(git status *), Bash(git branch *), Bash(git add *), Bash(git commit *), Bash(git log *), Bash(python3 .agents/factory/bin/*), Bash(date -u *)
---

# paper-outline — fold research into section prose

## When to Use

Invoke `/paper-outline` once the paper is scoped and at least the relevant sources are researched, to
turn a section's `## Key Points` + REFNOTEs into finished `## Draft` prose. The rhythm is
**one-section-then-stop**: name a section to work it, or say `next` to take the highest-priority
`draft`/actionable section in **writing order**. This is the `/hs-build` analog *for prose* — but it
writes Markdown into `outline/0N-*.md`, never LaTeX. The `## Draft` block is the **source of truth**;
`/paper-draft` renders it into `manuscript.tex` later.

`PAPER.md` frontmatter is the resume ground-truth (read it with `paper_status.py`, mutate it with
`set_status.py` — never hand-edit). The outline section file's `## Draft` is the deliverable; the
REFNOTEs (`outline/notes/refs/<bibkey>.md`) and `references.bib` are the evidence you fold in.

## References

- [`../../factory/methodology.md`](../../factory/methodology.md) — the lifecycle; `/paper-outline` is
  "hs-build, for prose" (§ lifecycle diagram, principle 3 "never parallel for drafting").
- [`../../factory/invariants.md`](../../factory/invariants.md) — the prose self-check (§2 conventions,
  §3 citation integrity, §4 fidelity, §5 honesty).
- [`../../factory/claims.md`](../../factory/claims.md) — C-IDs; how a section `satisfies` a claim and
  how folded evidence links to `satisfied_by`/`evidence`.
- [`../../factory/review-rubric.md`](../../factory/review-rubric.md) — severity vocabulary shared with
  the audit that grades this prose later.
- **Portability:** [`portability.md`](../../factory/portability.md) — this skill runs on any harness; if the *Current state* commands aren't auto-injected, run them yourself in Step 1, and if `AskUserQuestion` is unavailable, ask in plain text and STOP.

## User Instructions

Additional instructions provided with the invocation: $ARGUMENTS

## Current state (injected at load)

- Branch: !`git branch --show-current`
- Tree: !`git status --porcelain | head -n 20`
- Recent commits: !`git log --oneline -n 8`
- Paper FSM: !`python3 .agents/factory/bin/paper_status.py PAPER.md --summary 2>/dev/null || echo "(run paper_status.py in Step 1)"`

## Argument Parsing

Parse `$ARGUMENTS` case-insensitively; if ambiguous or self-contradictory, STOP and ask.

- `<section-id>` (e.g. `03-approach`) → work **that** section, regardless of its current status.
- `next` / no argument → auto-pick the target in Step 2 (highest-priority `draft`/actionable section
  by **writing order** — **never** auto-pick the abstract first).
- `status` / `report` → summarize FSM state (via `paper_status.py`, Step 1) + the last commit; no work.
- `dry run` / `plan only` / `preview` → do Steps 1–3 (pick the section, load its evidence), then
  report the plan (which Key Points, which REFNOTEs/snippets, target_words, expected commit) and STOP
  — make **no** edits or commits.

## Safety Principles

- **`paper_status.py` is the resume ground-truth**, re-run fresh every invocation (Step 1). If it
  exits non-zero (invalid `PAPER.md`) or reports `warnings` (anchor/status drift), **reconcile before
  acting** — do not guess.
- **On `draft` only.** If the branch is not `draft`, STOP. A dirty tree unrelated to this section → STOP
  (commit, stash, or discard first). Shipping to `main` is `/paper-release`.
- **One section is the unit of work.** Cover **every** `## Key Point`, not just the first. Stop after
  one section by default and report the next candidates; only continue to more sections when the
  argument names another or the human asks.
- **Serial and single-voice (methodology principle 3).** Never fan out subagents to draft — parallel
  writers make conflicting voice/structure decisions in one manuscript. Read broadly, write one
  section yourself.
- **NO LaTeX.** Write Markdown prose into `## Draft`. `\cite{}`, `\emph{}`, `\section{}`, `---`
  em-dashes, and the anchor map are all `/paper-draft`'s job. Cite sources by their `references.bib`
  bibkey in-prose (e.g. "(godoy2024llm)" or an author-year phrasing) so the render step can resolve
  them — do not invent citation macros here.
- **Evidence, not invention (invariants §5).** Every non-obvious/empirical/historical claim must
  trace to a REFNOTE or a repo artifact you actually read. No invented numbers, no sources not in
  `references.bib`. If the evidence for a Key Point is missing, do **not** fabricate it — leave a
  literal `[NEEDS CLARIFICATION: …]` / `[NEEDS SOURCE: …]` marker and flag that `/paper-research` owes
  a source.
- **target_words is a soft cap, the page budget is hard.** Aim at the section's `target_words`; a
  modest overrun is fine, but a bloated draft costs pages later — cut to the thesis, don't pad.
- **Never guess.** On ambiguous scope for the section, emit `[NEEDS CLARIFICATION: …]` in the `##
  Notes` block and ask the human (do not silently decide). An unresolved marker is a STOP.
- **Advance state only via `set_status.py`**, never by hand-editing frontmatter; it also syncs the
  outline file's `status:`. Write a session log at the end.

## Procedure

### Step 0 — status / dry-run (when requested)
`status`: run `paper_status.py` (Step 1), report the FSM + last commit, and STOP. `dry run`: do
Steps 1–3, report the plan that *would* run, and STOP (no edits, no commit).

### Step 1 — Pre-flight
1. Confirm the branch is `draft` and the tree is clean (from the injection). STOP otherwise.
2. Run `python3 .agents/factory/bin/paper_status.py PAPER.md` and read its output. Exit 2 → `PAPER.md`
   invalid, STOP. Non-empty `warnings` (anchor/status drift) → reconcile or STOP and report.
3. **Advance the macro-phase if needed.** If `macro_phase` is `scoped` or `researching`, this is the
   first fold — advance it:
   `python3 .agents/factory/bin/set_status.py PAPER.md --macro-phase outlining --touch`.
   If it is already `outlining` (or `integrating`/`revising`, i.e. a re-run/revision), leave it. If
   it is `in-review`/`released`, note that outlining is complete and confirm with the human before
   reopening a section.

### Step 2 — Pick the target section
1. **Explicit id** → use it (work it regardless of status). Confirm the `outline/<id>.md` file exists;
   unknown id → STOP.
2. **`next` / no argument** → choose from `actionable_next` (falling back to the `draft` bucket),
   ordered by the section `order` field (writing order) — the lowest `order` first. **Never auto-pick
   `00-abstract` first**: the abstract is written last (it has the highest `order`), so skip it unless
   it is the only section left or the human names it.
3. If which section to work is ambiguous (e.g. several equally-ranked, or the section's intent is
   unclear), STOP and ask — do not guess.

### Step 3 — Load the section's context
Read, before writing anything:
1. The target `outline/<id>.md` in full — its frontmatter (`status`, `target_words`), `## Key Points`,
   `## Notes`, and any existing `## Draft` (a re-run refines in place, it does not blindly overwrite).
2. The REFNOTEs that back it: `outline/notes/refs/<bibkey>.md` for every source relevant to the
   section — both by the **C-IDs the section `satisfies`** (cross-reference the `claims:` `evidence`
   bibkeys in `PAPER.md`) and by **topic** (the Key Points). Use their `key_findings`,
   `quotable_phrases`, and `sample_sentences`.
3. `outline/snippets/` for any reusable prose fragments (e.g. running jokes/motifs) the section uses.
4. `outline/notes/*.md` deep-dives the section's `## Notes` references, if any.

### Step 4 — Fold the evidence into `## Draft`
Write the section's `## Draft` prose (Markdown, in `outline/<id>.md`):
- **Cover every `## Key Point`** — each becomes a claim, sentence, or paragraph. Nothing dropped.
- **Cite each non-obvious claim** to its source by `references.bib` bibkey, inline in prose (not as a
  LaTeX macro). Empirical/historical assertions and the section's C-ID claims must be evidenced.
- **One voice.** Match the register and structure of the already-drafted sections; keep subsection
  structure consistent with `## Notes` and the eventual anchor map. Do not introduce a second style.
- **Respect `target_words`** as a soft cap; prefer the thesis over completeness. On a re-run, tighten
  and integrate rather than append.
- If a Key Point has no backing evidence, leave `[NEEDS CLARIFICATION: …]` / `[NEEDS SOURCE: …]` and
  note the gap for `/paper-research` — never fabricate.

### Step 5 — Self-check (the prose gate)
Re-read the draft against `invariants.md` before advancing:
- §2 prose conventions — write clean Markdown; **no raw `---` em-dashes** (use commas or rewording),
  no LaTeX. (LaTeX-specific conventions like `\emph`/`\texttt`/`~` are `/paper-draft`'s to apply.)
- §3 citation integrity — every non-obvious claim carries a bibkey that exists in `references.bib`.
- §5 honesty — every number/claim traces to a source you read; C-IDs the section `satisfies` are
  genuinely argued here.
- Word budget — roughly within `target_words`; if far over, cut. Update the file's `actual_words:`
  note (approximate) if the section uses one.
- **Scope circuit breaker (soft).** If the section still cannot be brought within `target_words` after
  honest tightening — especially on a re-run where it overshot before — PAUSE: do not silently ship an
  over-budget draft that lets the *hard* page budget blow later. Report the overrun and offer the human
  a choice (CUT which material, or MOVE it to another section / a footnote / cut-content note) rather
  than truncating on your own. A prompt to the human, not a hard truncation.
- Every `## Key Point` is covered and no unresolved marker remains that you can resolve now.
If the section cannot pass honestly (missing evidence, unresolved ambiguity), do **not** advance —
leave it `draft`, report the blocker, and stop.

### Step 6 — Advance the section state
Only when the draft passes Step 5:
```
python3 .agents/factory/bin/set_status.py PAPER.md --section <id> --status review --touch
```
This rewrites `PAPER.md` frontmatter **and** syncs `outline/<id>.md`'s `status:` to `review` (no
drift). Exit 3 → unknown section id (recheck the id); exit 2 → invalid input (STOP). Do not hand-edit
the frontmatter or the outline `status:` line.

### Step 7 — Meta-note (silence by default)
Before committing, ask ONE question: *did the skill itself (not you, not the task) cost something this
run?* Almost always the answer is no — **silence is the default; most runs add nothing.** If yes AND it
clears the bar in `.agents/factory/templates/META.md`, append a `## F<n>` finding to the **repo-root
`META.md`** (create it from `.agents/factory/templates/META.md` if absent): a metadata line
`origin=paper-outline:<step> severity=<high|medium|low> category=<instruction|steering|tooling|template|missing-guidance> status=open target=<best-guess file>`
plus the **What happened / Skill cause / Recommended fix / Confidence · Effort** bullets. Keep it to ≤3
findings; if an equivalent finding exists, append "· seen again" to its title rather than duplicating. A
content/task issue is NOT a finding — it belongs in `PAPER.md` **Clarifications**, a `reviews/` note,
or a `[NEEDS CLARIFICATION]` marker. Add `META.md` to that step's `git add`. You only *record*;
the human-gated `/paper-harness` is what later applies these.

`/paper-outline` is the factory's **richest producer** of these notes — it runs once per section across
many sessions, so a friction finding appended to `META.md` here preserves signal that a context reset
would otherwise erase.

### Step 8 — Commit (atomic prose + state)
```
git add outline/<id>.md PAPER.md META.md
git commit -m "DRAFT: Outline <id> — fold research into draft" \
           -m "Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```
Every branch commit is prefixed `DRAFT:` (stripped at `/paper-release`). Keep the subject specific to
the section; use the body for non-obvious decisions or a `[NEEDS SOURCE]` note. (`META.md` is staged
only if Step 7 wrote a finding.) Do not push.

### Step 9 — Session log (MANDATORY)
The orchestrator (this skill) writes `logs/<UTC-ISO>-<slug>.md` from the live conversation. Get the
timestamp with `date -u +"%Y-%m-%dT%H-%M-%S"`; `<slug>` = `outline-<id>`. Capture the **verbatim**
user invocation in the frontmatter `user_input`, plus what was folded, the source bibkeys cited, the
new section status, and any markers/blockers left. Commit the log (may be folded into the Step 8
commit or a follow-up `DRAFT:` commit).

### Step 10 — Continue or stop
Default: STOP after **one** section and report the next candidates (from `paper_status.py`
`actionable_next` in writing order). Only continue to another section when the argument named it or
the human asked; re-run Steps 2–9 per section. When all sections reach `review`
(`completion.outlining_complete`), recommend `/paper-draft` to integrate them into `manuscript.tex`.

### Final report
Section worked (id + one-line summary of what was folded), source bibkeys cited, any `[NEEDS
CLARIFICATION]`/`[NEEDS SOURCE]` markers left, the new section status and `macro_phase`, the word
count vs. `target_words`, and the next candidate sections (writing order). If a Key Point lacked
evidence, name the source `/paper-research` still owes.

## Examples

- `/paper-outline` — auto-pick the next actionable section (writing order, not the abstract), fold its
  research into `## Draft`, advance it `draft → review`, one `DRAFT:` commit, log, stop.
- `/paper-outline 03-approach` — work the Approach section specifically (even if not "next").
- `/paper-outline next` — same as no-argument: take the highest-priority draft section by `order`.
- `/paper-outline dry run` — show which section, Key Points, REFNOTEs, and target_words would be used;
  no edits.
- `/paper-outline status` — report FSM state (sections by status, claims lacking evidence) + last
  commit; no work.

## Notes

- **This skill produces Markdown, not LaTeX.** The `## Draft` block is the source of truth;
  `/paper-draft` renders it into `manuscript.tex` (pass A) and audits fidelity (pass B). Writing
  `\cite`/`\section`/`---` here creates drift the render step must undo — don't.
- **Never auto-start with the abstract.** It is written last (highest `order`) so it can summarize the
  finished sections; only work `00-abstract` when explicitly named or when it is the only one left.
- **Re-runnable and additive.** Re-invoking on a section (or after `/paper-research` adds a source)
  refines the existing `## Draft` in place — integrate new evidence, tighten prose, re-run the Step 5
  gate — it does not blindly overwrite good prose.
- **Bounded self-correction.** If a section will not converge across repeated re-runs (unresolved
  markers, thin evidence), STOP and raise it to the human or point at `/paper-research` — do not loop.
- Advancing `draft → review` (not `integrated`): a section is `integrated` only after `/paper-draft`
  renders and audits it. Keeping the distinction is what makes the outline↔tex fidelity check real.
