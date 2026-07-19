# Contribution claims (C-IDs) — the paper's requirement analog

HyperShell threads **R-IDs** (EARS acceptance criteria) as its traceability spine. A paper has no
"requirements" in that sense — it makes **claims**. This file defines the claim convention that gives
a paper the same claim → section → evidence traceability, without the category error of forcing EARS
("When *trigger*, the system shall *response*") onto an assertion.

**We do NOT use EARS here.** A contribution claim is a falsifiable assertion the paper argues for
("proactive engagement is the path forward"), not a triggered behavior. Use plain, declarative
prose.

## Hybrid policy (this project's choice)

Only the **headline claims** — the ones the abstract and introduction stake out, the reasons the
paper exists — get C-IDs. Everything else stays informal `## Key Points` bullets in the outline
section files. Keep the set **small (≈3–5)**; a sprawling claim registry makes
`paper_status.py`'s "claims lacking evidence" report noise, and a 4-page abstract cannot support many
distinct contributions.

## Schema

Claims live in two places, split like everything else in `PAPER.md`:

- **Frontmatter (machine subset, script-owned):** `id`, `status`, `satisfied_by` (section ids),
  `evidence` (bibkeys).
  ```yaml
  claims:
    - {id: C2, status: supported, satisfied_by: [00-abstract, 05-conclusion], evidence: [deelman2025hpc]}
  ```
- **Body (human free-text, verbatim):** the claim `statement` (and optional `kind`), under
  `## Contribution Claims`:
  ```
  - **C2** — Proactive engagement, not prohibition, is the path forward for facilitators. *(thesis)*
  ```

| Field | Where | Meaning |
|-------|-------|---------|
| `id` | frontmatter + body | Stable `C1`, `C2`, … — survives revisions, anchors traceability. |
| `statement` | body | One falsifiable assertion, in plain prose. |
| `kind` | body (optional) | `contribution` \| `framing` \| `assessment` \| `methodology`. |
| `status` | frontmatter | `proposed` (asserted, not yet evidenced) → `supported` (evidence backs it) → `cut`. |
| `satisfied_by` | frontmatter | Section ids that argue the claim. |
| `evidence` | frontmatter | `references.bib` bibkeys (and/or repo artifacts) that back it. |

## What makes a good claim

- **Falsifiable** — a skeptical reader could disagree and you could, in principle, be wrong.
  ("Proactive engagement is the path forward" is arguable; "AI is important" is not.)
- **Scoped** — bounded to what *this* paper (this center, this practice) actually shows. A
  practitioner report claims practice, not a proof.
- **Evidenced** — points at specific sources or repo artifacts, not vibes. `status: supported`
  requires the `evidence` list to genuinely back it (see `invariants.md` §5).
- **One claim per ID** — split compound assertions so each has its own pass/fail and section mapping.

## Anti-patterns

- Untestable superlatives ("revolutionary", "seamless") — state what is actually shown.
- A claim no section argues (`satisfied_by: []`) — either assign it a home or cut it.
- Marking a claim `supported` to make the FSM look complete — honesty over green checkmarks.
- More than ~5 C-IDs on a 4-page paper — demote the rest to informal Key Points.

## How the spine is used

`/paper-start` locks the C-IDs. `/paper-research` tags each source with the C-IDs it supports (into
`evidence`). `/paper-outline` folds that evidence into the `satisfied_by` sections. `/paper-draft`
pass B runs a **blind** claim-support audit: a fresh subagent sees the claims + `references.bib` +
`manuscript.tex` (not the outline) and asks "is each claim actually supported by cited evidence?"
`paper_status.py` reports any C-ID with an empty `evidence` list.
