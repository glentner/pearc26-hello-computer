---
timestamp: "2026-05-02T16:14:31Z"
session_started: "2026-05-01T19:52:28Z"
duration_minutes: ~80
session_type: "housekeeping"
summary: "Migrated stored prompts to .agents/skills/, removed .warp/, audited and rewrote AGENTS.md against actual repo state, synced outline/README.md."
user_input: |
  I want to do some house keeping in this project. Please see our AGENTS.md and README.md to understand the academic paper we've been writing together. I'm using Warp (here now and always) to work on this project. I've just learned that we can have project-specific skills (distinct from Warp "Rules") under .agents/skills/<some-skill>/SKILL.md and that these can even keep companion scripts and configuration in the directory.

  I've got a plans, prompts, rules, and a .warp/ folder here as I didn't understand yet how things all worked. Now, part of the purpose of this repo is educational so I don't necessarily want to suggest systemic meaning to names of things that don't have real support in other agent harnesses. I was thinking of moving my prompts to .agents/skills/ appropriately. What do you think of also organizing our rules, plans, and other things under .agents/? My only thought here is to distinguish between prompting for the harness and the *content* (or *material*) of the project.
user_followup: |
  My only uncertain with rules/ is that these are meant to be always-there ambient context for behavior with how we work on the project; and Warp has this concept and calls them "Rules", but I don't think .agents/rules/ is a supported thing. Warp Rules are stored in the Warp Drive and are not project specific. So I'm forced to treat these as lower-priority material context not hard instruction which is challenging (e.g., always forgetting to do our session logs). Just like the skills, these make sense to go under .agents but that's misleading to a reader because that's not supported and we're only linking in AGENTS.md (as we do now).
user_followup_2: |
  I think I want to keep the name "rules" as that's what they would be if they were global and stored in my Warp Drive. They could be improved and made more LLM-optimized, sure. I've read from other AI software engineers that keeping AGENTS.md lean with references to other deeper .md documents was a successful pattern. The fact that we can't always keep the rules speaks to the challenge with high-priority system instructions versus lower-priority in-context-window material on a best-effort basis.

  The prompts/ are meant to be repeated invocations so should be skills actually. Let's move those and handle .warp as we discussed. And we'll leave the rest of the structure alone. And instead I'd appreciate if you could just assess the alignment between our rules and other machinery in the repo with how they're referenced in AGENTS.md - that is - is our AGENTS.md up-to-date?
user_followup_3: |
  These all sounds good, nicely done identifying these inconsistencies. Please proceed.
files_modified:
  - .agents/skills/release/SKILL.md
  - .agents/skills/latex-integration-first-pass/SKILL.md
  - .agents/skills/latex-integration-second-pass/SKILL.md
  - .warp/prompts/release.md
  - prompts/latex_integration_first_pass.md
  - prompts/latex_integration_second_pass.md
  - AGENTS.md
  - rules/wip_commits.md
  - outline/README.md
  - logs/2026-05-02T16-14-31-skills-migration-and-agents-md-alignment.md
commits:
  - "68031db: WIP: Migrate stored prompts to .agents/skills/"
  - "3c01af5: WIP: Complete tips/ index and standardize Oz co-author attribution"
  - "6d2c54d: WIP: Replace stale AGENTS.md structure and workflow with current reality"
  - "12a0e60: WIP: Sync outline/README.md directory listing with actual contents"
related_plans: []
tags:
  - housekeeping
  - skills
  - agents-md
  - alignment
  - structural-docs
---

# Skills Migration and AGENTS.md Alignment

## Summary

Two-part housekeeping session. First: migrate ad-hoc stored prompts to the
project-scoped skill mechanism (`.agents/skills/<name>/SKILL.md`) and retire
the `.warp/` directory in favor of the harness-agnostic `.agents/` location.
Second: audit `AGENTS.md` against the actual state of the repository and
fix every drift point identified, including a structural-docs violation in
`outline/README.md`.

## Discussion

The session began with a broader design question about whether to consolidate
multiple top-level directories (`rules/`, `plans/`, `tips/`, `prompts/`,
`.warp/`) under `.agents/` to mirror the conceptual split between *harness
configuration* and *project content*.

