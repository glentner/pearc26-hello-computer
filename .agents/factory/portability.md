# Harness portability — running the paper factory outside Claude Code

The `paper-*` skills are plain markdown + portable shell (`git`, `make`, the `.agents/factory/bin`
scripts) and are meant to run on **any** agent harness — Claude Code, Warp, OpenCode, etc., including
**open-weight models**. A handful of affordances are Claude-Code-specific; each has a graceful fallback
so the skill still works (at worst with one manual step) elsewhere. This table is the compatibility
contract — keep it current when a skill gains a new affordance, and every skill links here.

## Affordance → fallback

| Claude-Code affordance | What it does | Fallback on another harness |
|---|---|---|
| **Frontmatter** (`name`, `description`, `argument-hint`, `allowed-tools`, `disable-model-invocation`) | Skill discovery + least-privilege tool gating | **Harmlessly ignored** — it is YAML frontmatter, not procedure. The skill **body** is the operating manual. Grant whatever tools your harness needs by its own mechanism (the committed `.agents/settings.json` is the safe baseline of what the skills run). |
| **`` !`cmd` `` injection** under "Current state (injected at load)" | Runs shell at load, pastes output into context | **Run those commands yourself** as the first action (pre-flight / Step 1). The listed commands *are* the state — if you see literal `` !`…` `` text, execute it and read the output. Most read `python3 .agents/factory/bin/paper_status.py PAPER.md --summary`. |
| **`$ARGUMENTS`** | The invocation's arguments | Use your harness's argument mechanism, or read the args from the user's message. |
| **`AskUserQuestion`** | Structured multiple-choice to the human | **Ask in plain text and STOP** for the answer. Never guess to dodge the question. |
| **`Agent` subagent fan-out** (`paper-research` survey, `paper-draft` pass B) | Parallel / fresh-context workers | **Do the work sequentially yourself**, producing the same artifacts. For `paper-research`, write the `outline/notes/refs/<bibkey>.md` briefs one at a time. For `paper-draft` **pass B this weakens *blindness*** — the whole point is a fresh reviewer that never saw the outline; compensate by doing a genuinely fresh cold read (ideally a new session) and grading claims strictly on `references.bib` + `manuscript.tex`, per the rubric — or escalate to a human reviewer. |
| **`ReportFindings`** (`paper-draft` pass B) | Renders findings in the host UI | **Additive, not load-bearing** — write the findings into the draft session log / hand them to the human directly. Skip the call. |
| **`Skill` / `/paper-*` launch** | How a skill starts | Launch by your harness's mechanism; the lifecycle handoffs ("then run `/paper-research`") are advisory prose. |

> **Scope the allowlists honestly:** the frontmatter `allowed-tools` and the committed
> `.agents/settings.json` are accident-protection, not a security boundary — `Bash(make *)` runs
> arbitrary Makefile recipes and `Bash(git commit *)` can commit anything staged. They exist to stop
> fat-fingered mutations (which is why `git checkout` — a silent working-tree discard — is deliberately
> absent; `git switch` covers real branch changes), not to confine a determined adversary.

## Already portable — no action

`git`, `make`, `python3 .agents/factory/bin/…` (the FSM scripts, `check_paper.py`, and `meta_status.py`
— all **stdlib-only**, no PyYAML, no virtualenv), file read/edit/grep/glob, and every artifact under
`outline/`, `reviews/`, and `.agents/`. All lifecycle state lives in **files** (`PAPER.md` frontmatter,
`META.md`), re-read fresh each invocation — nothing relies on Claude-specific memory. The scripts are
invoked by repo-relative path (`.agents/factory/bin/…`), not a Claude-specific variable.

## Smaller / open-weight models

The skills deliberately assume less skill/wisdom than the author, so a weaker model **fails safe** by
following the guardrails rather than guessing: STOP-and-ask on ambiguity, `[NEEDS CLARIFICATION]`
markers, the invariant gate (`invariants.md`), the blind/cold-read pass-B regime, and silence-by-default
meta-notes all degrade gracefully. When adapting a skill for another harness, keep instructions
imperative and checkable, and preserve every STOP condition — they are the safety net. Friction you hit
doing so is itself a meta-note (repo-root `META.md`) for `/paper-harness` to fix.
