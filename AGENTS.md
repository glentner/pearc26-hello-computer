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

**Current State**: The repository is in early setup phase with only template files present. The manuscript is currently at root level rather than in a subdirectory.

## Building the Manuscript

The manuscript uses the ACM `acmart` document class for conference submissions.

### Build Commands

```bash
# Build PDF using pdflatex (basic build)
pdflatex manuscript.tex

# Build with bibliography (if .bib file exists)
pdflatex manuscript.tex
bibtex manuscript
pdflatex manuscript.tex
pdflatex manuscript.tex

# Recommended: Use latexmk for automatic dependency handling
latexmk -pdf manuscript.tex

# Clean auxiliary files
latexmk -c manuscript.tex

# Clean all generated files including PDF
latexmk -C manuscript.tex
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

## Agent Documentation Requirements

### Planning Documents

When working on significant features or tasks that require planning, store planning documents in `plans/`:
- Use descriptive filenames (e.g., `experiment-design.md`, `data-pipeline-refactor.md`)
- Format as Markdown
- Include context, goals, approach, and any decisions made
- Update plans as understanding evolves during implementation

### Session Logs

All agent sessions must be logged to `logs/` with the following requirements:
- **Filename**: ISO 8601 timestamp format: `YYYY-MM-DDTHH-MM-SS.md` (e.g., `2026-01-31T19-16-25.md`)
- **Format**: Markdown with YAML frontmatter for metadata

**Log file template**:

```markdown
---
timestamp: "2026-01-31T19:16:25Z"
session_type: "feature" | "bugfix" | "refactor" | "documentation" | "exploration"
summary: "Brief description of what was accomplished"
files_modified:
  - path/to/file1.py
  - path/to/file2.tex
related_plans:
  - plans/relevant-plan.md
---

# Session Log

## User Input

[Verbatim or summarized user requests]

## Agent Actions

[Summary of actions taken, decisions made, and rationale]

## Outcome

[What was accomplished, any issues encountered, next steps if applicable]
```

### When to Log

- Log every interactive session that results in file modifications
- For multi-step work sessions, create a single log entry at the end summarizing the full session
- Brief Q&A sessions that don't modify files may be omitted

## Citation Information

When this work is published, update the BibTeX entry in README.md with actual:
- Author names
- Paper title
- DOI
- Conference proceedings details
