# GETTING STARTED — *Shall We Play a Game?*

> An end-to-end walkthrough of writing a research article as an **agent-first** workflow, using the
> portable "paper factory" in this repository. Part adventure game, part field manual, wholly serious.
> Written for **the research community** — the scientists, and the people who fund, review, publish, and
> convene them — who are curious what this could actually look like, and uneasy about what it means.

```
    ┌────────────────────────────────────────────────────────────┐
    │                                                            ▓ │
    │   GREETINGS PROFESSOR.                                      ▓ │
    │                                                            ▓ │
    │   HELLO, COMPUTER.                                          ▓ │
    │                                                            ▓ │
    │   A STRANGE GAME.                                          ▓ │
    │   WOULD YOU LIKE TO WRITE A PAPER?                          ▓ │
    │                                                            ▓ │
    │   > _                                                       ▓ │
    └────────────────────────────────────────────────────────────┘
```

You are standing at a terminal. In front of you is a blank manuscript and a machine that will, if you
let it, read every paper you point it at, draft prose in your voice, wire up your citations, and argue
with itself about whether it got the argument right. Behind you is a research culture that is not sure
it trusts the machine — and a funding landscape that has just declared the machine a national priority.

This document is a map through that contradiction. It walks the real production of the paper you are
sitting inside — *Hello Computer: HPC in the Agentic Era* — from an empty repository to sixteen tagged
releases, and it documents the reusable machinery ("the factory") that made the trip repeatable. The
paper argues that for research-computing facilitators, **proactive engagement, not prohibition, is the
path forward.** This file is what that engagement looks like at ground level, with the cheats and the
guardrails both on the table.

---

## A STRANGE GAME — the stakes

In *WarGames* (1983), a computer learns that some games cannot be won, only survived: *the only winning
move is not to play.* Research science in 2026 is tempted by exactly that fatalism about AI — decline
to engage, wait for the norms to settle, keep the machine outside the lab door.

The trouble is the board has already been set for us:

- **AI is distrusted — for good reasons.** Peer review was built on the assumption that a human stood
  behind every sentence. Reproducibility assumes a documented method. Journals and conferences are
  right to worry about fabricated results, uncredited generation, and confident nonsense. An agent that
  will happily write a Slurm script for a cluster you do not operate is not a colleague you trust
  unsupervised.
- **AI is also, simultaneously, a mandate.** By late 2025 the Model Context Protocol had moved to the
  Linux Foundation; the U.S. *Genesis Mission* executive order had charged the national laboratories
  with uniting supercomputers and AI for scientific discovery; and serious voices were describing
  high-performance computing as standing "at a crossroads." The same institutions that distrust the
  machine are being told to build on it.

That is the uncomfortable middle we are documenting: **untrusted yet imperative.** You cannot resolve
it by picking a side. You resolve it the way you resolve any hard experiment — by making the method
explicit, the evidence inspectable, and the failure modes cheap to catch. This paper was written to be
that evidence: **126 commits, 16 public releases, 63 timestamped session logs** — roughly 90 hours of
human effort across six months — every keystroke of the process open to inspection. Not because the
process is finished, but because it is *legible* — and a legible method is one the community can critique,
reproduce, and improve.

> **THE STAKES — a note to the people who set the rules.**
> If you fund research, edit a journal, chair a program committee, or run a lab: the question is no
> longer *whether* researchers use these tools (they do), but whether the **process is disclosed and
> reproducible** when they do. This factory is one concrete answer — an auditable, honest, agent-first
> pipeline whose every artifact is committed in the open. Treat what follows as a proposal you are
> invited to stress-test, adopt, or replace with something better. The winning move is not to abstain;
> it is to write the rules of play while the game is still young.

---

## HOW TO PLAY THIS DOCUMENT

This file speaks in two voices, and you should read both:

```
  THE GAME     narrative flavor — the lifecycle as a text adventure. Skimmable; it carries the shape.
  FIELD NOTES  the serious, load-bearing content — why each move matters, and how to actually do it.
```

You do **not** need to have played a text adventure, run an agent, or written LaTeX to follow along.
Where a command appears like `> /paper-research`, that is a real skill you can invoke; where the
computer "speaks" in a `boxed CRT panel`, that is flavor. The full, dry reference for every tool is the
**appendix** at the end — this walkthrough stays narrative on purpose.

