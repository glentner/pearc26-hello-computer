---
name: paper-release
description: >-
  Ship the paper's `draft` branch to `main` — the release phase of the paper factory. Strips `DRAFT:`
  prefixes, fast-forward merges into `main`, and (opt-in) bumps the version, tags, and publishes a
  GitHub release that triggers the PDF build via CI. A RELEASE GUARD runs `make build`, `make check`,
  and `paper_status.py` first: check_paper.py errors (dangling cite, over page limit) and open
  must-fix items or `release_ready: false` are hard blockers requiring explicit human override.
  For a camera-ready release, packages the ACM TAPS zip via `make upload`. On success advances
  macro_phase to `released`. Default invocation is conservative (merge-and-push only); squash, bump,
  tag, release, and camera-ready are enabled by free-form instructions after the slash command.
disable-model-invocation: true
argument-hint: "[squash] [patch|minor|major bump | vX.Y.Z] [tag] [release] [camera-ready] [status]"
allowed-tools: Read, Grep, Glob, AskUserQuestion, Bash(git status *), Bash(git branch *), Bash(git log *), Bash(git diff *), Bash(git rev-parse *), Bash(git rev-list *), Bash(git fetch *), Bash(git merge-base *), Bash(git switch *), Bash(git merge *), Bash(git reset *), Bash(git commit *), Bash(git tag *), Bash(git describe *), Bash(git filter-branch *), Bash(git push *), Bash(gh release *), Bash(make *), Bash(python3 .agents/factory/bin/*)
---

# paper-release — ship draft → main

## When to Use

Invoke `/paper-release` when the DRAFT commits on the `draft` branch are ready to ship to `main`. The
default behavior is conservative: rewrite `DRAFT: ` prefixes, fast-forward merge into `main`, push,
return to `draft`, and force-push `draft`. Anything beyond that (squash, version bump, tag, GitHub
release, ACM TAPS packaging) is opt-in via free-form instructions after the slash command. This is
the **one irreversible phase** — remote pushes, tags, and releases can't be checkpointed — so it
always confirms with you before any outward step. It is the release-mechanics port of the legacy
`/release` skill, gated on the paper factory's release readiness.

## References

- Lifecycle: [`methodology.md`](../../factory/methodology.md) (`/paper-release` = ship `draft → main`)
- Release blockers & human gate: [`review-rubric.md`](../../factory/review-rubric.md) ("Mandatory
  human gate") and [`invariants.md`](../../factory/invariants.md) (§1 venue/page/ACM policy, §3
  citation integrity — the must-fix classes that block release)
- Repo rules: `rules/draft_commits.md` (DRAFT prefix + force-push-on-draft), `rules/session_logs.md`
  (mandatory session log), `rules/file_deletion.md` (`/bin/rm`, not the `del` Warp-ism)
- **Portability:** [`portability.md`](../../factory/portability.md) — this skill runs on any harness; if the *Current state* commands aren't auto-injected, run them yourself in Step 1, and if `AskUserQuestion` is unavailable, ask in plain text and STOP.

## User Instructions

Additional instructions provided with the invocation: $ARGUMENTS

## Current state (injected at load)

- Branch: !`git branch --show-current`
- Tree: !`git status --porcelain | head -n 20`
- Commits on draft (vs main): !`git log --oneline main..HEAD 2>/dev/null | head -n 20`
- Paper FSM: !`python3 .agents/factory/bin/paper_status.py PAPER.md --summary 2>/dev/null || echo "(run paper_status.py in Step 1)"`

## Argument Parsing

Parse `$ARGUMENTS` case-insensitively against the patterns below. If ambiguous or self-contradictory,
STOP and ask rather than guess.

- `status` / `report` → run the RELEASE GUARD read-only (Steps 1–2), report readiness + what a
  default ship would do; no merge, no push, no mutation.
- `patch version bump` / `patch bump` → bump patch (`x.y.Z+1`); implies tag.
- `minor version bump` / `minor bump` → bump minor (`x.(Y+1).0`); implies tag.
- `major version bump` / `major bump` → bump major (`(X+1).0.0`); implies tag.
- An explicit version like `v1.2.0` overrides bump computation.
- `tag` → create an annotated version tag (requires a bump or explicit version).
- `release` → publish a GitHub release (implies tag and bump; triggers the PDF CI).
- `squash` / `squash commits` → collapse all draft commits into one before merging.
- `camera-ready` / `taps` → also build and stage the ACM TAPS upload zip via `make upload`.
- No arguments → the default merge-only path (Steps 1–2, 4, 6, 8, 10; skip 3, 5, 7, 9).

## Safety Principles

- **`--force` is used ONLY on the `draft` branch.** Never on `main`, never on tags, never anywhere else.
- **Fast-forward merge only** (`git merge draft`). Never `--no-ff`, never a merge commit — we keep
  linear history. After a successful ship, `main` and `draft` point to the **same** commit.
- **RELEASE GUARD is a hard gate.** `make build` and `make check` must pass; a `check_paper.py`
  ERROR (dangling cite, over page limit) is a non-negotiable blocker. If `paper_status.py` reports
  open `must-fix` items or `release_ready: false`, STOP and require an **explicit** human override via
  AskUserQuestion before proceeding — do not ship a paper the FSM says is not ready.
- **Confirm before any irreversible/outward step.** Always confirm the computed version and release
  notes, and get an explicit AskUserQuestion choice, before `git push`, `git tag`, or
  `gh release create`. Camera-ready (`make upload`) is confirmed too.
- **Never guess.** If the guard, version math, or an instruction is ambiguous, emit
  `[NEEDS CLARIFICATION: …]` and ask.
- **Advance state only via the script.** On success, `set_status.py --macro-phase released --touch` —
  never hand-edit `PAPER.md` frontmatter.
- Author every new commit with the configurable co-author trailer
  `Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>` (Claude Code — **not** the
  old Oz/Warp trailer).
- If a pre-flight check fails (dirty tree, wrong branch, build/check failure, divergent `main`),
  STOP and report. Do not attempt remediation without confirmation.

## Procedure

### Step 0 — status (when requested)
`status`: run Steps 1–2 read-only, report the guard result + the plan a default ship would run, and
stop. No merge, push, tag, or mutation.

### Step 1 — Pre-flight checks (always)
1. Read the paper FSM fresh: `python3 .agents/factory/bin/paper_status.py PAPER.md` (exit 2 →
   `PAPER.md` invalid, STOP). Capture `macro_phase`, `completion.release_ready`,
   `feedback_by_severity["must-fix"]`, `review.verdict`, `anchors_missing`, `warnings`.
2. Working directory must be clean: `git status --porcelain`. Non-empty → abort.
3. Current branch must be `draft`: `git branch --show-current`.
4. Sync with origin: `git fetch origin` and `git fetch --tags`.
5. `draft` must be ahead of `main`: `git rev-list --count main..HEAD`. `0` → nothing to ship; abort.

### Step 2 — RELEASE GUARD (always; the paper-factory gate)
1. Build must be clean: `make build`. Non-zero exit → STOP.
2. Linters must pass: `make check` (runs `check_paper.py`). **Exit 1 is a HARD BLOCKER** — a dangling
   `\cite` or an over-page-limit paper cannot ship. Report the ERROR lines and STOP. (WARNINGs, e.g.
   an orphan bib entry or a stale AI-use disclosure, are surfaced but do not block; note them.)
3. Readiness gate from Step 1's `paper_status.py`:
   - If `feedback_by_severity["must-fix"] > 0` **or** `completion.release_ready` is `false` (or
     `review.verdict != approved`), the paper is not release-ready. **STOP and require explicit human
     override** via AskUserQuestion ("Ship anyway despite N open must-fix / release_ready=false?"
     Yes overrides / No aborts). Only proceed on an explicit Yes; record the override in the session
     log and the report.
   - Also surface any `anchors_missing` or `warnings` for the human to weigh in the same prompt.
4. Audit-currency gate (orthogonal to the must-fix / `release_ready` checks above): read
   `review.reviewed_commit` from Step 1's `paper_status.py`.
   - If it is set, verify the shipped manuscript was actually the audited one:
     `git diff <reviewed_commit>..HEAD -- manuscript.tex references.bib`. **Non-empty output means the
     manuscript changed since the last `/paper-draft` pass-B audit** — STOP and require an **explicit
     human override** via AskUserQuestion ("Ship despite N-line drift since the last audited commit
     `<reviewed_commit>`?") before proceeding; record the override in the session log and report.
   - If `reviewed_commit` is unset, note "no audit recorded" and let the human decide in the same prompt.

### Step 3 — Squash (only if `squash` was requested)
Skip unless asked. When squashing:
1. Soft-reset to the merge-base (keeps all changes staged):
   ```bash
   BASE=$(git merge-base main draft)
   git reset --soft "$BASE"
   ```
2. Propose a single commit message synthesized from the prior `DRAFT: `-prefixed subjects, **without**
   the `DRAFT: ` prefix. Confirm with the human, then commit with the co-author trailer:
   ```bash
   git commit -m "<proposed message>" \
     -m "Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
   ```
3. After squashing, **skip Step 4's prefix rewrite** (no `DRAFT: ` prefixes remain).

### Step 4 — Rewrite `DRAFT: ` prefixes (skip if squashed)
```bash
git filter-branch -f --msg-filter 'sed "s/^DRAFT: //"' main..HEAD
```
Rewrites only commits in `main..HEAD`, dropping the `DRAFT: ` prefix; commits without it are
unaffected. `filter-branch` is the chosen tool per project preference — do not substitute
`git rebase -i` or `git-filter-repo`.

### Step 5 — Version bump and tag (only if a bump / explicit version / `tag` was requested)
1. Current latest tag: `git describe --tags --abbrev=0`.
2. Compute the new version per semver (or use the explicit version provided).
3. **Confirm the computed version with the human** (AskUserQuestion).
4. Create an **annotated** tag on the merged `main` HEAD (created in Step 6, so tag after the merge):
   ```bash
   git tag -a <version> -m "Release <version>"
   ```
   (If you prefer to tag before push, tag the merged HEAD after Step 6; never tag `draft`.)

### Step 6 — Fast-forward merge into `main`
```bash
git switch main
git merge draft
```
Do **not** pass `--no-ff`. If git refuses (non-fast-forward, conflicts), STOP and report — `main` has
diverged and needs human intervention. (If tagging, create the annotated tag from Step 5 now, on the
merged `main` HEAD.)

### Step 7 — ACM TAPS camera-ready package (only if `camera-ready` was requested)
Skip unless asked. Confirm intent first (AskUserQuestion), then:
```bash
make upload
```
This does a clean `make release`, stages `pdf/manuscript.pdf` + `Source/{manuscript.tex,references.bib}`,
and writes `pearc26-<TAPS_ID>.zip`. Report the zip path so the human can upload it to ACM TAPS; do not
attempt to submit it.

### Step 8 — Push `main` (and tag if any) — CONFIRM FIRST
Confirm the outward push via AskUserQuestion, then:
```bash
git push origin main
git push origin <version>   # only if a tag was created
```

### Step 9 — GitHub release (only if `release` was requested) — CONFIRM FIRST
Skip unless asked. When releasing:
1. Review prior release style for consistent tone/structure:
   ```bash
   gh release list -L 5
   gh release view <previous-tag> --json tagName,name,body
   ```
2. Draft comprehensive notes in the prior style — either `--generate-notes` (auto changelog) or
   hand-curated notes in a file (`--notes-file <file>`).
3. **Confirm the notes with the human** (AskUserQuestion), then publish:
   ```bash
   gh release create <version> --title "<version>" --generate-notes
   ```
4. Verify the release published and that the PDF workflow was triggered — the workflow listens for
   `release: types: [published]`, **not** tag pushes, so only `gh release create` builds the PDF.

### Step 10 — Return to `draft`, force-push, and advance state (always)
```bash
git switch draft
git push --force origin draft
```
After this, `origin/main` and `origin/draft` point to the same commit. Then advance the FSM:
```bash
python3 .agents/factory/bin/set_status.py PAPER.md --macro-phase released --touch
```
If `set_status.py` changed `PAPER.md`, commit it on `draft` (`DRAFT: ` prefix + co-author trailer) and
force-push `draft` again so the released state is recorded.

### Step 11 — Surface open harness findings (always; NON-BLOCKING)
Independently of the ship result, list any open harness feedback so it isn't forgotten:
```bash
python3 .agents/factory/bin/meta_status.py META.md --status open
```
Report each open finding as `F# · <severity> · <title>` with a pointer to run `/paper-harness` to apply
them. This is **explicitly NON-BLOCKING and orthogonal to the RELEASE GUARD** — harness findings are
about the *toolchain*, not the paper's release-readiness, and never gate or override a ship. Include the
list (or "none") in both the session log and the final report. If `META.md` is absent, note "no META.md".

### Step 12 — Session log (always, MANDATORY)
Per `rules/session_logs.md`, the orchestrator (this skill) writes
`logs/<UTC-ISO>-<slug>.md` from the live conversation. Timestamp via
`date -u +"%Y-%m-%dT%H-%M-%S"`; capture the **verbatim** user invocation in the frontmatter
`user_input`, plus `files_modified`, `commits` (SHAs + subjects), and any override recorded in
Step 2. Commit the log on `draft` (`DRAFT: ` prefix + co-author trailer) and force-push `draft`.

### Final report
Guard result (build/check/readiness, any override), the merge outcome (`main` == `draft` SHA), the
version/tag if any, the release URL + PDF-CI trigger if released, the TAPS zip path if camera-ready,
the new `macro_phase: released`, the open harness findings surfaced in Step 11 (or "none", with the
`/paper-harness` pointer), and the session-log path.

## Examples

- `/paper-release` — guard, strip `DRAFT:` prefixes, fast-forward merge into `main`, confirm+push
  `main`, return to `draft`, force-push `draft`, set `macro_phase: released`, log. No tag/release/PDF.
- `/paper-release status` — run the RELEASE GUARD read-only; report readiness and the ship plan; no
  changes.
- `/paper-release minor bump, tag and release` — default path plus compute the next minor version
  from the latest tag, confirm, annotated tag on merged `main`, confirm+push tag, draft+confirm
  release notes, publish the GitHub release (triggers the PDF build).
- `/paper-release squash and patch bump` — soft-reset `draft` to merge-base, propose+confirm one
  combined commit (co-author trailer), skip prefix rewrite, merge, patch tag, push tag. No GitHub
  release.
- `/paper-release camera-ready, tag as v1.1.0 and release` — use `v1.1.0` directly, build the ACM
  TAPS zip via `make upload`, tag, push, publish release. Confirm each outward step.

## Notes

- The PDF workflow triggers only on `release: types: [published]` — pushing a tag without creating a
  release will **not** build the PDF.
- The `DRAFT: ` prefix convention and the force-push-on-draft allowance are documented in
  `rules/draft_commits.md`. `--force` is only ever legal on `draft`.
- A `check_paper.py` ERROR is a hard release blocker regardless of any other verdict
  (`review-rubric.md`, "Mandatory human gate"). Fix it and re-run `/paper-outline`/`/paper-draft`,
  don't override it.
- Use `/bin/rm` for any file deletion (the repo's `del` alias is a Warp-ism — see
  `rules/file_deletion.md`); `make upload`/`make distclean` already use `/bin/rm`.
- If the invocation asks for something not covered here (e.g. `dry run`, `skip check`, ship from a
  branch other than `draft`), STOP and ask before deviating.
