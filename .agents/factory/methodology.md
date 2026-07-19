# The paper factory — methodology

This is the reference an agent reads to understand the research lifecycle that the `/paper-*`
skills implement. The skills themselves are thin; this is the *why*. When something here disagrees
with a skill, **the skill body is the operating procedure** — fix this file.

> **New here (human or agent)?** Start with [`getting-started.md`](getting-started.md) — a narrative,
> end-to-end walkthrough of writing a research article as an agent-first workflow, written for the
> research community at large. This file is the terse rationale; that one is the guided tour.

It is adapted from the HyperShell "software factory" (`hs-*` skills). The port is deliberate, not
literal: a software feature flows once through a linear FSM (shape → plan → build → review → ship); a
paper is **cyclic and additive** — you research a new source, fold it in, integrate, get external
feedback, and loop. We keep the factory's *principles* and rebuild its artifacts for research.

## The lifecycle

One paper flows through six skills. State lives in the repo-root `PAPER.md` (the contract + FSM);
content lives at the repo root (`outline/`, `reviews/`, `plans/`, `logs/`, `manuscript.tex`).

```
                      ┌─────────────── /paper-review ◀── external peer feedback
                      ▼                     (re-runnable per cycle)
 /paper-start   ─▶ /paper-research ─▶ /paper-outline ─▶ /paper-draft ─▶ /paper-release
   (scope: PAPER.md   (per source:      (per section:      (outline →      (draft → main,
    + outline          refs notes +      fold evidence      manuscript.tex   tag, TAPS zip)
    skeleton)          references.bib)   into ## Draft)     A: integrate
      │                    ▲   │              ▲   │         B: audit)
   macro_phase:            └───┘  (additive)  └───┘ (re-run per section/source)
   scoped → researching → outlining → integrating → in-review → revising → released
                                          ▲                          │
                                          └──────────────────────────┘  (revising re-enters)
```

- **`/paper-start`** — scope a NEW paper: venue/template, thesis, contribution claims (C-IDs),
  non-goals, seed references, section skeleton. Produces `PAPER.md` + the `outline/` skeleton. STOPs
  for sign-off before any research spend. *(hs-feature analog.)*