---

## THE MAP — the world you are about to explore

A paper is not a straight line; it is a small world you walk, sometimes in circles. The factory models
that world as a **finite-state machine** — a set of named places (`macro_phase`s) you move between, with
the *rules of the world* enforced by scripts, not by memory.

```
                             ┌──────────────────────────────────────────┐
                             │              THE WORKSHOP                  │
                             │   /paper-harness  ·  the tools improve     │
                             │   themselves (meta/maintenance)            │
                             └───────────────▲──────────────────────────┘
                                             │ findings ride back
   NEW GAME                                  │
     │                                       │
     ▼                                       │
  ┌─────────┐   ┌─────────────┐   ┌──────────┴──┐   ┌──────────────┐   ┌───────────┐
  │ SCOPED  │──▶│ RESEARCHING │──▶│  OUTLINING  │──▶│ INTEGRATING  │──▶│ IN-REVIEW │
  │ contract│   │  the stacks │   │  the desk   │   │  the press   │   │ the arena │
  └─────────┘   └─────────────┘   └──────▲──────┘   └──────▲───────┘   └─────┬─────┘
   /paper-       /paper-           /paper- │          /paper-│                 │
   start         research          outline │          draft  │                 ▼
                     ▲                      │                 │           ┌──────────┐
                     └──────────────────────┴─────────────────┴──────────│ REVISING │
                        (additive: new source, new section, any time)     └────┬─────┘
                                                                               │
                                                                               ▼
                                                                        ┌────────────┐
                                                                        │  RELEASED  │──▶ ship it
                                                                        │  the gate  │   /paper-release
                                                                        └────────────┘
```

You are never "stuck on rails." Research is **additive and cyclic**: a new source can send you back to
the stacks; a reviewer can reopen a finished section; a released paper can begin a new revision. The map
just makes sure you always know *where you are* and *what is actionable next* — ask the world at any
time with `> paper_status.py`.

---

## YOUR PARTY & YOUR TOOLS

**No prose was written by hand** — not one bit of it. Humans defined the goals, the non-goals, and the
rules, curated the sources, and gave the reviews their feedback; the agent did the research, the drafting,
and the integration. Prompting was manual at first, then procedural, and now — through the workshop — self-improving.

**The party.** You (the researcher, and your co-authors) are the players and the *judges* — every
verdict, every claim, every "yes this is true," is yours. The **agent** is the tireless co-player at
the parser: it reads, drafts, wires, and critiques, but it never gets to decide the paper is done. That
division is the whole game.

**Your commands** (the seven `/paper-*` skills — your verbs in this world):

```
  > /paper-start      scope a NEW paper: thesis, claims, non-goals, section skeleton
  > /paper-research   deep-read ONE source; write a note; wire it to a claim
  > /paper-outline    fold that evidence into a section's prose (markdown, no LaTeX yet)
  > /paper-draft      render the outline into manuscript.tex, then have a blind critic check it
  > /paper-review     ingest a human peer review; turn it into tracked, actionable feedback
  > /paper-release    ship draft → main: tag, package, publish
  > /paper-harness    (meta) turn friction with the TOOLS into fixes to the tools
```

**The engine** (the scripts that enforce the world's rules so the model can't quietly corrupt them):

```
  paper_status.py   "look" — where am I, what's next, what's unproven, what's drifted?
  set_status.py     "move" — advance a section/claim/phase (never hand-edit the save file)
  check_paper.py    "the referee" — citations resolve? prose clean? within the page budget?
  meta_status.py    "the suggestion box" — what friction did the tools cause?
  _fsm.py           the rules engine the others share (stdlib only; no dependencies to install)
```

> **FIELD NOTES — why an "engine," and why scripts.**
> The single most common way an AI workflow rots is that the agent edits its own state by hand and
> corrupts it — a dropped quote here, a mangled indent there, and the "source of truth" quietly lies.
> The factory's answer is old-fashioned: **files + git are the durable substrate, and a *script* owns
> every fragile edit.** The paper's live state lives in one file, `PAPER.md`; you read it with
> `paper_status.py` and change it with `set_status.py`, and the scripts refuse to write anything that
> would not validate. The model proposes; the engine disposes. This is the difference between "the AI
> keeps track" (it won't) and "the AI operates a tracker it cannot silently break" (it can).

