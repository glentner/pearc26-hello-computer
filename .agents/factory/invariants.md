# Paper-invariants gate & checklist

A curated, enumerated checklist of the load-bearing conventions for this paper — the research analog
of HyperShell's code footgun list. It replaces software invariants (task lifecycle, exit codes) with
**venue, format, prose, and citation** invariants. Three consumers:

- **`/paper-draft` pass B** — the fidelity/claim/citation audit grades the integrated
  `manuscript.tex` against the relevant sections here; a violation is a finding.
- **`/paper-review`** — when distilling external feedback, map each item to the invariant it touches.
- **`check_paper.py` (`make check`)** — the ✅ items below are checked deterministically; the 🧐 items
  need a cold read.

Only invoke the sections relevant to the change. Consult `AGENTS.md` (the constitution) for anything
not enumerated here; keep this file in lockstep with it.

## 1. Venue & format (highest blast radius — a rejection risk)

- 🧐 **Page budget is hard.** PEARC '26 extended abstract: **4 pages** including references.
  Scope is cuttable to fit (methodology principle 5). `make check` reports the current page count.
- 🧐 **Document class / mode.** `acmart`; camera-ready uses `\documentclass[sigconf]`. Do not switch
  class or add packages that break the ACM template without a reason recorded in `PAPER.md`.
- 🧐 **Rights.** `\setcopyright{cc}` + `\setcctype{by}` (CC-BY). After acceptance, the
  `\acmDOI`/`\acmISBN`/`\copyrightyear` come from the ACM rights email — do not invent values.
- ✅ **Generative-AI disclosure is mandatory and must be current.** ACM policy requires disclosing AI
  use in `\begin{acks}`. It must name the *actual* tools/models and harness used. `check_paper.py`
  flags a disclosure that names a superseded harness (e.g. "Warp" after migrating to Claude Code) —
  it does **not** auto-edit the manuscript; the authors update it.

## 2. LaTeX prose conventions (the `/paper-draft` integration contract)

These are the conventions the two legacy `latex-integration-*` skills encoded; `/paper-draft`
enforces them, and `check_paper.py` catches the grep-able ones.

- ✅ **No raw em-dashes.** This project uses commas or reworded clauses, never `---`. (En-dashes `--`
  in ranges like `July 26--30` are fine.) Reviewer feedback FB-1.02 was literally em-dash overuse —
  agents overuse them, so this is checked.
- ✅ **Quotes:** LaTeX double quotes ``` ``...'' ``` , never straight `"..."`.
- 🧐 **Emphasis / code:** `\emph{...}` for italics (markdown `*...*`); `\texttt{...}` for inline
  code/commands (markdown `` `...` ``).
- 🧐 **Non-breaking spaces:** `~` where a break would read badly (e.g. `2~AM`, `Fig.~1`, `Vaswani et
  al.~\cite{...}`).
- 🧐 **Line wrapping:** match the manuscript's existing convention (~80 chars); wrap by hand.

## 3. Citation integrity (deterministic)

- ✅ **Every `\cite` resolves.** Every key cited in `manuscript.tex` must have an entry in
  `references.bib` (a dangling cite is an ERROR in `check_paper.py`).
- ✅ **No orphan entries.** A `references.bib` entry that is never cited is a WARNING (either cite it
  or cut it — it does not appear in the rendered bibliography anyway).
- 🧐 **Every non-obvious claim is cited.** Empirical or historical assertions carry a citation;
  contribution claims (C-IDs) list their `evidence:` bibkeys in `PAPER.md`. `paper_status.py` reports
  C-IDs lacking evidence.
- ⚠️ **Do NOT trust the outline `citations:` frontmatter** as ground truth — it is present in only
  some section files. The `manuscript.tex` + `references.bib` pair is authoritative.

## 4. Structural fidelity (outline ↔ manuscript)

- 🧐 **The outline `## Draft` blocks are the source of truth; `manuscript.tex` is derived.** After
  `/paper-draft`, no prose should exist in the tex that isn't in the outline (or vice versa) — that
  is exactly what pass B's cold read verifies.
- ✅ **Heading map accuracy.** The `PAPER.md` `anchors` block maps each section to its exact
  `manuscript.tex` heading command(s); `paper_status.py` warns if an anchor no longer occurs in the
  tex. Seed anchors from the *live* manuscript, never from the deprecated `latex-integration-*` map.
- 🧐 **Section status truth.** A section marked `integrated` in `PAPER.md` must actually be reflected
  in the tex; `set_status.py` keeps the outline file's `status:` in sync (no drift).

## 5. Reproducibility & honesty

- 🧐 **Numbers are real.** Any statistic ("over one hundred commits", "thirteen-source bibliography",
  "3.5 days on 8 GPUs") must be verifiable from the repo or the cited source. No invented figures.
- 🧐 **Claims match evidence.** A C-ID marked `supported` must have its `evidence:` bibkeys actually
  back it; `proposed` is the honest state until then. Do not upgrade a claim to `supported` to make
  the FSM look complete.
- 🧐 **The public repo link and process artifacts** referenced in the paper (claim C5) must exist and
  be accurate — the meta-demonstration is only a contribution if it is real.
