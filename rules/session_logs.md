# Session Logging

This document describes the requirements for logging agent interaction sessions.

## Overview

All agent sessions that result in file modifications must be logged to `logs/`. These logs provide a record of what was requested, what actions were taken, and the outcomes—useful for understanding project history and reproducing work.

## Log File Requirements

### Filename Format

Use ISO 8601 timestamp format with hyphens (filesystem-safe):
```
YYYY-MM-DDTHH-MM-SS.md
```

Example: `2026-01-31T19-16-25.md`

### File Format

Markdown with YAML frontmatter for structured metadata.

## Template

```markdown
---
timestamp: "2026-01-31T19:16:25Z"
session_type: "feature"
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

## Frontmatter Fields

### Required Fields

| Field | Description |
|-------|-------------|
| `timestamp` | ISO 8601 timestamp with timezone (e.g., `"2026-01-31T19:16:25Z"`) |
| `session_type` | One of: `feature`, `bugfix`, `refactor`, `documentation`, `exploration` |
| `summary` | Brief one-line description of the session outcome |

### Optional Fields

| Field | Description |
|-------|-------------|
| `files_modified` | List of files created, modified, or deleted |
| `related_plans` | List of planning documents relevant to this session |
| `user_input` | Verbatim user input (multi-line YAML string with `\|`) |
| `user_followup` | Additional verbatim follow-up inputs if session spans multiple exchanges |

## Session Types

- **feature**: Adding new functionality or capabilities
- **bugfix**: Fixing errors or incorrect behavior
- **refactor**: Restructuring code without changing functionality
- **documentation**: Updating docs, comments, or metadata
- **exploration**: Investigating, researching, or prototyping

## Content Guidelines

### User Input Section

- Include the user's request verbatim if brief
- Summarize longer or multi-part requests
- Capture the intent and any specific requirements mentioned

### Agent Actions Section

- List actions in chronological order
- Explain reasoning for non-obvious decisions
- Note any alternatives considered and why they were rejected

### Outcome Section

- State what was accomplished clearly
- Document any issues encountered or limitations
- Include next steps if the work is incomplete or follow-up is needed

## When to Log

**DO log:**
- Sessions that create, modify, or delete files
- Multi-step work sessions (single log at the end summarizing the full session)
- Sessions that result in commits

**DO NOT log:**
- Brief Q&A sessions with no file modifications
- Sessions where the user cancels before any work is done