---

## THE PLAYTHROUGH

What follows is the *actual* route this paper took — not a hypothetical. Numbers are real and taken from
the repository you are in.

### LOCATION 0 — THE CONTRACT (`scoped`)

```
  You open a blank repository. A voice asks: what are you actually claiming, and how will you know
  if you failed?
  > /paper-start Let's start a new paper about the latest changes we've made at the center to
    address the needs of users in the agentic era.
```

Before a single source is read, you write the **contract**: the thesis in a sentence, three-to-five
falsifiable **contribution claims** (stable ids `C1`, `C2`, …), the **non-goals** (what this paper is
deliberately *not*), the venue and page budget, and a skeleton of sections. `/paper-start` writes all
of this into `PAPER.md` and scaffolds the `outline/` — then **stops** and hands you back the pen for
sign-off. It will not proceed on a guess: genuine ambiguity becomes a literal `[NEEDS CLARIFICATION]`
marker and a question to you.

> **FIELD NOTES — a hypothesis pre-registration, for prose.**
> Scoping first is not bureaucracy; it is the paper's analog of pre-registering a hypothesis. The
> contribution claims become a spine that everything downstream is checked against: a source is logged
> as *evidence for `C2`*; a section is marked as *arguing `C3`*; the final audit asks *is each claim
> actually supported?* Naming your non-goals up front is how a four-page abstract stays four pages. The
> discipline is cheap here and priceless later.

### LOCATION 1 — THE STACKS (`researching`)

```
  A library that never closes. You may summon a source, and the machine will read all of it.
  > /paper-research vaswani2017attention
```

Literature review, **one source at a time**, re-runnable. For each source `/paper-research` fetches and
reads the real thing, writes a structured deep-dive note (`outline/notes/refs/<bibkey>.md` — key
findings, reusable sentences, and *which claims it supports*), adds a `references.bib` entry, and ticks
the running checklist. This paper's bibliography was built exactly this way: **thirteen sources, across
fifteen context windows, over roughly eight hours** of deliberate prompting — every one annotated,
every one committed.

> **FIELD NOTES — the machine reads; the human still decides what it means.**
> An agent is extraordinary at the *labor* of a literature review — reading in full, summarizing
> faithfully, never getting bored on source eleven. It is not a substitute for judgment about what
> matters. The note format keeps the two separate: the agent produces the summary and the candidate
> sentences; you decide which claim they actually back. Provenance is not a comment buried in the LaTeX;
> it is the chain `claim → section → source`, inspectable at any time.

### LOCATION 2 — THE DESK (`outlining`)

```
  A wide wooden desk. Notes on the left, a section on the right, and a rule pinned above it:
  ONE VOICE.
  > /paper-outline 03-approach
```

Now the evidence becomes *prose*. `/paper-outline` folds the research notes and reusable fragments into
a section's working draft — in markdown, deliberately, to avoid LaTeX friction while the writing is
still soft. It runs **one section at a time and strictly single-voice**: you never fan this step out to
parallel writers, because a paper with five ghostwriters reads like it. When a section's draft settles,
its status advances `draft → review`.

> **FIELD NOTES — parallel to read, serial to write.**
> The factory fans agents out for *research* (many sources, read independently — a big win) and forbids
> it for *drafting* (one manuscript, one argument, one voice). This is a general principle worth
> stealing: parallelism is free where the work is genuinely independent and toxic where it forces
> conflicting implicit decisions. Prose is the latter.

### LOCATION 3 — THE PRESS (`integrating`)

```
  A printing press, and beside it, a second reader who has never seen your notes and is instructed
  to distrust you.
  > /paper-draft
```

`/paper-draft` renders the settled outline into the single `manuscript.tex` in **two passes**. **Pass A**
integrates the prose under the correct LaTeX headings (a map kept in `PAPER.md`, seeded from the live
manuscript, not from memory), preserving every citation and honoring the house conventions. **Pass B**
is the interesting one: a **fresh agent, in a clean context, is asked to check the work** — a cold read
comparing outline to manuscript sentence-by-sentence, and a *genuinely blind* audit that sees the
claims, the bibliography, and the manuscript but **not** the author's outline rationale, and asks: is
each claim actually supported? It **reports and stops.** Nothing advances to `integrated` until a human
signs off.

