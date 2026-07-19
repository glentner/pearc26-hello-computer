# AGENTS.md

This file provides guidance to AI coding agents working in this repository. It is harness-neutral:
the project now uses **Claude Code** (which reads this file via the `CLAUDE.md → AGENTS.md` symlink and
discovers skills/settings via `.claude → .agents`); earlier history was produced with WARP (warp.dev).

## Project Overview

This is an ACM conference paper replication package repository for PEARC'26. The repository follows a dual-license structure:
- **MIT License** for all code and data (`LICENSE_MIT`)
- **CC BY 4.0** for manuscript content (`LICENSE_CC-BY-4.0`)

The manuscript is intended as the Author's Accepted Manuscript (AAM) version, suitable for self-archiving even if the final publication has exclusive ACM licensing.

## Repository Structure

Manuscript and supporting material:
- `manuscript.tex` - The paper itself (ACM `acmart`, single source file at root)
- `references.bib` - Bibliography
- `Makefile`, `.latexmkrc` - Build system (see Build Commands below)
- `outline/` - Section drafts (`00-abstract.md` through `05-conclusion.md`), research notes, and reusable snippets; the day-to-day working directory before integration into `manuscript.tex`
- `reviews/` - Multi-phase review documents produced during revision

Process and history:
- `plans/` - Planning documents for significant features or revisions
- `logs/` - Session logs from agent interactions, ISO-timestamped
- `rules/` - Long-form prose describing project conventions (linked from this file)
- `tips/` - Discoveries about working with agentic tools

Harness configuration:
- `.agents/skills/` - Project-scoped skills (the only directory in the repo with harness-aware semantics)
- `.github/` - GitHub workflows, including `release_pdf.yml` for release-triggered PDF builds

Build output:
- `build/` - LaTeX build artifacts (gitignored)
- `lentner-2026-*.pdf` - Release PDFs (gitignored; attached to GitHub releases)
- `pearc26-*.zip` - ACM TAPS camera-ready upload package (gitignored; produced by `make upload`)

## Building the Manuscript

The manuscript uses the ACM `acmart` document class for conference submissions.
Build artifacts are isolated in the `build/` directory.

### Build Commands

```bash
# Incremental build (default)
make build

# Full clean rebuild with release PDF (lentner-2026-{version}.pdf)
make release

# Camera-ready: build release, then package PDF + source as pearc26-36.zip for ACM TAPS
make upload

# Continuous build with file watching (for live editing)
make watch

# Open PDF in Skim
make open

# Clean build artifacts
make clean

# Clean everything including release PDFs
make distclean
```

### Manuscript Configuration

The manuscript is configured with:
- Document class: `acmart` with `[manuscript, screen, authorversion]` options
- This is the **author version** suitable for self-archiving
- Conference: PEARC'26 (June 2026)
- Copyright year: 2026

## Development Workflow

The manuscript is developed as an outline-first markdown drafting loop, with periodic integration into `manuscript.tex`:

1. **Draft in `outline/`**. Each section (`00-abstract.md` through `05-conclusion.md`) is a markdown file with frontmatter (`status`, `target_words`) and a `## Draft` block holding the working prose. Notes and reusable fragments live in `outline/notes/` and `outline/snippets/`.
2. **Iterate freely**. Markdown avoids LaTeX friction during prose work. Section files keep their `status` field (`draft` → `review` → `integrated`) so the integration step can act on deltas only.
3. **Plan revisions in `plans/`**. Significant revision passes get a planning document (see `rules/planning_docs.md`).
4. **Integrate with the LaTeX skills**. Use `/latex-integration-first-pass` to apply outline deltas to `manuscript.tex` (Subphase A), then `/latex-integration-second-pass` for a cold-read fidelity audit (Subphase B). The two-pass split avoids self-confirming errors from a single agent.
5. **Build and verify**. `make build` produces `build/manuscript.pdf`; `make watch` rebuilds on save during heavy editing.
6. **Ship**. Run `/release` to ship `wip` to `main`: strip `WIP: ` prefixes, fast-forward merge, push, force-push wip. Pass arguments (e.g. `/release minor version bump with tag and release`) to also bump the version, tag, and publish a GitHub release (which triggers `release_pdf.yml` to build and attach the versioned PDF).

Session logs in `logs/` and planning documents in `plans/` capture the trail of *why* changes were made; the manuscript itself is the *what*.

## The Paper Factory (`/paper-*` lifecycle)

The ad-hoc workflow above is now formalized as a portable, reusable toolkit under `.agents/` — the
"paper factory", adapted from the HyperShell software-factory pattern. **Read
[`.agents/factory/methodology.md`](.agents/factory/methodology.md) for the full rationale**, or
[`.agents/factory/getting-started.md`](.agents/factory/getting-started.md) for a narrative, end-to-end
walkthrough (written for the research community, not just implementers). It is the recommended way to
work on this paper and to bootstrap the next one (copy the `.agents/` tree).

**State machine.** The repo-root `PAPER.md` holds this paper's contract (thesis, contribution claims,
non-goals, the section→LaTeX anchor map) plus the finite-state machine (macro-phase + per-section
status + claims). The FSM is **script-owned — never hand-edit `PAPER.md` frontmatter**:

- `python3 .agents/factory/bin/paper_status.py PAPER.md` — read the state (JSON): section status
  buckets, claims lacking evidence, refs/feedback counts, anchor drift, completion predicates. Run it
  first in any session.
- `python3 .agents/factory/bin/set_status.py PAPER.md …` — advance state (sections, claims, macro-phase,
  review) and keep the outline files' `status:` in sync. `--help` for flags.
- `make check` (`python3 .agents/factory/bin/check_paper.py`) — deterministic linters: citation
  integrity, prose conventions (no raw `---`, `` ``…'' ``), and page/word budget.