The conclusion (after several rounds): only things with actual harness support
should live under `.agents/`. Everything else — including `rules/`, which has
no portable cross-harness mechanism for "always-on ambient context" — should
stay at the top level. The user's framing: keep the directory `rules/`
because the term matches Warp's user-scoped Rules concept (stored in Warp
Drive); treat them as best-effort context referenced from `AGENTS.md`; accept
that the only true "always-on" mechanism in the current cross-harness
landscape is the body of `AGENTS.md` itself.

This insight is itself worth a paragraph in the manuscript (noted but not
acted on this session).

## Work Completed

### Part 1: Skills migration (commit 68031db)

- Created three project skills with YAML frontmatter (`name`, `description`):
  - `.agents/skills/release/SKILL.md` (was `.warp/prompts/release.md`)
  - `.agents/skills/latex-integration-first-pass/SKILL.md` (was `prompts/latex_integration_first_pass.md`)
  - `.agents/skills/latex-integration-second-pass/SKILL.md` (was `prompts/latex_integration_second_pass.md`)
- Removed `prompts/` and `.warp/` directories using `del` (per `rules/file_deletion.md`).
- Updated `AGENTS.md` "Stored Prompts" section to "Skills" and listed all three.

### Part 2: AGENTS.md alignment audit

Identified six drift points; applied fixes for all.

#### Tips index completion (commit 3c01af5)

`AGENTS.md` referenced only `tips/warp-conversation-history.md` while
`tips/` actually contains three files. Added entries for
`agent-text-editing-pitfalls.md` and `long-horizon-tasks.md`. Promoted
`tips/` to its own subsection (parallel to the `rules/` listing) instead
of a parenthetical at the end of the rules list. This restores compliance
with `rules/structural_docs.md`.

#### Co-author attribution standardization (commit 3c01af5)

`AGENTS.md` and `rules/wip_commits.md` used the older
`Co-Authored-By: Warp <agent@warp.dev>` form. The agent in Warp is now
called "Oz", and the LaTeX integration skills (preserved verbatim from the
prompt files) already use `Co-Authored-By: Oz <oz-agent@warp.dev>`.
Standardized everything on the Oz form. Added a note in
`rules/wip_commits.md` acknowledging the historical "Warp" form so the
provenance of older commits stays explicable; historical commits are not
rewritten.

#### Repository Structure rewrite (commit 6d2c54d)

The previous "intended structure" listed `src/`, `data/`, `manuscript/`,
`figures/` as not-yet-created placeholders, plus a "Current State: early
setup phase with only template files present" note. None of this matched
reality. Replaced with a description of the actual layout, grouped by
purpose:

- Manuscript and supporting material (manuscript.tex, references.bib,
  Makefile, outline/, reviews/)
- Process and history (plans/, logs/, rules/, tips/)
- Harness configuration (.agents/skills/, .github/)
- Build output (build/, lentner-2026-*.pdf)

#### Development Workflow rewrite (commit 6d2c54d)

The previous workflow described `src/`/`data/`/`figures/` creation steps
that don't reflect this project. Replaced with the outline-first markdown
drafting loop, the two-pass LaTeX integration via the new skills, and the
build/release flow.

#### outline/README.md sync (commit 12a0e60)

The directory structure block listed only `easter-eggs.md` under
`outline/notes/` while the directory has accumulated 11 entries plus the
`refs/` subdirectory. Enumerated each entry with a short description.

## Notable Decision

Initially I proposed `Co-Authored-By: Oz <oz-agent@warp.dev>` based on the
current agent name. The user's existing project rule and the older `rules/wip_commits.md`
specified the "Warp" form. Adopted the Oz form on the principle that the
canonical attribution should track the current agent identity, with a note
preserving the historical context.

## Next Steps

- Push the four WIP commits to `origin/wip` when convenient.
- Consider whether `reviews/` deserves its own README index (or an entry in
  `rules/structural_docs.md`).
- The "linking vs inlining" insight about always-on context vs best-effort
  prose is worth incorporating into the manuscript discussion section.
