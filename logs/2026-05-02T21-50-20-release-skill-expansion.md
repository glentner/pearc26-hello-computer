---
timestamp: "2026-05-02T21:50:20Z"
duration_minutes: ~20
session_type: "skill-expansion"
summary: "Combined the user's 'Ship It' Warp prompt with the existing /release skill into a single comprehensive ship-it workflow that defaults to merge-only and accepts free-form arguments for squash, version bump, tag, and GitHub release."
user_input: |
  Do you have access to my stored prompts? I want to take the current version of my "Ship It" prompt which includes merging into the 'main' branch from 'wip' correctly after rewriting commit messages. We have an older version of it not in use that had included the instruction to squash the commits before merging to 'main' but I removed that instruction because generally I find that I'd like to keep all the commits. But my opinion on that is evolving.

  What I want to do is take that logic/instruction from 'Ship It' and combine that with our .agents/skills/release/SKILL.md skill with a comprehensive workflow that takes us from 'WIP: ' commits to version bumped, merged, tagged, pushed with a new release and back on the 'wip' branch. I want to craft the instructions to safely and confidently handle a few scenarios. I want the /release skill to default to handling everything without a version bump, tag, or release and only do the merge and push. But I need it to include all the context and instructions in case we are where I'll provide additional user instruction with the slash-command to say something like "Let's do a minor version bump with tag and release" that speaks to those additional actions and what specifically I want to do in the instance.

  Please find a copy of the 'Ship It' Warp prompt (from my Warp Drive) in /tmp/ship_it.md just in case.
files_modified:
  - .agents/skills/release/SKILL.md
  - AGENTS.md
  - logs/2026-05-02T21-50-20-release-skill-expansion.md
commits:
  - "e603848: WIP: Expand /release skill into a comprehensive ship-it workflow"
related_plans: []
tags:
  - skills
  - release
  - ship-it
  - workflow
  - agents-md
---

# /release Skill Expansion

## Summary

User asked to merge their Warp Drive "Ship It" prompt (provided as
`/tmp/ship_it.md` for reference) with the existing `.agents/skills/release/SKILL.md`
skill. The combined skill should default to a conservative merge-and-push
flow and opt into version bump / tag / GitHub release / squash via free-form
arguments after the slash command.

## Context

- I noted up front that I do not have direct access to Warp Drive stored
  prompts; the user anticipated this and placed a copy at `/tmp/ship_it.md`.
- The "Ship It" prompt prescribes the rewrite-and-merge mechanics:
  `git filter-branch -f --msg-filter 'sed "s/^WIP: //"' main..HEAD`,
  fast-forward merge into `main` (linear history; no `--no-ff`), push,
  return to `wip` and force-push. Force-push is ONLY permitted on `wip`.
- The previous `/release` skill only handled the GitHub release step and
  assumed `main` was already up-to-date.

## Design Decisions

- **Single skill, not two.** The user's intent is one entry point (`/release`)
  that DTRT based on arguments. Splitting into `/ship` + `/release` would
  fragment the workflow and require the user to remember a longer ladder
  of commands.
- **Default to merge-only.** Per user direction: bare `/release` strips
  prefixes, fast-forward merges, pushes, force-pushes wip. No tag, no
  GitHub release, no PDF build.
- **`$ARGUMENTS` placeholder.** The skill embeds `$ARGUMENTS` so any text
  after `/release` lands inline in the skill body where the agent reads
  it. A pattern table documents the recognized cases (patch/minor/major
  bump, explicit version, tag, release, squash) and instructs the agent
  to ASK if the request is ambiguous rather than guess.
- **Pre-flight `make build`.** This is a manuscript project; shipping a
  paper that doesn't compile would be a categorical mistake. Added to the
  always-run pre-flight block.
- **Squash skips the prefix rewrite.** When the user squashes, the new
  commit message is authored fresh (without `WIP: `), so running
  `git filter-branch` afterward would be a no-op. Documented this
  explicitly.
- **Annotated tags.** Tag flow uses `git tag -a` rather than lightweight
  tags; release engineering norms favor annotated tags for human-readable
  release metadata.
- **Honor `git filter-branch`.** The Ship It prompt explicitly directs
  the agent to use `filter-branch` despite Git's gentle deprecation
  notice. The skill carries this preference through and explicitly tells
  the agent NOT to substitute `git rebase -i` or `git-filter-repo`.

## Worked Examples Included in Skill

- `/release` — merge only.
- `/release Let's do a minor version bump with tag and release` — full pipeline.
- `/release squash and patch bump` — squash + tag, no GitHub release.
- `/release tag as v1.2.0 and release` — explicit version override.

## Work Completed

### Commit e603848 — Skill rewrite + AGENTS.md updates

- `.agents/skills/release/SKILL.md` rewritten as an 8-step procedure with
  clear "always" / "only if requested" markers. Argument parsing table and
  safety principles section make the optional surface explicit.
- `AGENTS.md` Skills section: `/release` one-liner now reflects the full
  scope.
- `AGENTS.md` Development Workflow step 6: renamed from "Release" to
  "Ship" and rewritten to describe `/release` alone for merge-only and
  `/release ...` with arguments for the full pipeline.

## Notable Decision: Did NOT Split Off "Ship It" as a Separate Skill

Considered: `/ship` (default merge-only) and `/release` (the existing
release-only flow). Rejected because:
- Two skills with overlapping concerns make the user remember which is
  which; the user explicitly framed the request as a single combined
  workflow.
- Versioning, tagging, and releasing only make sense AFTER shipping wip
  to main; combining them is the natural composition.
- The argument-driven model lets one entry point cover both the simple
  daily case and the rare full-release case.

## Next Steps

- First real-world invocation of the new `/release` will exercise all
  branches; expect to refine wording or add edge cases based on how it
  performs.
- Camera-ready submission will be a good forcing function for the
  full-release path (`/release minor version bump with tag and release`
  or similar).
