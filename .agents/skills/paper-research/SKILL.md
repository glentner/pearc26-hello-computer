---
name: paper-research
description: >-
  Literature search and structured summarization for the paper, ONE source at a time and re-runnable
  (the additive analog of hs-plan's research fan-out). Given a bibkey, a URL, "find sources on
  <topic>", "next", or "status": fetches/reads the source, derives a bibkey, writes
  outline/notes/refs/<bibkey>.md from the REFNOTE template (key_findings + sample_sentences +
  supports: [C-IDs]), adds/verifies a references.bib entry, marks the source complete in the refs
  README checklist, tags the C-IDs it supports via set_status.py --add-evidence, and DRAFT-commits.
  Advances macro_phase scoped -> researching. Does NOT write section prose (that is /paper-outline).
  Second step of the paper-factory lifecycle (see .agents/factory/methodology.md).
disable-model-invocation: true
argument-hint: "<bibkey> | <url> | find sources on <topic> | next | status"
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch, Agent, Bash(git status *), Bash(git branch *), Bash(git rev-parse *), Bash(git log *), Bash(git add *), Bash(git commit *), Bash(python3 .agents/factory/bin/*)
---

# paper-research — one source, deep-dived and folded in

## When to Use

Invoke `/paper-research` after `/paper-start` has locked `PAPER.md` (the contract, C-IDs, and seed
references), or any time you want to fold **one more source** into the paper's evidence base. Each run
deep-dives a single source: it writes that source's REFNOTE, ensures a `references.bib` entry, ticks
the refs checklist, and links the source to the contribution claims it supports. It is **additive and
re-runnable** — run it once per source, in any order, over many sessions. It **STOPS after one
source** and reports what remains pending. It never writes section prose (that is `/paper-outline`)
and never touches `manuscript.tex`.

## References

- [`.agents/factory/methodology.md`](../../factory/methodology.md) — the lifecycle; principle 3
  (parallelism for research, never for drafting) and principle 6 (never guess).
- [`.agents/factory/claims.md`](../../factory/claims.md) — the C-ID convention; how `/paper-research`
  tags each source with the claims it supports (`evidence`).
- [`.agents/factory/invariants.md`](../../factory/invariants.md) — §3 citation integrity, §5
  reproducibility & honesty (real numbers, real sources).
- Templates: [`REFNOTE.md`](../../factory/templates/REFNOTE.md) (the per-source deep-dive shape) and
  [`CONTRACT.md`](../../factory/templates/CONTRACT.md) (where the C-IDs live).
- Rules: [`session_logs.md`](../../../rules/session_logs.md) (mandatory end-of-session log),
  [`file_deletion.md`](../../../rules/file_deletion.md) (use `/bin/rm`, not the Warp-era `del`).
- **Portability:** [`portability.md`](../../factory/portability.md) — this skill runs on any harness; if the *Current state* commands aren't auto-injected, run them yourself in Step 1, and if `AskUserQuestion` is unavailable, ask in plain text and STOP.

## User Instructions

Additional instructions provided with the invocation: $ARGUMENTS

## Current state (injected at load)

- Branch: !`git branch --show-current`
- Tree: !`git status --porcelain | head -n 20`
- Paper FSM: !`python3 .agents/factory/bin/paper_status.py PAPER.md --summary 2>/dev/null || echo "(run paper_status.py in Step 1)"`
- Refs pending: !`grep -c '^- \[ \]' outline/notes/refs/README.md 2>/dev/null || echo 0`

## Argument Parsing

Parse `$ARGUMENTS` case-insensitively. It selects **one** target source (or a report):

- `status` / `report` → run `paper_status.py`, print the refs checklist (complete / in-progress /
  pending N/M) and the C-IDs still lacking evidence; **do no work**, write no files, no commit.
- `next` (or empty `$ARGUMENTS`) → pick the **first** `- [ ]` (pending) entry from
  `outline/notes/refs/README.md` as the target. If none are pending, report "all sources deep-dived"
  and stop.
- A token matching an existing bibkey (`^[a-z]+[0-9]{4}[a-z0-9]*$`, e.g. `deelman2025hpc`) → that is
  the target; its REFNOTE may already exist (refresh it) or be pending.
- A URL (`http(s)://…`) → fetch it, then derive a bibkey (Step 2).
- `find sources on <topic>` / `survey <topic>` → **topic mode**: optionally fan out read-only survey
  subagents (Step 2a), then deep-dive the **single** best candidate this run.
- Anything else → treat as a free-text source description or topic; if it is too vague to identify one
  source, emit `[NEEDS CLARIFICATION: which source/topic?]` and ask (AskUserQuestion is not in scope —
  ask in prose and STOP).

If the argument is self-contradictory (e.g. a bibkey and a URL that disagree), STOP and ask.

## Safety Principles

- **Work on `draft`; commits are `DRAFT:`-prefixed.** If the injected branch is not `draft`, STOP and say
  so (shipping to `main` is `/paper-release`'s job, never this skill's).
- **Read state first, mutate only via the scripts.** Run `paper_status.py` before doing anything;
  advance the FSM (`macro_phase`, claim evidence) **only** with `set_status.py`. Never hand-edit
  `PAPER.md` frontmatter.
- **Additive and serial for writes.** This run writes exactly **one** REFNOTE. You **may** fan out
  read-only `Agent` subagents to *survey* candidate sources (topic mode) — they read/search only and
  return briefs; they **never write** files. Only this orchestrator writes, and it writes one source's
  notes serially (methodology principle 3).
- **Never guess (principle 6).** If the source is ambiguous, its bibkey unclear, or which C-IDs it
  supports is genuinely uncertain, emit a literal `[NEEDS CLARIFICATION: …]` and ask. An **unresolved
  `[NEEDS CLARIFICATION]` marker anywhere in `PAPER.md` blocks research** — STOP and send the human to
  resolve it (or back to `/paper-start`).
- **Real sources, real evidence (invariants §3, §5).** Only cite a source you actually fetched/read;
  bibkey a source only from its true metadata; link a C-ID to a source **only if the source genuinely
  supports that claim**. Do not invent authors, DOIs, or a supporting relationship to make the FSM
  look complete.
- **No prose, no LaTeX.** Do not write section `## Draft` prose and do not touch `manuscript.tex` —
  those are `/paper-outline` and `/paper-draft`.
- **Deletion via `/bin/rm`** (never the repo's Warp-era `del` alias); see `file_deletion.md`.
- **Session log is mandatory** (see `session_logs.md`): this orchestrator writes
  `logs/<UTC-ISO>-<slug>.md` at the very end, capturing the VERBATIM `$ARGUMENTS` as `user_input`.
- **STOP after one source.** Report pending sources and let the human decide whether to re-run.

## Procedure

### Step 1 — Pre-flight & read state
1. Confirm the branch is `draft` (from the injected state). If not, STOP.
2. Run `python3 .agents/factory/bin/paper_status.py` and read the JSON: `macro_phase`,
   `claims_total`, `claims_lacking_evidence`, `refs{complete,in_progress,pending}`, `warnings`. Exit 2
   means `PAPER.md` is invalid — STOP and report.
3. Grep `PAPER.md` for `[NEEDS CLARIFICATION`. If any unresolved marker exists, STOP (research is
   blocked until it is resolved).
4. If `$ARGUMENTS` is `status`/`report`, print the state summary + refs checklist + C-IDs lacking
   evidence and **stop here** (no work).
5. If `macro_phase` is `scoped`, advance it:
   `python3 .agents/factory/bin/set_status.py PAPER.md --macro-phase researching`. (If already
   `researching`/`outlining`/`revising`, leave it; do not regress a later phase — note it and
   proceed. If `released`, ask the human whether this is a genuine post-release addition before
   continuing.)

### Step 2 — Resolve the target source & bibkey
1. Per Argument Parsing, resolve the single target: a bibkey, a URL, the next `- [ ]` from the refs
   README, or (topic mode) a chosen candidate.
2. **Fetch/read it.** Use `WebFetch`/`WebSearch` for a URL or online source, `Read` for a local PDF or
   file already in the repo. For a `next`/bibkey target that already has an `outline/notes/refs/*.md`,
   read it to refresh rather than duplicate.
3. **Derive the bibkey** from the source's real metadata: `firstauthorlastname` + `year` + short
   topic slug (e.g. `deelman2025hpc`, `anthropic2024mcp`), lowercase, matching the existing scheme in
   `references.bib` and the refs README. If a bibkey was given, use it verbatim. If the correct bibkey
   is ambiguous, emit `[NEEDS CLARIFICATION]` and ask.

### Step 2a — Optional survey fan-out (topic mode only)
For `find sources on <topic>`, you may launch a small number of **read-only** `general-purpose`
`Agent` subagents, breadth-first, one per sub-topic. Each gets: the topic + the paper's thesis/C-IDs
(from `PAPER.md`) + explicit scope bounds + "search/read only; return a ≈1k-token brief of candidate
sources (title, authors, year, URL, one-line relevance to which C-ID); **do not write any file**."
Consume each subagent's returned brief; NEVER read its `.output` transcript sidecar — that floods
context. Read the briefs, pick the **single** strongest candidate for this run (prefer one that fills a
C-ID currently lacking evidence), and proceed. Log the candidates you found so future runs can pick them
up (e.g. add pending `- [ ]` lines to the refs README). Do **not** deep-dive more than one this run.
If subagents are unavailable, do the survey yourself sequentially — same `outline/notes/refs/<bibkey>.md`
output, only parallelism is lost (see [`portability.md`](../../factory/portability.md)).

### Step 3 — Write the REFNOTE
Write `outline/notes/refs/<bibkey>.md` from [`REFNOTE.md`](../../factory/templates/REFNOTE.md).
Frontmatter carries the machine-useful fields — `bibkey`, `title`, `authors`, `year`, `source_type`,
`url`, `status: complete`, `key_findings` (bulleted, factual), `sample_sentences` (paraphrase-ready
prose for `/paper-outline`), and `supports: [C-IDs]` (the claims this source backs). The body is the
long-form deep-dive: overview, core arguments, and a **Relevance to Our Paper** section that names the
C-IDs and the sections that will use it. Keep numbers and quotes faithful to the source (invariants
§5). Match the shape of the existing notes (e.g. `outline/notes/refs/deelman2025hpc.md`).

### Step 4 — Add / verify the `references.bib` entry
Ensure `references.bib` has a BibTeX entry keyed exactly `<bibkey>` with the correct type
(`@article`/`@misc`/`@inproceedings`/…) and real fields (author, title, year, and DOI/URL where
they exist). If the entry already exists, verify it matches the source and fix drift; if not, append a
new one. The key **must** be identical to the REFNOTE bibkey — `check_paper.py` proves citation
integrity later, so get the key right now.

### Step 5 — Mark the source complete in the refs checklist
In `outline/notes/refs/README.md`, flip the target's line to `- [x]` (add the line if the source is
new, under the right category, with the `bibkey — Authors Year — Title` format). Update the running
**Completed: N/M** count and the "(M total)" header so the checklist and the `paper_status.py`
`refs{complete,pending}` counts stay in sync.

### Step 6 — Tag the C-IDs this source supports
For **each** C-ID the source genuinely backs (the `supports:` list from Step 3), link it:
```
python3 .agents/factory/bin/set_status.py PAPER.md --claim <Cx> --add-evidence <bibkey>
```
This is idempotent. It links evidence only; it does **not** upgrade a claim's `status` to
`supported` — that honesty judgment belongs to `/paper-outline`/`/paper-draft` (claims.md,
invariants §5). If the source supports no C-ID (pure background), skip this step and note it.

### Step 7 — Meta-note (silence by default)
Before committing, ask ONE question: *did the skill itself (not you, not the task) cost something this
run?* Almost always the answer is no — **silence is the default; most runs add nothing.** If yes AND it
clears the bar in `.agents/factory/templates/META.md`, append a `## F<n>` finding to the **repo-root
`META.md`** (create it from `.agents/factory/templates/META.md` if absent): a metadata line
`origin=paper-research:<step> severity=<high|medium|low> category=<instruction|steering|tooling|template|missing-guidance> status=open target=<best-guess file>`
plus the **What happened / Skill cause / Recommended fix / Confidence · Effort** bullets. Keep it to ≤3
findings; if an equivalent finding exists, append "· seen again" to its title rather than duplicating. A
content/task issue is NOT a finding — it belongs in `PAPER.md` **Clarifications**, a `reviews/` note,
or a `[NEEDS CLARIFICATION]` marker. Add `META.md` to that step's `git add`. You only *record*;
the human-gated `/paper-harness` is what later applies these.

### Step 8 — DRAFT commit + session log
1. Stage the artifacts and commit:
   ```
   git add outline/notes/refs/<bibkey>.md references.bib outline/notes/refs/README.md PAPER.md META.md
   git commit -m "DRAFT: deep-dive <bibkey>" -m "Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
   ```
   Do not push.
2. Write the mandatory session log to `logs/<UTC-ISO>-deep-dive-<bibkey>.md` (timestamp via
   `date -u +"%Y-%m-%dT%H-%M-%S"`), with the **verbatim** `$ARGUMENTS` as `user_input`, the files
   modified, the commit, and a short summary. (The orchestrator writes this from the live
   conversation, per `session_logs.md`.)

### Step 9 — Report & stop
Report: the bibkey deep-dived, the C-IDs it now backs, the updated refs count (N/M), any C-IDs still
lacking evidence, and the remaining pending sources. Recommend re-running `/paper-research next` for
the next source, or `/paper-outline` once the evidence base is deep enough to fold into a section.
**Stop** — one source per run.

## Examples

- `/paper-research next` — pick the first pending `- [ ]` from the refs README, deep-dive it, tag its
  C-IDs, commit `DRAFT: deep-dive <bibkey>`, stop.
- `/paper-research deelman2025hpc` — (re)write the REFNOTE for a known bibkey and re-verify its bib
  entry and claim links.
- `/paper-research https://arxiv.org/abs/1706.03762` — fetch the URL, derive `vaswani2017attention`,
  write its notes + bib entry.
- `/paper-research find sources on MCP security confinement` — fan out read-only survey subagents,
  pick the strongest candidate, deep-dive that one.
- `/paper-research status` — print the FSM phase, the refs N/M checklist, and C-IDs lacking evidence;
  no work.

## Notes

- Re-runnable by design: state lives in the committed `PAPER.md` + refs README, re-read each run via
  `paper_status.py`. It is safe to stop after any source and resume days later.
- The `supports:` link is a *claim → source* edge, not a promise the claim is proven — `/paper-outline`
  folds the evidence into section prose and `/paper-draft` pass B blindly audits whether the cited
  evidence actually backs each claim (claims.md, review-rubric.md).
- If a source turns out **not** to support the C-ID you expected, say so and cut the link — honesty
  over a full-looking evidence list (invariants §5).
- Survey subagents are read-only and never write files; if you want their candidates persisted, add
  them yourself as pending `- [ ]` lines in the refs README.
