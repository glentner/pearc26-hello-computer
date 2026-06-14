# AGENTS.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

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

## Agent Workflow Rules

Detailed rules for agent interactions are documented in the `rules/` directory:

- **[rules/wip_commits.md](rules/wip_commits.md)** - WIP commit workflow for incremental development
- **[rules/session_logs.md](rules/session_logs.md)** - Requirements for logging agent sessions to `logs/`
- **[rules/planning_docs.md](rules/planning_docs.md)** - Guidelines for planning documents in `plans/`
- **[rules/structural_docs.md](rules/structural_docs.md)** - Keep structural documents (READMEs, indexes) in sync
- **[rules/file_deletion.md](rules/file_deletion.md)** - Use `del` instead of `rm` for file cleanup

Discoveries about working with agentic tools live in `tips/`:

- **[tips/warp-conversation-history.md](tips/warp-conversation-history.md)** - Recovering verbatim user inputs from Warp's local SQLite store
- **[tips/agent-text-editing-pitfalls.md](tips/agent-text-editing-pitfalls.md)** - Common diff-truncation failure modes during prose edits
- **[tips/long-horizon-tasks.md](tips/long-horizon-tasks.md)** - Structured-memory pattern for multi-session work

### Skills

Project-specific skills live in `.agents/skills/<skill-name>/SKILL.md` and are auto-discovered by Warp.

- **`/release`** — Ship `wip` to `main` (strip `WIP: ` prefixes, fast-forward merge, push, force-push wip). Optional arguments: squash commits, bump version, tag, publish a GitHub release (which triggers the PDF build via CI).
- **`/latex-integration-first-pass`** — Delta-based integration of revised outline prose into `manuscript.tex` (Subphase A)
- **`/latex-integration-second-pass`** — Cold-read fidelity audit comparing outline drafts against integrated `manuscript.tex` (Subphase B)

### Quick Reference

- Work on the `wip` branch; prefix commits with `WIP: `
- Log all sessions that modify files to `logs/` with ISO timestamps
- **ALWAYS** capture verbatim user input in session log frontmatter (`user_input` field)
- Create planning docs in `plans/` for significant features
- Include `Co-Authored-By: Oz <oz-agent@warp.dev>` in commits

## Citation Information

When this work is published, update the BibTeX entry in README.md with actual:
- Author names
- Paper title
- DOI
- Conference proceedings details
