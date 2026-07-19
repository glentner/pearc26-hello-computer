# DRAFT Commits Workflow

This document describes the work-in-progress commit workflow used in this repository.

## Overview

While working on the manuscript, commit often with descriptive messages using `git`. All work happens
on the `draft` branch, with commits prefixed `DRAFT: `. This keeps work regularly pushed off the local
machine to the remote `draft` branch — backup, and visibility into the paper as it takes shape.

## Workflow

### Starting work

1. Ensure you're on the `draft` branch:
   ```bash
   git switch draft
   ```
2. Make changes and commit frequently with the `DRAFT: ` prefix:
   ```bash
   git commit -m "DRAFT: Fold cycle-2 feedback into the approach section"
   git commit -m "DRAFT: Integrate abstract from revised outline"
   ```
3. Push to the remote `draft` branch regularly:
   ```bash
   git push origin draft
   ```

### Completing a revision (release)

Shipping is done by `/paper-release`, which:

1. Strips the `DRAFT: ` prefix from all commits since the last release
   (`git filter-branch -f --msg-filter 'sed "s/^DRAFT: //"' main..HEAD`).
2. Fast-forward merges `draft` into `main` (linear history; never `--no-ff`).
3. Returns to `draft` and force-pushes it (the `draft` branch is understood to be rewritten; force-push
   is acceptable **here only**, never on `main`).

## Commit message format

### During development (DRAFT commits)

```
DRAFT: <brief description of change>

<optional longer description>

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>
```

### `[harness]` commits (the one exception)

The `/paper-harness` skill (the toolchain self-improvement applier) is the exception to the `DRAFT: `
prefix. Its commits use a **`[harness]` subject** (e.g. `[harness] Factor the meta-note step into a
snippet (F1)`) — **not** a `DRAFT: ` prefix — so that `/paper-release`'s `sed "s/^DRAFT: //"`
prefix-strip leaves them intact; the `[harness]` subjects ride to `main` on the next release
fast-forward merge as a readable record of toolchain changes. They are committed directly on `draft`,
one fix per atomic commit, and **keep the co-author trailer** like every other commit.

## Why this approach?

- **Safety**: frequent commits and pushes keep work backed up.
- **Visibility**: the paper's evolution is visible on the `draft` branch.
- **Preserved history**: the incremental `DRAFT:` commits document the writing process — valuable for a
  project that is itself *about* agent-first authorship.
- **Force-push OK**: the `draft` branch is understood to be rewritten; force-push is acceptable there
  (never on `main`).

## Attribution

All commits include the co-author line when work is done with an AI agent. Under Claude Code:

```
Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>
```

This is the **configurable current-harness identity**; if you re-home the toolkit to another harness,
update it in one place (the skills' commit steps).

## History (the `wip` → `draft` rename)

Through the production of the paper (v0.1.0–v1.1.0; see the git history and `logs/`), this project used a
`wip` branch and a `WIP: ` prefix, and earlier commits credit `Oz <oz-agent@warp.dev>` / `Warp
<agent@warp.dev>` from the WARP era. The convention is now **`draft` / `DRAFT: `** — it reads naturally
for a manuscript and won't be misread as "work-in-progress code." Historical commits and the legacy
`/release` and `/latex-integration-*` skills are **not** rewritten.

**To adopt the new convention on this repo** (a git operation, done when you're ready — the factory only
*recommends* it):

```bash
git branch -m wip draft            # rename the local branch
git push origin -u draft           # publish the renamed branch
git push origin --delete wip       # remove the old remote branch (optional)
```
