# Planning Documents

This document describes the requirements for creating and maintaining planning documents.

## Overview

When working on significant features or tasks that require planning, store planning documents in `plans/`. These documents capture the design thinking, decisions, and approach before and during implementation.

## When to Create a Plan

Create a planning document when:

- Building new functionality that spans multiple files or components
- Making architectural decisions that affect the project structure
- The task is complex enough that implementation approach isn't obvious
- Multiple viable approaches exist and trade-offs need to be documented
- The work will span multiple sessions

## File Requirements

### Filename Format

Use descriptive, kebab-case filenames:
```
<topic>-<aspect>.md
```

Examples:
- `experiment-design.md`
- `data-pipeline-refactor.md`
- `api-integration-approach.md`
- `performance-optimization.md`

### File Format

Markdown with optional YAML frontmatter for metadata.

## Template

```markdown
---
created: "2026-01-31"
status: "in-progress"
---

# Plan Title

## Context

[Background information and why this work is needed]

## Goals

[What success looks like - specific, measurable if possible]

## Current State

[Relevant existing code, systems, or constraints]

## Proposed Approach

[Detailed description of the implementation plan]

### Option 1: [Name]

[Description, pros, cons]

### Option 2: [Name]

[Description, pros, cons]

## Decision

[Which approach was chosen and why]

## Implementation Notes

[Details discovered during implementation, gotchas, etc.]

## Open Questions

- [ ] Question 1
- [ ] Question 2
```

## Frontmatter Fields (Optional)

| Field | Description |
|-------|-------------|
| `created` | Date the plan was created (YYYY-MM-DD) |
| `status` | One of: `draft`, `in-progress`, `completed`, `abandoned` |
| `related_logs` | List of session logs related to this plan |

## Content Guidelines

### Context Section

- Explain the problem or opportunity
- Reference any external requirements (issues, tickets, discussions)
- Keep it brief—just enough for someone to understand why this work matters

### Goals Section

- Be specific about what "done" looks like
- Include acceptance criteria if applicable
- Distinguish between must-have and nice-to-have outcomes

### Proposed Approach Section

- Describe the technical approach in enough detail to implement
- If multiple options exist, document each with pros/cons
- Include code snippets or pseudocode where helpful

### Decision Section

- Clearly state which approach was chosen
- Document the reasoning—this is valuable for future reference
- Note any trade-offs accepted

### Implementation Notes Section

- Update this section during implementation
- Capture unexpected findings or challenges
- Note any deviations from the original plan and why

## Lifecycle

1. **Creation**: Create the plan before starting significant work
2. **Evolution**: Update the plan as understanding deepens during implementation
3. **Completion**: Mark as completed when the work is done; the plan becomes historical documentation
4. **Reference**: Link to the plan from relevant session logs

## Relationship to Session Logs

- Plans are forward-looking (what we intend to do)
- Session logs are backward-looking (what we did)
- Reference plans from session logs using the `related_plans` field
- Reference session logs from plans using the `related_logs` field (optional)