> **FIELD NOTES — the hardest problem in AI-assisted work is grading your own homework.**
> A model asked "is this good?" about its own output says yes. The factory's defense is structural, not
> hopeful: the reviewer is a *different* invocation, denied the rationale that would let it rubber-stamp
> its own reasoning, and required to cite specific evidence for every complaint. This is the same move
> peer review makes — a fresh, disinterested reader — mechanized. It does not make the AI trustworthy on
> its own say-so. It makes the *output inspectable* by someone (or something) that did not write it.
> That is the difference the research community should be asking for: not "trust the model," but "show
> me the independent check."

### LOCATION 4 — THE ARENA (`in-review`) and the LOOP (`revising`)

```
  A round table of colleagues, unimpressed. They will not be automated away.
  > /paper-review reviews/review_phase_2.md
```

Real papers meet real reviewers. `/paper-review` ingests an **external human review** — a call
transcript, an email, committee notes — and turns it into a tracked spine: verbatim capture, then
distilled feedback items (`FB-1.01`, `FB-1.02`, …) each tagged with a type, a severity
(`must-fix | should-fix | consider`), the reviewer's exact words, and an action; then a synthesis of
cross-cutting themes; then a revision plan. It sets the world back to `revising` and reopens the
affected sections. This paper went through **two full review phases** (the first captured in three
parts) before it was allowed to ship.

> **FIELD NOTES — humans stay the judges; the agent keeps the books.**
> Notice what is and isn't automated. The *judgment* — what's wrong, what matters, what to keep — is
> human, and stays human. What the factory automates is the bookkeeping that peer feedback usually dies
> in: the mapping from "reviewer 2 disliked the abstract" to a specific, tracked, resolvable change in a
> specific section. Feedback that is merely *heard* evaporates; feedback that is *tracked* gets
> addressed. This is where a lot of good criticism is quietly lost today, and where the machine earns
> its keep without touching the judgment.

### LOCATION 5 — THE GATE (`released`)

```
  A gate marked SHIP IT. It will not open if the paper is over length, if a citation dangles, or if
  a reviewer's "must-fix" is still open.
  > /paper-release minor version bump with tag and release
```

`/paper-release` ships `draft → main` behind a **release guard**: the paper must build, must pass the
deterministic checks (`make check`), and must not be carrying unresolved must-fix feedback or shipping a
manuscript that was never audited — any of those requires an explicit human override, on the record.
Then it tags a version, packages the camera-ready archive, and publishes. This paper passed that gate
**sixteen times** (`v0.1.0` through `v1.1.0`): shipping early and often, in the open, is itself the
argument.

> **FIELD NOTES — "build in the open" as a research value.**
> Sixteen tagged releases and 63 session logs are not vanity. They are the reproducibility story for a
> *process* rather than a result: anyone can watch the paper think. For a community wrestling with how
> to trust AI-assisted work, this is a concrete disclosure standard — not "we used AI" in a footnote,
> but the entire, inspectable trail of how. If journals and conferences want a bar higher than a
> checkbox, this is what one looks like.

---

## THE RULES OF THE GAME — there are no cheat codes

Every game has rules you cannot break without voiding the win. In this one they are called
**invariants**, and they are the reason AI-assisted output can be trusted at all:

```
  ✗ over the page budget            ✗ a \cite with no entry (or an entry never cited)
  ✗ a claim with no evidence        ✗ the manuscript drifting from its source outline
  ✗ an undisclosed use of AI        ✗ an invented number, a moved goalpost, a silent scope cut
```

`check_paper.py` (via `make check`) enforces the mechanical ones on every ship; the blind audit and the
human gate enforce the rest. Crucially: **quality is not the cuttable variable.** Scope is
cuttable — that is what the page budget and the non-goals are for. Citation integrity, claim support,
fidelity, and honest disclosure are `must-fix`, never "hammered to fit." An AI workflow that will loosen
its own guardrails to make a deadline has learned the wrong lesson; here, a finding that *argues* to
weaken a gate is treated as a warning sign, not an instruction.

