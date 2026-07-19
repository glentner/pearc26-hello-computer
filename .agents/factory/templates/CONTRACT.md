---
slug: {paper-slug}
title: "{Full Paper Title}"
venue: {PEARC26}
template: "{acmart sigconf}"
macro_phase: scoped
base: main
branch: draft
last_updated: {YYYY-MM-DD}
sections:
  - {id: 00-abstract, status: draft, satisfies: [C1], target_words: 150, order: 6}
  - {id: 01-introduction, status: draft, satisfies: [C1, C2], target_words: 400, order: 4}
  - {id: 02-background, status: draft, satisfies: [], target_words: 300, order: 1}
  - {id: 03-approach, status: draft, satisfies: [C3], target_words: 500, order: 2}
  - {id: 04-discussion, status: draft, satisfies: [], target_words: 600, order: 3}
  - {id: 05-conclusion, status: draft, satisfies: [C2], target_words: 200, order: 5}
  - {id: 06-acks, status: draft, satisfies: [], target_words: 80, order: 7}
claims:
  - {id: C1, status: proposed, satisfied_by: [00-abstract, 01-introduction], evidence: []}
  - {id: C2, status: proposed, satisfied_by: [01-introduction, 05-conclusion], evidence: []}
  - {id: C3, status: proposed, satisfied_by: [03-approach], evidence: []}
review: {cycle: 0, verdict: none}
---

# {Full Paper Title} — Paper Contract

> **This is the paper's contract and finite-state machine** (the GOAL analog). The **frontmatter
> above** is the machine-owned FSM — read it with `python3 .agents/factory/bin/paper_status.py`,
> mutate it with `set_status.py`, **never hand-edit** the frontmatter (add a section/claim with
> `set_status.py --add-section` / `--add-claim`, never by hand). **This body** is the human-editable
> contract, preserved verbatim by the scripts. Written by `/paper-start`; keep it at the right
> altitude — solved and bounded, but leaving drafting freedom.
>
> Two frontmatter fields are added by scripts *during* the lifecycle and are absent at scoping: a
> section's `attempts` (the durable draft↔audit circuit breaker, via `set_status.py --record-attempt`;
> `paper_status.py` warns at ≥3) and `review.reviewed_commit` (the commit the last `/paper-draft`
> pass-B audit graded, via `--reviewed-commit`; `/paper-release` gates on it being current).

## Thesis

<The single argument this paper makes, in two or three sentences. What do you want the reader to
believe or do afterward? Motivate it; do not yet describe every section.>

## Contribution Claims

Stable `C1`, `C2`, … per `.agents/factory/claims.md` (plain assertions, NOT EARS). Hybrid policy:
only the headline abstract/intro claims get C-IDs; keep the set to ≈3–5. Each id here must match a
`claims:` entry in the frontmatter (`satisfied_by` sections, `evidence` bibkeys).

- **C1** — <falsifiable headline claim>. *(framing | contribution | assessment | methodology)*
- **C2** — <the thesis, as one assertion>.
- **C3** — <the concrete contribution this paper reports>.

## Non-goals

Explicit exclusions that keep scope bounded to the page budget. Naming what the paper is **not**
doing is as important as what it is.

- <thing deliberately out of scope>
- <boundary a reviewer might otherwise expect you to cover>

## Clarifications

Questions resolved with the human during scoping. Unresolved ones stay marked
`[NEEDS CLARIFICATION: …]` and **block** `/paper-research` — never guess.

- **Q:** <question> — **A:** <answer> (resolved YYYY-MM-DD).

## Section → LaTeX anchor map

Machine-read by `paper_status.py` (verifies each anchor occurs in `manuscript.tex`) and by
`/paper-draft` (the heading map for outline→LaTeX integration). **Seed from the live `manuscript.tex`
once it exists**, never from a remembered map. One `id | \anchor` per line; a section with multiple
headings gets multiple lines; `00-abstract`/`06-acks` are environments, not `\section`s. (On a brand
new paper this may be empty until the first `/paper-draft` run seeds it.)

```anchors
00-abstract | \begin{abstract}
01-introduction | \section{{Introduction}}
02-background | \section{{Background}}
03-approach | \section{{Approach}}
04-discussion | \section{{Discussion}}
05-conclusion | \section{{Conclusion}}
06-acks | \begin{acks}
```

## Venue & build notes

- **Venue:** <ACM PEARC '26 extended abstract, hard N-page limit — `make check`>.
- **Template:** <`acmart` class/mode; rights; where AI use is disclosed>.
- **Seed references / prior work:** <bibkeys or leads for `/paper-research` to deep-dive>.
- **Source of truth:** `outline/0N-*.md` `## Draft` → integrated into `manuscript.tex` by
  `/paper-draft`; `references.bib` holds all sources.
