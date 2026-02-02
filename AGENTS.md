# AGENTS.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

This is an ACM conference paper replication package repository for PEARC'26. The repository follows a dual-license structure:
- **MIT License** for all code and data (`LICENSE_MIT`)
- **CC BY 4.0** for manuscript content (`LICENSE_CC-BY-4.0`)

The manuscript is intended as the Author's Accepted Manuscript (AAM) version, suitable for self-archiving even if the final publication has exclusive ACM licensing.

## Repository Structure

Per the README, the intended structure is:
- `src/` - Source code for experiments (not yet created)
- `data/` - Raw and processed datasets (not yet created)
- `manuscript/` - LaTeX source files for the paper (currently `manuscript.tex` is at root)
- `figures/` - Generated plots and diagrams (not yet created)
- `plans/` - Planning documents from agent sessions
- `logs/` - Session logs from agent interactions
- `rules/` - Detailed workflow and documentation rules
- `tips/` - Discoveries and recommendations for working with agentic tools

**Current State**: The repository is in early setup phase with only template files present. The manuscript is currently at root level rather than in a subdirectory.

## Building the Manuscript

The manuscript uses the ACM `acmart` document class for conference submissions.
Build artifacts are isolated in the `build/` directory.

### Build Commands

```bash
# Incremental build (default)
make build

# Full clean rebuild with release PDF (lentner-2026-{version}.pdf)
make release

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

When adding experiments or code:
1. Create source code in `src/` directory
2. Place datasets in `data/` directory
3. Generate figures/plots to `figures/` directory
4. Reference figures and results in `manuscript.tex`
5. If the manuscript grows, consider splitting into multiple `.tex` files in a `manuscript/` subdirectory

## Agent Workflow Rules

Detailed rules for agent interactions are documented in the `rules/` directory:

- **[rules/wip_commits.md](rules/wip_commits.md)** - WIP commit workflow for incremental development
- **[rules/session_logs.md](rules/session_logs.md)** - Requirements for logging agent sessions to `logs/`
- **[rules/planning_docs.md](rules/planning_docs.md)** - Guidelines for planning documents in `plans/`
- **[rules/structural_docs.md](rules/structural_docs.md)** - Keep structural documents (READMEs, indexes) in sync
- **[rules/file_deletion.md](rules/file_deletion.md)** - Use `del` instead of `rm` for file cleanup
- **[tips/](tips/)** - Discoveries about agentic tools (see `tips/warp-conversation-history.md`)

### Stored Prompts

- **`/release`** - Create a GitHub release from `main` branch (triggers PDF build via CI)

### Quick Reference

- Work on the `wip` branch; prefix commits with `WIP: `
- Log all sessions that modify files to `logs/` with ISO timestamps
- **ALWAYS** capture verbatim user input in session log frontmatter (`user_input` field)
- Create planning docs in `plans/` for significant features
- Include `Co-Authored-By: Warp <agent@warp.dev>` in commits

## Citation Information

When this work is published, update the BibTeX entry in README.md with actual:
- Author names
- Paper title
- DOI
- Conference proceedings details