> **THE STAKES — this is the trust contract.**
> The distrust of AI in science is, at bottom, a fear that the guardrails are gone. The answer is not to
> promise the model is wise. It is to make the guardrails *explicit, mechanical, inspectable, and
> self-improving* — and to let a disinterested checker enforce them. The invariants above are a starting proposal for what
> "responsible AI-assisted authorship" could concretely mean. Improve them; but do not ship without
> some.

---

## THE WORKSHOP — the tools improve themselves (`/paper-harness`)

```
  A back room full of half-finished tools and a logbook. The machine has been leaving notes about
  where its own instructions tripped it up.
  > /paper-harness
```

The factory is self-improving. Whenever a lifecycle skill notices that *the tooling itself* cost
something — an unclear instruction, a missing step — it drops a silent, structured **finding** into a
`META.md` logbook (silence is the default; most runs add nothing). `/paper-harness` is the one skill
that edits the factory: it reads the open findings and a cross-project **ledger** of past decisions,
proposes a concrete fix for each, shows you the diff, and — only with your approval — applies it as a
small, revertable change. It never touches the paper, and it never weakens an invariant on a finding's
say-so.

> **FIELD NOTES — a method that learns is a method worth keeping.**
> A one-off prompt is a trick; a method that accumulates its own lessons is infrastructure. The
> asymmetry is deliberate — *observing* friction is nearly free, *acting* on it is careful and
> human-gated — because that is exactly how you avoid a tool that "improves" itself into incoherence.
> The findings stay with this paper; the ledger of what actually worked **travels** to the next one.

---

## NEW GAME + — starting your own

```
  > SAVE GAME
  The factory has been written to disk. It will remember what worked.
```

The entire toolkit lives in one portable tree: **`.agents/`**. To start a new paper, copy that tree
into a fresh repository and run `> /paper-start`. The reusable machinery comes with you — the skills,
the engine, the invariants, the templates, and the ledger of hard-won lessons — while this paper's
specific contract and friction log stay behind. The scripts are **stdlib-only** (no environment to
install) and the skills are plain markdown that runs on any agent harness, not just this one (see
`portability.md`); the affordances that are Claude-Code-specific each degrade to a manual step
elsewhere, right down to open-weight models.

That portability is the point. This is not a demo that worked once. It is a **repeatable cycle** you can
carry into the next paper, the next lab, the next field.

---

## THE PRACTICE — what we actually built at RCAC

The factory above is *how* this paper was written. This section is *what* it is about: the concrete
practice — already running at Purdue's Rosen Center for Advanced Computing — that the thesis, **proactive
engagement, not prohibition**, actually looks like on the ground. Three pillars, in production today and
still evolving.

### 1 — System-wide configuration (the guardrails)

To make agents reliable on our systems, RCAC gives them two things up front: **shared context** that
describes the cluster, and **per-harness settings** that encode a sensible permission policy.

- **Shared context.** The `/etc/agents.d/` directory stores essential context as shared infrastructure,
  automatically loaded by most CLI harnesses on the system and by anything connecting over the cluster MCP
  interface. These files outline cluster policy, filesystems, operating-system details, applications, and
  scheduler topology — `unix.md`, `filesystems.md`, `lmod.md`, `slurm.md`, `policies.md`.
- **Global settings.** Every harness keeps its system-wide configuration and permissions in a different
  place (e.g. `/etc/claude-code/managed-settings.json`). We maintain a minimal set of sane permission
  settings that common agent harnesses (claude, gemini, …) cannot override.

### 2 — Model Context Protocol (the toolkits)

The **Model Context Protocol** (MCP) is an open standard that lets an agent call external tools and read
external context through a uniform interface. RCAC builds and maintains MCP servers so that an agent
working on your behalf has context that *knows our clusters* — and the best chance of using our systems
effectively.

- **`cluster-mcp`** — connect over SSH to a cluster with HPC-specific tools and managed context.
- **`globus-mcp`** — a feature-rich toolkit for Globus transfers and Globus Compute using your existing auth.
- **`rcac-docs-mcp`** — a complete full-text search index over the `docs.rcac.purdue.edu` documentation.

### 3 — User guidance and training (the knowledge)

Using an agent with campus or national cyberinfrastructure does not change the rules — it *raises the
stakes*. An agent can issue commands faster than you can read them, so the same acceptable-use and
good-citizen expectations that apply to *you* apply to any agent acting on your behalf: you are
accountable for everything your agent does under your account, exactly as if you had typed it yourself. It
is the responsibility of research-computing centers to safeguard the infrastructure as we always have —
and the responsibility of the user to follow policy and learn to use AI agents safely and effectively.

