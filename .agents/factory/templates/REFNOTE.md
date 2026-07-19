<!--
  REFNOTE template — a per-source literature deep-dive note (one file per bibkey).
  Filled by /paper-research and written to outline/notes/refs/<bibkey>.md; the matching
  entry in outline/notes/refs/README.md flips [ ] -> [x] and references.bib gets the source.
  Replace every {placeholder}; delete the optional sections that don't apply. The frontmatter
  is human/skill-authored free text (NOT the machine FSM) — the C-IDs in `supports:` and in
  set_status.py --claim <id> --add-evidence <bibkey> must name the same claim/source so the
  claim's `evidence` list in PAPER.md stays in sync. See ../methodology.md and ../claims.md.
-->
---
bibkey: "{bibkey}"
title: "{Full Source Title}"
authors: "{First Last, First Last, …}"
year: {YYYY}
source_type: "{paper|book|report|standard|blog|dataset|software|web}"
url: "{https://…}"
venue: "{Journal / Conference / Publisher, or n/a}"
status: "complete"
supports: [{C1, C2}]
key_findings:
  - "{One-line finding this source establishes, in your words}"
  - "{Another finding — keep each atomic and citable}"
  - "{…}"
sample_sentences: |
  {One or two ready-to-paste sentences that cite this source the way the paper would use it,
  e.g. "Foo et al. (YYYY) show that …", so drafting can lift prose without re-reading the source.
  Attribute explicitly; keep to what the source actually supports.}
---

# {Full Source Title}

## Overview

{Two to four sentences: what this source is, who wrote it and where/when it appeared, and its
one-sentence thesis. Orient a reader who has never seen it.}

## Key Ideas / The Problem

{What problem does the source tackle, and what is its central idea, method, or argument?
Use subsections or a numbered list for the load-bearing points. This is the substance a
drafting pass will draw on — be specific, not a paraphrase of the abstract.}

## Results & Impact

{The concrete outcomes: findings, numbers, benchmarks, or conclusions, and how the field
received them. Include the figures that matter to our argument; cite them precisely.}

## Why This Matters for Our Paper

{The tie-back. For each C-ID in `supports:` above, state in one line how this source backs that
claim — the sentence a reviewer would want when they see `evidence: [{bibkey}]` on the claim.}

- **{C1}** — {how this source supports C1}.
- **{C2}** — {how this source supports C2}.

<!-- Optional — delete if not useful for this source. -->
## Citation Statistics

{Citation count / influence, adoption, or standing in the literature, with the as-of date.}

<!-- Optional — delete if not useful for this source. -->
## Trivia

- {Memorable detail, backstory, or naming note that colors the source.}
