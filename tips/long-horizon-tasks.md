# Long-Horizon Task Management with Agentic Tools

## The Problem

Agentic AI tools operate within finite context windows. Complex projects—like writing a research paper—span multiple sessions and generate far more context than any single conversation can hold. Without deliberate strategy, each session starts from scratch, losing the accumulated understanding from prior work.

## Our Solution: Structured Memory Files

We use a combination of markdown files with YAML frontmatter to create "memory anchors" that persist between sessions:

### 1. Planning Documents (`plans/`)

Plans capture strategic direction and track progress:

```markdown
---
created: "2026-01-31"
status: "in-progress"
---

# Plan Title

## Goals
1. Goal one
2. Goal two

## Sub-Tasks
- [ ] Task A.1: Description
- [ ] Task A.2: Description

## Progress
**Completed**: 0/N

## Session Prompt Template
```
[Incremental prompt for next session]
```
```

The **session prompt template** is the key innovation—it's a pre-written prompt that future sessions can use to re-establish context quickly.

### 2. Reference Notes (`outline/notes/refs/`)

Deep-dive notes on each source preserve research insights:

```yaml
---
bibkey: "author2024title"
title: "Full Title"
key_findings:
  - "Finding one"
  - "Finding two"
sample_sentences: |
  Pre-written prose ready to integrate into the manuscript.
---
```

The `sample_sentences` field is particularly valuable—it's pre-synthesized prose that can be pulled directly into drafts.

### 3. Session Logs (`logs/`)

Logs capture what happened and why, including the user's verbatim input:

```yaml
---
timestamp: "2026-02-01T01:47:50Z"
session_type: "documentation"
summary: "Brief description"
files_modified:
  - path/to/file.md
user_input: |
  The exact prompt the user provided
---
```

Preserving `user_input` verbatim enables audit trails and helps future sessions understand intent.

### 4. Progress Trackers (`README.md` in task directories)

Simple checklists with completion fractions:

```markdown
## References (13 total)
- [x] `author2024a` — Complete
- [ ] `author2024b` — Pending

## Progress
**Completed**: 1/13
```

## The Recursive Dimension

The most powerful aspect: **prompts that create the infrastructure for future prompts**. Early sessions establish:

- Rules (in `rules/`) about how future sessions should behave
- Templates (in plans) that future sessions can follow
- File conventions that make context re-loading predictable

This creates a positive feedback loop where each session improves the scaffolding for the next.

## Practical Tips

1. **End sessions with commits**: Always commit work before context is lost
2. **Write the next prompt**: Include a session prompt template in plans
3. **Preserve verbatim input**: The `user_input` field in logs is invaluable for context recovery
4. **Use YAML frontmatter**: Structured metadata enables programmatic access and consistent formatting
5. **Track progress visibly**: Completion fractions (e.g., "5/13") make status immediately clear

## Example: Reference Deep-Dive Workflow

See `outline/notes/refs/README.md` for a working example:

1. Plan defines the 13 references to process
2. Progress tracker shows completion status
3. Session prompt template enables any new session to pick up where the last left off
4. Each deep-dive produces a structured note with `key_findings` and `sample_sentences`
5. Session logs preserve the decision trail

## Why This Works

Traditional documentation captures *what* was done. This approach captures:

- **What** was done (file changes)
- **Why** it was done (user input, rationale)
- **What's next** (session prompts, progress trackers)
- **How to continue** (templates, conventions)

The result: a project that can be "re-hydrated" into any new session with minimal context loss.

## Related

- `rules/session_logs.md` — Session logging requirements
- `outline/notes/agentic-research-meta.md` — Meta-commentary on this approach
- `plans/first-integration.md` — Example plan with session prompt template
