# Structural Documentation

This document describes the requirement to keep high-level structural documents synchronized with their contents.

## Overview

When modifying files within a directory that has a structural document (like `README.md` or an index file), the structural document must be updated to reflect any relevant changes.

## Structural Documents

| Directory | Structural Document | Purpose |
|-----------|---------------------|---------|
| `outline/` | `outline/README.md` | Documents the outline workflow and lists section files |
| `outline/notes/` | (referenced in `outline/README.md`) | Research notes and supporting material |
| `outline/snippets/` | (referenced in `outline/README.md`) | Draft text fragments |
| `rules/` | `AGENTS.md` | Agent workflow rules index |
| `tips/` | `AGENTS.md` | Agentic tool discoveries index |
| `plans/` | (referenced in session logs) | Planning documents |

## When to Update

Update the relevant structural document when:

- **Adding files**: Add new entries to indexes, lists, or references
- **Removing files**: Remove stale references
- **Renaming files**: Update all references to use new names
- **Changing scope**: Update descriptions if a file's purpose changes significantly
- **Adding key findings**: Summarize important discoveries in appropriate overview sections

## What to Update

For `outline/README.md` specifically:

- Section file list and descriptions
- Notes file list in the `outline/notes/` section
- Snippets list in the `outline/snippets/` section
- Any cross-references between sections

For `AGENTS.md`:

- Repository structure listing
- Agent workflow rules links
- Quick reference section if workflows change

## Verification

Before committing changes to a directory with structural docs, verify:

1. All new files are referenced appropriately
2. No broken references to removed/renamed files
3. Descriptions remain accurate
4. The structural document still provides a useful overview