**The lifecycle** (macro-phase: `scoped → researching → outlining → integrating → in-review →
revising → released`, cyclic): `/paper-start` (scope a new paper) → `/paper-research` (deep-dive one
source) → `/paper-outline` (fold evidence into a section's `## Draft`) → `/paper-draft` (integrate
outline → `manuscript.tex`, two passes) → `/paper-review` (ingest external peer feedback, loop back) →
`/paper-release` (ship `draft → main`). Reference material and artifact templates live in
`.agents/factory/{methodology,invariants,claims,review-rubric}.md` and `.agents/factory/templates/`.

The `PAPER.md` in this repo was **retrofitted** onto the finished v1.0.1 paper as a worked example
(all sections `integrated`, `macro_phase: released`).

**Self-improvement loop.** The factory improves itself the same way it writes the paper. The five
producer skills append silence-by-default `## F<n>` findings to a repo-root `META.md` when the
*skillset itself* costs something; `python3 .agents/factory/bin/meta_status.py` reads them; `/paper-release`
surfaces open findings at ship time (non-blocking); and the human-gated **`/paper-harness`** applier —
the only skill that writes `.agents/` — previews and applies each fix as an atomic `[harness]` commit on
`draft`, recording every decision in `.agents/factory/harness-log.md` (the ledger, which *travels* to the
next paper; `META.md` is left behind). `/paper-harness` never touches `PAPER.md`'s FSM or
`manuscript.tex`, and never weakens an invariant. See methodology.md ("The self-improvement loop").

## Agent Workflow Rules

Detailed rules for agent interactions are documented in the `rules/` directory:

- **[rules/draft_commits.md](rules/draft_commits.md)** - DRAFT commit workflow for incremental development
- **[rules/session_logs.md](rules/session_logs.md)** - Requirements for logging agent sessions to `logs/`
- **[rules/planning_docs.md](rules/planning_docs.md)** - Guidelines for planning documents in `plans/`
- **[rules/structural_docs.md](rules/structural_docs.md)** - Keep structural documents (READMEs, indexes) in sync
- **[rules/file_deletion.md](rules/file_deletion.md)** - File cleanup (under Claude Code, use `/bin/rm` as the Makefile does; `del` was a Warp-only alias)

Discoveries about working with agentic tools live in `tips/`:

- **[tips/warp-conversation-history.md](tips/warp-conversation-history.md)** - Recovering verbatim user inputs from Warp's local SQLite store
- **[tips/agent-text-editing-pitfalls.md](tips/agent-text-editing-pitfalls.md)** - Common diff-truncation failure modes during prose edits
- **[tips/long-horizon-tasks.md](tips/long-horizon-tasks.md)** - Structured-memory pattern for multi-session work

### Skills

Project-specific skills live in `.agents/skills/<skill-name>/SKILL.md` and are auto-discovered via the
`.claude → .agents` symlink.

**The paper factory (`/paper-*`) — the current lifecycle:**

- **`/paper-start`** — Scope a NEW paper: venue/template, thesis, contribution claims, non-goals,
  seed references, section skeleton. Creates `PAPER.md` + the `outline/` scaffold.
- **`/paper-research`** — Deep-dive one source at a time; writes `outline/notes/refs/<bibkey>.md`, a
  `references.bib` entry, and links the source to the claims it supports.
- **`/paper-outline`** — Fold research into a section's `## Draft` prose; advances `draft → review`.
- **`/paper-draft`** — Integrate the outline into `manuscript.tex` (Pass A) then verify with a fresh
  subagent (Pass B: cold-read fidelity + blind claim/citation audit); advances `review → integrated`.
- **`/paper-review`** — Ingest external peer feedback (transcript/email): capture → distill `FB-N.NN`
  → synthesize → write a revision plan; loops the paper back to `revising`.
- **`/paper-release`** — Ship `draft → main` with a RELEASE GUARD (`make build` + `make check` +
  `paper_status.py` readiness); optional bump/tag/GitHub-release + ACM TAPS packaging.

**Meta / maintenance (not a lifecycle phase):**

- **`/paper-harness`** — Apply the self-improvement loop: turn the `META.md` friction findings the
  lifecycle skills logged into human-gated `[harness]` fixes to `.agents/` (skills, templates, scripts,
  factory docs), one atomic commit each, recorded in `.agents/factory/harness-log.md`. The only skill
  that writes `.agents/`; never touches the paper or the FSM; never weakens an invariant.

**Legacy skills (superseded, retained for history, `disable-model-invocation: true`):**

- **`/release`** → use **`/paper-release`** (adds the release guard + `macro_phase` transition).
- **`/latex-integration-first-pass`** / **`/latex-integration-second-pass`** → use **`/paper-draft`**
  (Pass A / Pass B); the hard-coded heading map is replaced by the `PAPER.md` anchor block.

### Quick Reference

- Work on the `draft` branch; prefix commits with `DRAFT: ` (the convention renamed from `wip`/`WIP:`; see `rules/draft_commits.md`)
- Log all sessions that modify files to `logs/` with ISO timestamps
- **ALWAYS** capture verbatim user input in session log frontmatter (`user_input` field)
- Create planning docs in `plans/` for significant features
- Co-author trailer: under Claude Code use `Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>` (the configurable current-harness identity; historical commits used `Oz <oz-agent@warp.dev>` — not rewritten). See `rules/draft_commits.md`.
- Use the paper factory: run `python3 .agents/factory/bin/paper_status.py PAPER.md` first, then a `/paper-*` skill (see "The Paper Factory" above)

## Citation Information

When this work is published, update the BibTeX entry in README.md with actual:
- Author names
- Paper title
- DOI
- Conference proceedings details
