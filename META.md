# META — Paper Harness Feedback (hello-computer)

> **Harness feedback log** for this paper — the producer artifact of the factory's self-improvement
> loop. Written by the lifecycle skills (`paper-start` / `paper-research` / `paper-outline` /
> `paper-draft` / `paper-review`) when the **skillset itself** costs something; read by `paper-release`
> (surfaced at ship time) and applied by `/paper-harness`. Orthogonal to the paper spine (`PAPER.md` →
> `outline/` → `manuscript.tex` → `reviews/`) — it is about the *toolchain*, not the paper. Left behind
> when the `.agents/` tree is copied to a new paper (the `harness-log.md` ledger travels; findings do
> not).
>
> **Silence is the default.** The bar for a finding is one test: *was this the **skill's** fault — not
> mine, not the task's?* A one-off content issue belongs in `PAPER.md` **Clarifications**, a `reviews/`
> note, or a `[NEEDS CLARIFICATION]` marker — not here. The blind `paper-draft` pass-B claim reviewer
> never reads this file.

- **slug:** hello-computer

## What worked well

- The single-authoritative `PAPER.md` + `set_status.py` (with the targeted outline `status:` sync) made
  the retrofit drift-free on the first try — `paper_status.py` reported zero drift/anchor warnings
  against the live `manuscript.tex`. Do not re-introduce a second source of section status.
- Seeding the `anchors` block from the live `manuscript.tex` (not a remembered map) caught the
  `\subsection` vs `\paragraph` and `(Caution)` vs `(Cautionary Notes)` realities immediately.

## Friction findings

<!-- Real findings are appended below this line by the lifecycle skills. -->

## F1 — The meta-note step is duplicated verbatim across the five producer skills
`origin=paper-outline:meta-note severity=low category=template status=open target=.agents/factory/methodology.md`
- **What happened:** wiring the self-improvement loop meant copy-pasting the same ~12-line "Meta-note (silence by default)" step into `paper-start`, `paper-research`, `paper-outline`, `paper-draft`, and `paper-review`; a future wording change must be made in five places or they drift.
- **Skill cause:** the factory has no shared-snippet mechanism, so a cross-skill step can only be duplicated, not referenced — a template/tooling gap, not an authoring mistake.
- **Recommended fix:** factor the canonical meta-note step into one place (e.g. a `## Meta-note` section in `methodology.md`, or a `templates/meta-note.md` snippet) that each skill links to in one line, instead of inlining the full step. Low urgency; five copies are tolerable for now.
- **Confidence:** high · **Effort:** small
