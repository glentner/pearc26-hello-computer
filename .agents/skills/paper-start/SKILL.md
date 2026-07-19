---
name: paper-start
description: >-
  Scope a NEW paper from a clean draft branch (the first step of the paper-factory lifecycle; the
  hs-feature analog). Gathers the contract interactively — venue/template, thesis, 3-5 contribution
  claims (C-IDs, plain assertions per claims.md), non-goals, seed references, and the section skeleton
  with per-section target_words + writing order + page budget — then writes PAPER.md from the CONTRACT
  template (macro_phase: scoped) and scaffolds the outline/ skeleton (00-abstract .. 06-acks stubs,
  READMEs, a references.bib stub). Refuses to clobber an existing PAPER.md. STOPs for sign-off before
  any research spend. Never guesses: unresolved ambiguity becomes a literal [NEEDS CLARIFICATION]
  marker recorded in PAPER.md. See .agents/factory/methodology.md.
disable-model-invocation: true
argument-hint: "<inline paper description / thesis> | status"
allowed-tools: Read, Write, Edit, Grep, Glob, AskUserQuestion, Bash(git status *), Bash(git branch *), Bash(git rev-parse *), Bash(git log *), Bash(git add *), Bash(git commit *), Bash(python3 .agents/factory/bin/*)
---

# paper-start — scope the paper (the contract)

## When to Use

Invoke `/paper-start` on a clean `draft` branch to begin a brand-new paper. It produces exactly two
things — the repo-root `PAPER.md` contract (`macro_phase: scoped`) and the `outline/` section
skeleton — and then **stops** for your sign-off before the expensive `/paper-research` step. This is
**scoping**: make the thesis coherent, the contribution claims falsifiable and bounded, and the
section skeleton fit the page budget, while leaving the drafting free. Do **not** research, survey
the literature, or write prose here — that is `/paper-research` and `/paper-outline`.

It **refuses to clobber** an existing `PAPER.md`: a paper is scoped once. To inspect or resume an
already-scoped paper, use `python3 .agents/factory/bin/paper_status.py` (or `/paper-research`,
`/paper-outline`), not this skill.

## References

- [`.agents/factory/methodology.md`](../../factory/methodology.md) — the lifecycle; principle 5
  (ceremony scales to the page/word budget) and principle 6 (never guess — `[NEEDS CLARIFICATION]`).
- [`.agents/factory/claims.md`](../../factory/claims.md) — the C-ID convention: plain falsifiable
  assertions (NOT EARS), hybrid policy, keep the set to ≈3-5 headline claims.
- [`.agents/factory/invariants.md`](../../factory/invariants.md) — §1 venue & format (the 4-page
  budget, `acmart`, rights, AI-use disclosure) you lock into the contract here.
- Template: [`CONTRACT.md`](../../factory/templates/CONTRACT.md) — the shape of the `PAPER.md` you
  write (frontmatter FSM subset + body: thesis, claims, non-goals, anchor map, venue notes).
- Rules: [`session_logs.md`](../../../rules/session_logs.md) (mandatory end-of-session log),
  [`structural_docs.md`](../../../rules/structural_docs.md) (keep `outline/README.md` in sync),
  [`draft_commits.md`](../../../rules/draft_commits.md) (branch `draft`, `DRAFT:` prefix),
  [`file_deletion.md`](../../../rules/file_deletion.md) (use `/bin/rm`, not the Warp-era `del`).
- **Portability:** [`portability.md`](../../factory/portability.md) — this skill runs on any harness; if the *Current state* commands aren't auto-injected, run them yourself in Step 1, and if `AskUserQuestion` is unavailable, ask in plain text and STOP.

## User Instructions

Additional instructions provided with the invocation: $ARGUMENTS

## Current state (injected at load)

- Branch: !`git branch --show-current`
- Tree: !`git status --porcelain | head -n 20`
- PAPER.md present?: !`test -f PAPER.md && echo "EXISTS — /paper-start will REFUSE to clobber; use paper_status.py or /paper-research instead" || echo "absent — clear to scope a new paper"`
- Paper FSM: !`python3 .agents/factory/bin/paper_status.py PAPER.md --summary 2>/dev/null || echo "(run paper_status.py in Step 1)"`

## Argument Parsing

Parse `$ARGUMENTS` case-insensitively.

- `status` / `report` → if `PAPER.md` exists, run `paper_status.py` and report the phase, slug, and
  claim count; if it does not exist, say "no paper scoped yet — run `/paper-start <description>`".
  Either way **do no work**, write no files, no commit.
- An inline description / thesis sentence → adopt it as the **seed** for the interactive scoping
  (Step 2). Preserve the author's intent; only structure and disambiguate it.
- No arguments **and** no `PAPER.md` → begin interactive scoping from a blank slate (Step 2 will ask).
- No arguments **and** a `PAPER.md` already exists → STOP per the pre-flight refusal (Step 1).

## Safety Principles

- **On `draft`, otherwise-clean tree.** If the injected branch is not `draft`, STOP (do not auto-switch
  or stash). Any modified or untracked file → STOP (commit, stash, or discard first).
- **Never clobber a scoped paper.** If `PAPER.md` already exists, STOP and report it — do not
  overwrite it, and do not "merge" a new scope into it. A paper is scoped exactly once; point the
  human at `paper_status.py` / `/paper-research` instead.
- **Never guess.** On any ambiguity in the thesis, a claim, the section skeleton, or the venue,
  emit a literal `[NEEDS CLARIFICATION: …]` marker in the `PAPER.md` **Clarifications** section and
  ask the human via `AskUserQuestion`. Record answers there. An unresolved marker **blocks**
  `/paper-research`, so resolve what you can now.
- **Scoping only.** No literature search, no survey fan-out, no prose drafting, no `manuscript.tex`.
  If you feel the urge to research a source, that is `/paper-research`'s job.
- **Keep the claim set small.** ≈3-5 headline C-IDs (claims.md); demote the rest to informal
  `## Key Points` in the outline. Do not manufacture claims to look complete.
- **Respect the page budget.** The appetite is the page/word budget (a PEARC '26 extended abstract
  is 4 pages). Size `target_words` to fit; scope is cuttable, not inflatable.
- **Never hand-edit the frontmatter FSM.** After writing `PAPER.md` from the template, validate and
  mutate FSM state only via `paper_status.py` / `set_status.py` (the body is human free-text).
- **Advance no further.** This skill leaves `macro_phase: scoped` and STOPs. It never researches,
  drafts, integrates, or ships.

## Procedure

### Step 0 — status (when requested)
`status`: run `paper_status.py` if `PAPER.md` exists (else report "no paper scoped"), print the
phase/slug/claim count, and stop. No edits, no commit.

### Step 1 — Pre-flight
1. Confirm the injected branch is `draft` and the tree is otherwise clean. STOP otherwise.
2. **Refuse to clobber.** If `PAPER.md` exists (from the injection or `test -f PAPER.md`), STOP and
   report: "A paper is already scoped (`slug`, `macro_phase`). `/paper-start` will not overwrite
   it — run `python3 .agents/factory/bin/paper_status.py` to inspect it, or `/paper-research` to
   continue." Do nothing else.

### Step 2 — Gather the contract (interactive; never guess)
Use `AskUserQuestion` for each decision; for anything left open, write a `[NEEDS CLARIFICATION: …]`
marker into the contract and keep going. Gather, seeding from `$ARGUMENTS` where given:
1. **Venue & template** — default ACM PEARC '26 extended abstract, `acmart` (`sigconf`), rights
   `\setcopyright{cc}` / `\setcctype{by}`, AI use disclosed in `\begin{acks}` (invariants §1).
   Confirm or override.
2. **Page/word budget** — default the 4-page PEARC limit; confirm.
3. **Thesis** — the single argument, in two or three sentences (the CONTRACT "Thesis" block).
4. **Contribution claims** — 3-5 falsifiable, scoped, plain assertions with stable ids `C1`, `C2`,
   … (claims.md; NOT EARS). Note each claim's `kind` and which sections will argue it.
5. **Non-goals** — explicit exclusions that keep scope inside the budget.
6. **Seed references / prior work** — bibkeys or leads for `/paper-research` to deep-dive later (do
   not fetch them now). These go in the "Venue & build notes" seed-references line.
7. **Section skeleton** — the section ids (default the seven `00-abstract` … `06-acks`), each with a
   `target_words` and a writing `order`, plus which C-IDs each section `satisfies`. Keep the sum of
   `target_words` inside the page budget.

**Soft scope circuit breaker.** If scoping yields **more than ~5 headline C-IDs**, or the summed
section `target_words` exceeds the page budget, PAUSE and offer to cut scope into `## Non-goals`
(the paper analog of "cut scope, don't inflate") before proceeding — this is a prompt to the human,
not a hard limit.

### Step 3 — Write `PAPER.md` from the CONTRACT template
Copy [`.agents/factory/templates/CONTRACT.md`](../../factory/templates/CONTRACT.md) and fill it:
- **Frontmatter (machine subset):** `slug` (concise kebab from the title), `title`, `venue`,
  `template`, `macro_phase: scoped`, `base: main`, `branch: draft`, `last_updated` (today), the
  `sections:` list (`id`, `status: draft`, `satisfies`, `target_words`, `order`), the `claims:` list
  (`id`, `status: proposed`, `satisfied_by`, `evidence: []`), `review: {cycle: 0, verdict: none}`.
- **Body (human free-text):** Thesis, `## Contribution Claims` (the `C-ID — statement *(kind)*`
  bullets, matching the frontmatter ids), `## Non-goals`, `## Clarifications` (resolved Q/A plus any
  remaining `[NEEDS CLARIFICATION]` markers), `## Section → LaTeX anchor map` (leave the `anchors`
  block **empty/stub** — it is seeded from the live `manuscript.tex` on the first `/paper-draft`
  run, never guessed here), and `## Venue & build notes` (venue, template/rights, seed references,
  source-of-truth note).

### Step 4 — Scaffold the `outline/` skeleton
Create one file per section id, `outline/00-abstract.md` … `outline/06-acks.md`, each:
```markdown
---
status: draft
target_words: <N from the skeleton>
---

# <Section Title>

## Key Points
- [NEEDS CLARIFICATION: key points to be developed in /paper-outline]

## Notes
- Satisfies: <C-IDs, if any>

## Draft
<!-- prose stub — folded in by /paper-outline; this ## Draft block is the source of truth -->
```
Also create:
- `outline/README.md` — the structural doc (workflow overview, section-file list + descriptions,
  section-file format, page budget); per `structural_docs.md`.
- `outline/notes/refs/README.md` — an **empty** deep-dive checklist (Status Legend `[ ]`/`[~]`/`[x]`,
  a `## References (0 total)` list seeded with any Step-2 seed references as `- [ ]` lines, a
  `## Progress` line, and a `## Session Prompt Template` block for `/paper-research`).
- `references.bib` — a stub (a header comment noting all sources live here; empty otherwise).

To add a section or claim **later** (e.g. during a revision), use `set_status.py --add-section` /
`set_status.py --add-claim` — never hand-edit the `PAPER.md` frontmatter.

### Step 5 — Validate the FSM
Run `python3 .agents/factory/bin/paper_status.py PAPER.md`. It **must exit 0**. If it exits 2
(invalid) or reports warnings, fix the `PAPER.md` you wrote (re-check the frontmatter subset against
the template) and re-run until clean. Do not hand-fix by guessing the serialization — match the
template exactly.

### Step 6 — Sync structural docs
Ensure `outline/README.md` lists every section file you created and any notes/snippets stubs, and
that its page-budget allocation matches the `target_words` in `PAPER.md` (`structural_docs.md`). No
broken references.

### Step 7 — Meta-note (silence by default)
Before committing, ask ONE question: *did the skill itself (not you, not the task) cost something this
run?* Almost always the answer is no — **silence is the default; most runs add nothing.** If yes AND it
clears the bar in `.agents/factory/templates/META.md`, append a `## F<n>` finding to the **repo-root
`META.md`** (create it from `.agents/factory/templates/META.md` if absent): a metadata line
`origin=paper-start:7 severity=<high|medium|low> category=<instruction|steering|tooling|template|missing-guidance> status=open target=<best-guess file>`
plus the **What happened / Skill cause / Recommended fix / Confidence · Effort** bullets. Keep it to ≤3
findings; if an equivalent finding exists, append "· seen again" to its title rather than duplicating. A
content/task issue is NOT a finding — it belongs in `PAPER.md` **Clarifications**, a `reviews/` note,
or a `[NEEDS CLARIFICATION]` marker. Add `META.md` to that step's `git add`. You only *record*;
the human-gated `/paper-harness` is what later applies these.

### Step 8 — DRAFT commit + session log
1. Stage the scaffold and commit:
   ```
   git add PAPER.md outline/ references.bib META.md
   git commit -m "DRAFT: scope paper <slug>" -m "Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
   ```
   Do not push.
2. Write the mandatory session log to `logs/<UTC-ISO>-scope-paper-<slug>.md` (timestamp via
   `date -u +"%Y-%m-%dT%H-%M-%S"`), with the **verbatim** `$ARGUMENTS` as `user_input`, the files
   created, the commit, and a short summary. The orchestrator writes this from the live conversation
   (`session_logs.md`).

### Step 9 — Report & hand off
Report the contract summary: slug, title, venue/template, thesis (one line), the C-ID list with
statuses, the non-goals, the section skeleton (ids + `target_words` + order, total vs. page budget),
seed references, and any open `[NEEDS CLARIFICATION]` markers. Then state the **sign-off gate**:
review `PAPER.md`, resolve any remaining clarifications, then run **`/paper-research`** to begin the
literature deep-dives. **Stop** — no research or drafting in this skill.

## Examples

- `/paper-start a practitioner report on how HPC facilitators should engage with agentic AI` —
  seed the thesis from the sentence, interactively lock the C-IDs / sections / budget, write
  `PAPER.md` (`scoped`) + the `outline/` skeleton, commit `DRAFT: scope paper <slug>`, stop.
- `/paper-start` (no args, no PAPER.md) — begin interactive scoping from a blank slate via
  `AskUserQuestion`.
- `/paper-start status` — if a paper is scoped, print its phase/slug/claims; else say none is
  scoped. No work.
- `/paper-start <anything>` when `PAPER.md` already exists — STOP: refuse to clobber, point at
  `paper_status.py` / `/paper-research`.

## Notes

- One paper is scoped **once**. Re-scoping means editing `PAPER.md`'s body (and mutating FSM state
  with `set_status.py`), not re-running `/paper-start`.
- The `anchors` block stays empty until the first `/paper-draft` seeds it from the live
  `manuscript.tex` (invariants §4) — never invent anchor lines here.
- Leave every claim `proposed` and every `evidence: []` empty. `/paper-research` links evidence and
  `/paper-draft` pass B blindly audits whether the cited evidence actually backs each claim; do not
  upgrade a claim to `supported` to make the FSM look complete (invariants §5, claims.md).
- An unresolved `[NEEDS CLARIFICATION]` marker in `PAPER.md` intentionally **blocks**
  `/paper-research` — resolve what you can with the human now rather than guessing.
- This skill never researches, drafts prose, touches `manuscript.tex`, or ships. Those are
  `/paper-research`, `/paper-outline`, `/paper-draft`, and `/paper-release`.
