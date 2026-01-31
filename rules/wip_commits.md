# WIP Commits Workflow

This document describes the work-in-progress (WIP) commit workflow used in this repository.

## Overview

While working on a feature or task, commit often with descriptive messages and notes using `git` as the version control tool. All work should start on the `wip` branch with commits prefixed by `WIP: `.

This approach ensures code is regularly pushed off the local machine to the remote `wip` branch, providing backup and visibility into ongoing work.

## Workflow

### Starting Work

1. Ensure you're on the `wip` branch:
   ```bash
   git checkout wip
   ```

2. Make changes and commit frequently with the `WIP: ` prefix:
   ```bash
   git commit -m "WIP: Add initial experiment scaffolding"
   git commit -m "WIP: Implement data loading function"
   git commit -m "WIP: Fix edge case in parser"
   ```

3. Push to the remote `wip` branch regularly:
   ```bash
   git push origin wip
   ```

### Completing a Feature (Release)

When work on a feature is complete and ready for release:

1. Strip the `WIP: ` prefix from the most recent commit to mark the milestone:
   ```bash
   git commit --amend -m "$(git log -1 --pretty=%B | sed 's/^WIP: //')"
   ```

2. Force push to the `wip` branch to mark the release point:
   ```bash
   git push --force origin wip
   ```

3. Merge into `main` (preserving the full incremental history):
   ```bash
   git checkout main
   git merge wip
   git push origin main
   ```

4. Return to `wip` for continued development:
   ```bash
   git checkout wip
   ```

## Commit Message Format

### During Development (WIP commits)

```
WIP: <brief description of change>

<optional longer description>
<optional notes about what's incomplete or needs attention>

Co-Authored-By: Warp <agent@warp.dev>
```

### Final Commits (after squashing)

```
<type>: <brief description>

<detailed description of changes>

Co-Authored-By: Warp <agent@warp.dev>
```

Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`

## Why This Approach?

- **Safety**: Frequent commits and pushes ensure work is backed up
- **Visibility**: Others can see progress on the `wip` branch
- **Preserved History**: The incremental WIP commits document the development process—valuable for a project about agentic workflows
- **Force Push OK**: The `wip` branch is understood to be rewritten; force push is acceptable here (but never on `main`)

## Attribution

All commits should include the co-author line when work is done with an AI agent:
```
Co-Authored-By: Warp <agent@warp.dev>
```
