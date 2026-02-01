# Session Logging

This document describes the **mandatory requirements** for logging agent interaction sessions.

## Overview

All agent sessions that result in file modifications **must** be logged to `logs/`. These logs provide a record of what was requested, what actions were taken, and the outcomes—essential for understanding project history and reproducing work.

## Log File Requirements

### Filename Format (STRICT)

Use ISO 8601 timestamp format with hyphens, followed by a descriptive slug:
```
YYYY-MM-DDTHH-MM-SS-descriptive-slug.md
```

**Examples:**
- `2026-02-01T02-21-25-first-integration-execution.md`
- `2026-02-01T02-43-34-wip-prefix-correction.md`
- `2026-02-01T01-31-32-release-v0.2.0.md`

**Requirements:**
- Timestamp is UTC (use `date -u +"%Y-%m-%dT%H-%M-%S"`)
- Slug is lowercase, hyphen-separated, descriptive of the session's purpose
- No spaces or underscores in filenames

### File Format

Markdown with YAML frontmatter for structured metadata.

## Template

```markdown
---
timestamp: "2026-02-01T02:21:25Z"
duration_minutes: ~17
user_input: |
  [VERBATIM user input - this is MANDATORY]
  [Include the complete, exact text the user provided]
  [Multi-line input is captured with the YAML | operator]
files_modified:
  - path/to/file1.py
  - path/to/file2.tex
commits:
  - "abc1234: commit message"
  - "def5678: another commit"
related_plans:
  - plans/relevant-plan.md
---

# Descriptive Title

## Summary

[Brief summary of what was accomplished]

## Work Completed

[Detailed description of actions taken, decisions made, and rationale]

## Next Steps

[Any follow-up work or recommendations, if applicable]
```

## Frontmatter Fields

### Required Fields (MANDATORY)

| Field | Description |
|-------|-------------|
| `timestamp` | ISO 8601 timestamp with timezone (e.g., `"2026-02-01T02:21:25Z"`) |
| `user_input` | **MANDATORY** - Verbatim, complete user input using YAML `|` for multi-line |

**CRITICAL**: The `user_input` field must contain the **exact, verbatim text** the user provided. This is non-negotiable. Do not summarize, paraphrase, or omit any part of the user's input.

### Recommended Fields

| Field | Description |
|-------|-------------|
| `duration_minutes` | Approximate session duration (e.g., `~17` or `~5`) |
| `files_modified` | List of files created, modified, or deleted |
| `commits` | List of commits made during the session (hash: message format) |
| `related_plans` | List of planning documents relevant to this session |

### Optional Fields

| Field | Description |
|-------|-------------|
| `tags` | List of relevant tags for categorization |
| `commits_rewritten` | Number of commits rewritten (for rebase/amend sessions) |
| `user_followup` | Additional verbatim follow-up inputs if session spans multiple exchanges |

## Content Guidelines

### User Input (CRITICAL)

The `user_input` frontmatter field is the **most important field** in session logs. It must contain:

1. **The exact, verbatim text** the user provided - no paraphrasing
2. **Complete input** - do not truncate or summarize
3. **Multi-line format** using YAML `|` operator

For sessions with multiple user inputs:
- Use `user_followup` for the second input
- Use `user_followup_2`, `user_followup_3`, etc. for subsequent inputs
- Each must be verbatim

If verbatim input is unavailable (e.g., session recovery), add:
```yaml
user_input_note: "Reconstructed from context - original input unavailable"
```

### Body Content

- **Title**: Descriptive heading matching the filename slug
- **Summary**: Brief overview of what was accomplished
- **Work Completed**: Detailed actions, decisions, and rationale
- **Next Steps**: Follow-up work if applicable (optional)

## When to Log

**DO log:**
- Sessions that create, modify, or delete files
- Multi-step work sessions (single log at the end summarizing the full session)
- Sessions that result in commits

**DO NOT log:**
- Brief Q&A sessions with no file modifications
- Sessions where the user cancels before any work is done
