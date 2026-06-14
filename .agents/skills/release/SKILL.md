---
name: release
description: "Ship the wip branch to main — strip WIP: prefixes from commit messages, fast-forward merge, push, return to wip and force-push. With optional arguments: squash commits, bump version (patch/minor/major), create an annotated tag, and publish a GitHub release (which triggers the PDF build via CI). Default invocation does merge-and-push only; additional behavior is enabled by free-form instructions after the slash command."
---

# Release (Ship It)

## When to Use

Invoke `/release` when WIP commits on the `wip` branch are ready to ship to `main`. The default behavior is conservative: rewrite `WIP: ` prefixes, fast-forward merge into `main`, push, return to `wip`, and force-push. Anything beyond that (squash, version bump, tag, GitHub release) is opt-in via free-form instructions passed after the slash command.

## User Instructions

Additional instructions provided with the invocation: $ARGUMENTS

## Argument Parsing

If any text was passed with the invocation, parse it case-insensitively against the patterns below. If the instruction is ambiguous or contradicts itself, STOP and ask the user to clarify rather than guess.

- `patch version bump` / `patch bump` → bump patch (`x.y.Z+1`); implies tag
- `minor version bump` / `minor bump` → bump minor (`x.(Y+1).0`); implies tag
- `major version bump` / `major bump` → bump major (`(X+1).0.0`); implies tag
- `tag` → create an annotated version tag (requires a bump or explicit version)
- `release` → publish a GitHub release (implies tag and bump)
- `squash` / `squash commits` → collapse all wip commits into one before merging
- An explicit version like `v1.2.0` overrides bump computation

If no arguments were passed, run the default merge-only path (Steps 1, 3, 4, 6, 8 below; skip 2, 5, 7).

## Safety Principles

- `--force` is used **only** on the `wip` branch. Never on `main`, never on tags, never anywhere else.
- Use the default fast-forward merge (`git merge wip`). Never `--no-ff`. We want linear history.
- After a successful ship, `main` and `wip` point to the **same** commit.
- Author all new commits with `Co-Authored-By: Oz <oz-agent@warp.dev>` (per `rules/wip_commits.md`).
- If pre-flight checks fail (dirty tree, wrong branch, build failure, divergent main), STOP and report. Do not attempt remediation without confirmation.
- Confirm the computed version and the release notes with the user **before** tagging or publishing.

## Procedure

### Step 1 — Pre-flight checks (always)

1. Working directory must be clean:
   ```bash
   git status --porcelain
   ```
   Non-empty output → abort.
2. Current branch must be `wip`:
   ```bash
   git branch --show-current
   ```
3. Sync with origin:
   ```bash
   git fetch origin
   git fetch --tags
   ```
4. `wip` must be ahead of `main`:
   ```bash
   git rev-list --count main..HEAD
   ```
   `0` → nothing to ship; abort.
5. Manuscript must build cleanly:
   ```bash
   make build
   ```
   Non-zero exit → abort.

### Step 2 — Squash (only if `squash` was requested)

Skip entirely unless the user asked to squash. When squashing:

1. Compute the merge-base and soft-reset to it (keeps all changes staged):
   ```bash
   BASE=$(git merge-base main wip)
   git reset --soft "$BASE"
   ```
2. Propose a commit message synthesized from the prior `WIP: `-prefixed messages, **without** the `WIP: ` prefix. Confirm with the user, then commit:
   ```bash
   git commit -m "<proposed message>" -m "Co-Authored-By: Oz <oz-agent@warp.dev>"
   ```
3. After squashing, **skip Step 3** (there are no `WIP: ` prefixes left to rewrite).

### Step 3 — Rewrite `WIP: ` prefixes (skip if squashed)

```bash
git filter-branch -f --msg-filter 'sed "s/^WIP: //"' main..HEAD
```

This rewrites only commits in `main..HEAD`, dropping the `WIP: ` prefix. Commits that don't start with `WIP: ` are unaffected. Note: `filter-branch` is the chosen tool here per project preference; do not substitute `git rebase -i` or `git-filter-repo`.

### Step 4 — Fast-forward merge into `main`

```bash
git checkout main
git merge wip
```

Do **not** pass `--no-ff`. If git refuses the merge (non-fast-forward, conflicts), STOP and report — `main` has diverged and human intervention is needed.

### Step 5 — Version bump and tag (only if requested)

Skip entirely unless a bump, explicit version, or `tag` was requested. When tagging:

1. Determine the current latest tag:
   ```bash
   git describe --tags --abbrev=0
   ```
2. Compute the new version per semver (or use the explicit version provided).
3. Confirm the computed version with the user.
4. Create an **annotated** tag on the merged `main` HEAD:
   ```bash
   git tag -a <version> -m "Release <version>"
   ```

### Step 6 — Push `main` (and tag if any)

```bash
git push origin main
git push origin <version>   # only if a tag was created in Step 5
```

### Step 7 — GitHub release (only if `release` was requested)

Skip entirely unless the user asked for a release. When releasing:

1. Review prior release style for tone and structure (so notes feel consistent):
   ```bash
   gh release list -L 5
   gh release view <previous-tag> --json tagName,name,body
   ```
2. Draft comprehensive notes consistent with the prior style. Either:
   - Use `--generate-notes` for an auto-generated changelog, then review with the user before publishing; **or**
   - Hand-curate notes in a file and pass `--notes-file <file>`.
3. Confirm the notes with the user, then publish:
   ```bash
   gh release create <version> --title "<version>" --generate-notes
   ```
   (or `--notes-file` instead of `--generate-notes`).
4. Verify the release published and that `release_pdf.yml` was triggered. The workflow listens for `release: types: [published]`, not tag pushes — only the `gh release create` step builds the PDF.

### Step 8 — Return to `wip` and force-push (always)

```bash
git checkout wip
git push --force origin wip
```

After this, `origin/main` and `origin/wip` point to the same commit. The wip branch is ready for the next iteration.

## Examples

### Default — just merge

```
/release
```

Strips `WIP: ` prefixes on `main..HEAD`, fast-forward merges into `main`, pushes `main`, returns to `wip`, force-pushes `wip`. No tag, no GitHub release, no PDF build.

### Minor version bump with tag and release

```
/release Let's do a minor version bump with tag and release
```

Default path plus: compute next minor version from `git describe --tags --abbrev=0`, confirm with user, annotated tag on merged main, push tag, draft release notes consistent with prior releases, publish GitHub release (triggers PDF build).

### Squash with patch bump, no release

```
/release squash and patch bump
```

Soft-reset `wip` to merge-base, propose+confirm a single combined commit message, commit with Oz co-author. Skip prefix rewrite (no `WIP: ` left). Merge to main, push, compute patch version, tag, push tag. **No** GitHub release. Force-push wip.

### Explicit version

```
/release tag as v1.2.0 and release
```

Use `v1.2.0` directly instead of computing a bump. Same flow as a bump-with-release otherwise.

## Notes

- `release_pdf.yml` triggers only on `release: types: [published]`. Pushing a tag without creating a release will **not** build the PDF.
- The `WIP: ` prefix convention and the force-push-on-wip allowance are documented in `rules/wip_commits.md`.
- If the user's instruction includes something not covered above (e.g. `dry run`, `skip build`), STOP and ask before deviating from the documented procedure.