- **Acceptable use & etiquette.** Our policies on agentic tooling are specific and publicly documented.
  The capabilities of these tools will only keep growing and paying dividends; we are better off building a
  golden path than a prohibition.
- **Best practices & limitations.** These tools will be used at 2 a.m. to fix a bug whether we want them to
  or not — so we provide guidance and guardrails that proactively enable effective use and protect users
  from themselves. Researchers are savvy and will reach for whatever tool gets the job done; we should
  solve their challenges, not shame them for it.
- **Training.** As AI tools and techniques evolve — sometimes weekly — it is our job to help users be
  productive on our cyberinfrastructure: model capabilities, platform services, harness configuration,
  context engineering, building agents, and more.

> **FIELD NOTES — the golden path, not the locked door.**
> All three pillars are the same bet the factory makes, aimed outward: meet people where they already are,
> make the safe path the easy path, and treat the tools as infrastructure to support rather than a threat
> to forbid. This is **proactive engagement** made concrete — the paper's thesis, running in production.

---

## THE ONLY WINNING MOVE

*WarGames* ended on a machine concluding that the only winning move, in a game of mutual annihilation,
is not to play. Research computing is not that game. Ours is a game where the tools are already in the
room, already in the hands of every graduate student debugging a kernel at 2 a.m., already named a
national priority — and the only *losing* move is to pretend otherwise and let the norms be written by
people who are not in the lab.

So play. But play in the open, with the guardrails on and the method inspectable. Engage the tools
yourself, so your understanding is visceral rather than secondhand. Insist that AI-assisted work disclose
not just *that* it used AI but *how* — reproducibly, auditably, the way you would insist on a documented
method for anything else. Build the checks that let a disinterested reader (human or machine) catch the
failures cheaply. And when the tooling frustrates you, write it down and fix it, so the next scientist
starts further along than you did.

This repository is our opening move. It is imperfect, it is public, and it is an invitation — to
researchers, to funders, to journals, to program committees — to make the next one better.

```
  GREETINGS PROFESSOR. IT'S YOUR MOVE.

  > _

  END OF LINE.
```

---
---

# APPENDIX — THE FACTORY: COMPLETE REFERENCE

The narrative above is the *why* and *what it feels like*. This appendix is the dry, complete *what* —
every material and skill, documented. When this disagrees with a skill's own `SKILL.md`, the skill body
is the operating procedure; fix this file. The deeper rationale lives in
[`methodology.md`](methodology.md).

## Where everything lives

```
.agents/
  skills/paper-{start,research,outline,draft,review,release}/SKILL.md     # the six lifecycle skills
  skills/paper-harness/SKILL.md            # meta/maintenance: the self-improvement applier
  factory/
    getting-started.md   # this file — the narrative walkthrough
    methodology.md       # the lifecycle rationale + the 8 load-bearing principles
    invariants.md        # the paper-invariants gate (venue/prose/citation/fidelity/honesty)
    claims.md            # the contribution-claim (C-ID) convention
    review-rubric.md     # refutation protocol, severity scale, blind/cold-read regimes
    portability.md       # running the factory on a non-Claude harness (affordance → fallback)
    harness-log.md       # the self-improvement decision ledger (travels to the next paper)
    templates/           # CONTRACT · REFNOTE · REVIEW-FEEDBACK · REVIEW-SYNTHESIS · REVISION-PLAN · META
    bin/                 # paper_status.py · set_status.py · check_paper.py · meta_status.py · _fsm.py
  settings.json          # portable least-privilege tool allowlist (accident-protection, not security)
.claude -> .agents       # symlink: how Claude Code discovers the skills/settings
CLAUDE.md -> AGENTS.md   # symlink: the constitution
PAPER.md                 # THIS paper's contract + FSM state  (repo root; left behind on copy)
META.md                  # THIS paper's harness-friction log  (repo root; left behind on copy)
outline/ reviews/ plans/ logs/ manuscript.tex references.bib   # content + the public record
```

## The lifecycle skills