- **`/paper-research`** — literature search + structured summarization, **one source at a time,
  re-runnable**. Writes `outline/notes/refs/<bibkey>.md` and a `references.bib` entry; tags the
  C-IDs the source supports. *(hs-plan's research fan-out, made additive.)*
- **`/paper-outline`** — fold research + snippets into a section's `## Draft` prose. Serial,
  single-voice, re-runnable per section. Advances a section `draft → review`. *(hs-build, for prose.)*
- **`/paper-draft`** — render the outline source-of-truth into `manuscript.tex` in two passes:
  **A** delta-integration, **B** verification (cold-read fidelity + blind claim/citation/invariant
  audit). Advances sections `review → integrated`. *(hs-build render + hs-review's blind check.)*
- **`/paper-review`** — ingest EXTERNAL peer feedback (transcript/email/PDF): capture → distill
  (`FB-N.NN`) → synthesize → write a revision plan; loops the paper back to `revising`. *(the slot
  hs-publish occupied, reinterpreted — external, human-paced, cyclic.)*
- **`/paper-release`** — ship `draft → main`: strip `DRAFT:` prefixes, fast-forward merge, tag, ACM TAPS
  package, optional GitHub release. *(the release mechanics of the existing `/release` skill.)*

The artifact spine — **`PAPER.md` (claims + FSM) → `outline/` (drafts) → `manuscript.tex` (derived)
→ `reviews/` (external feedback)** — is committed as a dated, public record. The *process is the
contribution* (claim C5): we build in the open.

## Load-bearing principles

1. **Files + git are the durable substrate.** State lives only in the committed `PAPER.md`
   frontmatter, re-read fresh each invocation via `paper_status.py`. Never rely on conversation
   memory to carry lifecycle state — `/paper-draft`'s audit runs in a separate context, and a skill
   may run days later. The circuit breakers are file-backed for the same reason: a section's
   `attempts` (the internal draft↔audit loop) and `review.cycle` (the external review↔revise loop)
   live in `PAPER.md`, so a non-converging loop is still visible after a context reset
   (`paper_status.py` warns at `attempts ≥ 3`).
2. **The script owns the fragile serialization.** Advance state with `set_status.py`, never by
   hand-editing `PAPER.md` frontmatter. All human free-text (claim statements, the LaTeX heading
   map) lives in the `PAPER.md` *body*, which the scripts preserve verbatim — so the machine subset
   in the frontmatter stays trivially safe to round-trip. See `bin/_fsm.py`.
3. **Parallelism for research, never for drafting.** `/paper-research` may fan out read-only
   subagents to survey sources. `/paper-outline` and `/paper-draft` are strictly single-threaded and
   serial — parallel writers make conflicting voice/structure decisions in one manuscript.
4. **Cold-read and blind verification beat self-review.** `/paper-draft` pass B delegates to a
   **fresh subagent**: a cold-read fidelity check (outline vs. tex) and a *blind* claim-support +
   citation-integrity audit (the reviewer sees the claims + `references.bib` + `manuscript.tex`, not
   the outline rationale). Enforced by spawning subagents, not by trusting a `/clear`. See
   `review-rubric.md`.
5. **Ceremony scales to appetite.** The appetite here is the **page/word budget** (a PEARC extended
   abstract is 4 pages). Scope is cuttable to fit; `make check` reports the page count. Do not
   manufacture claims or sources beyond what the budget and thesis need. **But quality is not
   negotiable:** the page budget is cuttable *appetite*; citation integrity, claim support, and
   outline↔manuscript fidelity are `must-fix` (see `invariants.md` / `review-rubric.md`), never
   scope-hammered to fit.
6. **Never guess.** Ambiguity gets a literal `[NEEDS CLARIFICATION: …]` marker and a question to the
   human, recorded in `PAPER.md`. An unresolved marker blocks `/paper-research`.
7. **Verify deterministically where you can.** Citation integrity, prose conventions, and page/word
   budget are mechanically checkable — `check_paper.py` (`make check`) catches them so the cold-read
   pass can focus on meaning.
8. **Observe cheaply, act deliberately.** Recording friction with the *toolchain itself* is near-free —
   every producer skill can append a silence-by-default `## F<n>` note to the repo-root `META.md`.
   Acting on it is careful: only the human-gated `/paper-harness` applies findings, one previewed
   atomic `[harness]` commit each, and it may **never** quietly weaken an invariant. This asymmetry is
   the self-improvement loop (below).

## The self-improvement loop

The factory improves itself the same way it writes the paper: files + git, script-owned state, a human
gate. It is **orthogonal** to the paper lifecycle — it improves the *toolchain*, not the manuscript —
and is meta/maintenance, not a `macro_phase`.

```
producers ───▶ META.md ───▶ paper-release ───▶ /paper-harness ───▶ harness-log.md
(start/research/    (repo root;   surfaces open     applies (human-      (ledger; TRAVELS
 outline/draft/      silence by    findings at        gated, one atomic    to the next paper;
 review append        default)      ship time,         [harness] commit     read first,
 ## F<n> findings)                  non-blocking)      per fix)             anti-thrash)
```

- **`META.md`** (repo root, beside `PAPER.md`): the friction log. A producer appends a `## F<n>`
  finding only when *the skill itself* cost something — the bar is "was this the skill's fault, not
  mine, not the task's?". Read via `meta_status.py`. **Left behind** when the `.agents/` tree is copied
  to bootstrap a new paper (findings are paper-specific); the ledger is what travels.
- **`/paper-harness`**: the only skill that writes `.agents/`. Reads open findings + the ledger, shapes
  with the human, previews a re-derived diff per fix, applies one atomic `[harness]` commit each
  (directly on `draft`, keeping the co-author trailer), and **never** auto-weakens `invariants.md` — a
  finding that argues to loosen a gate is itself a warning sign.
- **`harness-log.md`** (`.agents/factory/`): the decision ledger, read first by `/paper-harness`
  (anti-thrash: a fix that reverts a recent change or repeats a rejected one is flagged). Unlike
  `META.md`, it **travels** with the copied tree — cross-paper memory of what worked.

Single-paper adaptations vs. the upstream hypershell loop: one repo-root `META.md` (no per-feature
`spec/{slug}/` portfolio, no `--all`); `[harness]` commits go directly on the single `draft` branch (not
via a develop/PR split); and the co-author trailer is **kept**, not dropped (this is a public
replication package).

## What we borrow from the software factory (and what we discard)

**Adopt:** the artifact spine + stable-ID traceability; script-owned FSM state; blind/cold-read
verification; `[NEEDS CLARIFICATION]` over guessing; appetite (as page budget); "build in the open."

**Adapt:** hs-build splits into TWO activities — research→outline *prose* (`/paper-outline`) and
outline→*LaTeX* (`/paper-draft`). hs-review (internal QA) becomes `/paper-draft` pass B; the external
peer-review discipline becomes `/paper-review` (a genuinely new phase). EARS requirements become
plain contribution **claims** (see `claims.md`) — a paper asserts, it does not specify triggered
behavior.

**Discard:** the per-phase dependency DAG (a 4-page paper's ~7 sections rarely have hard build
order — we track a *writing* `order` and status buckets instead of a topological gate); the
`hammerable`/`hill`/`parallel` software honesty signals; PyYAML (stdlib-only for a LaTeX repo).

## Where things live

```
.agents/
  skills/paper-{start,research,outline,draft,review,release}/SKILL.md   # the six lifecycle skills
  skills/paper-harness/SKILL.md   # meta/maintenance: the self-improvement applier (writes .agents/)
  factory/
    getting-started.md    # narrative end-to-end walkthrough (start here)
    methodology.md        # this file
    invariants.md         # the paper-invariants gate (draft pass B + /paper-review + check_paper.py)
    claims.md             # the contribution-claim (C-ID) convention
    review-rubric.md      # refutation protocol, severity scale, blind/cold-read regimes
    portability.md        # running the factory on a non-Claude harness (affordance -> fallback)
    harness-log.md        # the self-improvement decision ledger (TRAVELS to the next paper)
    templates/            # CONTRACT / REFNOTE / REVIEW-FEEDBACK / REVIEW-SYNTHESIS / REVISION-PLAN / META
    bin/                  # paper_status.py, set_status.py, check_paper.py, meta_status.py, _fsm.py (stdlib)
PAPER.md                  # this paper's contract + FSM state (content; at repo root)
META.md                   # this paper's harness-feedback log (repo root; left behind on tree-copy)
outline/ reviews/ plans/ logs/ manuscript.tex references.bib   # content + public record
AGENTS.md                 # the constitution (CLAUDE.md is a symlink to it)
```

`.claude` is a symlink to `.agents`, so Claude Code discovers the skills and settings through it.
To bootstrap a new paper, copy the `.agents/` tree.

## Traceability chain

`PAPER.md` C-IDs → section `satisfies:` → `outline/` drafts → `\cite` keys in `manuscript.tex` →
`references.bib`; and, in the reverse direction, external `reviews/` → `FB-N.NN` feedback items →
`plans/N-revision.md` → reopened sections. `paper_status.py` reports both the forward spine (claims
lacking evidence) and drift; `check_paper.py` proves citation integrity. The committed files *are*
the retained trace — provenance lives in git + these artifacts, not in the LaTeX source.
