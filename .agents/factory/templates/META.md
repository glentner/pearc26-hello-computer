# META — Paper Harness Feedback ({paper-slug})

> **Harness feedback log** for this paper — the producer artifact of the factory's self-improvement
> loop. Written by the lifecycle skills (`paper-start` / `paper-research` / `paper-outline` /
> `paper-draft` / `paper-review`) when the **skillset itself** costs something; read by `paper-release`
> (surfaced at ship time) and applied by `/paper-harness`. This file is **orthogonal** to the paper
> spine (`PAPER.md` → `outline/` → `manuscript.tex` → `reviews/`) — it is about the *toolchain*, not
> the paper. It lives at the repo root beside `PAPER.md` and is **left behind** when the `.agents/`
> tree is copied to bootstrap a new paper (the `harness-log.md` ledger travels; findings do not).
>
> **Silence is the default.** The bar for a finding is one test: *was this the **skill's** fault — not
> mine, not the task's?* A merely-hard section, a self-inflicted error, or a one-off content issue
> (which belongs in `PAPER.md` **Clarifications**, a `reviews/` note, or a `[NEEDS CLARIFICATION]`
> marker) is **not** a finding. The blind `paper-draft` pass-B claim reviewer never reads this file — it
> would leak author intent and defeat blindness.

- **slug:** {paper-slug}

## What worked well

Brief, optional reinforcement: a part of a skill / the harness that materially helped, so
`/paper-harness` knows what **not** to change. One line each, naming the skill/step. Skip the section
entirely if nothing stands out.

- <what helped, and in which skill/step>

## Friction findings

Zero or more findings, appended below — each a markdown **section** so appending is a low-corruption
operation and a stdlib parser reads them (`python3 .agents/factory/bin/meta_status.py`). Skills always
write `status=open`; only `/paper-harness` flips it. `target` is a best-guess file with **no line
number** (re-derive the exact edit at apply time to avoid staleness). If an equivalent finding already
exists, append "· seen again" to its title instead of duplicating — recurrence is signal, not bloat.

Field enums — `origin`: `paper-<skill>:<step>`; `severity`: `high` (a safety / gate / correctness /
ACM-policy gap) `| medium | low`; `category`: `instruction | steering | tooling | template |
missing-guidance`; `status`: `open` (written by skills) `| applied | rejected | deferred` (written by
`/paper-harness`).

Schema (copy one block per finding, appending it **after** this fence — the fence is illustrative and
is skipped by the parser):

```markdown
## F1 — <one-line title of the skillset problem>
`origin=paper-<skill>:<step> severity=<high|medium|low> category=<instruction|steering|tooling|template|missing-guidance> status=open target=<best-guess file>`
- **What happened:** <what the skill made you do, or fail to do>.
- **Skill cause:** <why this is the instructions' fault — not yours, not the task's>.
- **Recommended fix:** <the concrete change to the skill / template / script>.
- **Confidence:** <high|med|low> · **Effort:** <small|medium|large>
```

<!-- Real findings are appended below this line by the lifecycle skills. -->