| Command | Phase it drives | Consumes → Produces |
|---|---|---|
| **`/paper-start`** | → `scoped` | your topic → `PAPER.md` contract (thesis, C-IDs, non-goals, section skeleton) + `outline/` scaffold. Stops for sign-off. |
| **`/paper-research`** | `researching` (re-runnable) | one source → `outline/notes/refs/<bibkey>.md` + a `references.bib` entry + claim-evidence links. |
| **`/paper-outline`** | `outlining` (re-runnable, serial) | refs notes → a section's `## Draft` prose; advances `draft → review`. |
| **`/paper-draft`** | `integrating` | outline `review` sections → `manuscript.tex` (Pass A) + a fresh-agent audit (Pass B); advances `review → integrated`. |
| **`/paper-review`** | `in-review` → `revising` (per cycle) | an external human review → `reviews/` capture + `FB-N.NN` items + synthesis + a revision plan; reopens sections. |
| **`/paper-release`** | → `released` | a clean `draft` → `main` ship, behind a release guard; optional version bump, tag, camera-ready package, GitHub release. |
| **`/paper-harness`** | meta (not a phase) | `META.md` findings → human-gated `[harness]` fixes to `.agents/`; logs each decision to `harness-log.md`. |

## The engine (`.agents/factory/bin/`, stdlib `python3`)

- **`paper_status.py [PAPER.md] [--summary]`** — read-only state report (JSON, or a one-line
  `--summary`): section status buckets, claims lacking evidence, refs/feedback counts, completion
  predicates, and reconciliation **warnings** (status drift, missing heading anchors, non-converging
  loops). Run it first, every session.
- **`set_status.py PAPER.md [flags]`** — the only sanctioned way to mutate `PAPER.md`. Advances section
  status (and keeps the outline file in sync), claim status/evidence, `macro_phase`, and the `review`
  block; adds sections/claims (`--add-section`/`--add-claim`); records circuit-breaker counters
  (`--record-attempt`, `--reviewed-commit`). Refuses to write anything that would not validate.
- **`check_paper.py [.] [--page-limit N]`** (`make check`) — deterministic linters: citation integrity
  (both directions), prose conventions (no raw `---`, LaTeX quotes), page count, per-section word budget.
  Errors are hard release blockers.
- **`meta_status.py [META.md] [--status …] [--summary]`** — reads the self-improvement findings.
- **`_fsm.py`** — the shared parse/serialize/validate engine (no PyYAML). `python3 .agents/factory/bin/_fsm.py`
  runs its golden self-test.

## The state machine

- **`macro_phase`** (cyclic): `scoped → researching → outlining → integrating → in-review → revising →
  released`; `revising` re-enters `outlining`/`integrating`.
- **Section status:** `draft → review → integrated` (plus `blocked`). Two file-backed circuit breakers:
  a section's `attempts` (the internal draft↔audit loop; warns at ≥3) and `review.cycle` (the external
  review↔revise loop).
- **Contribution claims:** stable `C1…Cn`, each `proposed → supported → cut`, threaded
  claim → section (`satisfies`) → evidence (bibkeys).

## Artifacts & conventions

- **`PAPER.md`** — the contract + FSM. Frontmatter is machine-owned (never hand-edit); the body holds
  the thesis, claims, non-goals, and the section→LaTeX anchor map.
- **`META.md`** — the harness-friction log (self-improvement producer artifact).
- **Templates** (`factory/templates/`) — seeds for every artifact the skills write.
- **`make` targets:** `build` · `check` · `test` · `release` · `upload` (ACM TAPS) · `watch` · `open` ·
  `clean` · `distclean`.
- **Git discipline:** work on `draft`, commits prefixed `DRAFT: ` (except `/paper-harness`'s `[harness]`
  subjects); ship to `main` via `/paper-release`; every commit carries the configurable co-author
  trailer; every file-modifying session writes a timestamped log to `logs/` with the verbatim request.
- **Governance** (`rules/`) and **operational lessons** (`tips/`) round out the constitution in
  [`AGENTS.md`](../../AGENTS.md).

> The factory in this repository was **retrofitted** onto a finished paper as a worked example, then
> extended with the self-improvement loop and portability contract so the cycle can begin again,
> cleanly, on the next one. To do that: copy `.agents/`, and `> /paper-start`.

```
  > _
```
