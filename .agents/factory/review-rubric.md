# Review rubric — refutation protocol & severity

The operating manual for the two verification activities in the paper factory. Both use the same
**refutation protocol** and **severity vocabulary**; they differ in what they inspect and who runs
them.

1. **Internal audit** — `/paper-draft` **pass B**, run by a fresh subagent, after pass A integrates
   the outline into `manuscript.tex`.
2. **External feedback distillation** — `/paper-review`, turning a human peer review into tracked
   `FB-N.NN` items.

> **Section ownership.** When `/paper-draft` delegates pass B, it hands the fresh subagent ONLY the
> **reviewer-facing** sections — *Refutation protocol*, *Severity vocabulary*, and the ONE pass-B
> regime it is running. The **orchestrator-only** sections (*Bounded loops & escalation*, the
> *Mandatory human gate*, and the whole *`/paper-review` distillation* section) are for the skill that
> drives the loop and advances FSM state — **never pass them to the reviewer subagent**, or it will
> believe it owns verdicts, state transitions, or `/paper-review`. Each section below is tagged
> `[reviewer-facing]` or `[orchestrator-only]`.

## Refutation protocol (mandatory, both activities) · [reviewer-facing]

For every candidate finding, **try to disprove it first**:

1. Locate it — quote the exact outline sentence and the exact `manuscript.tex` line, or the exact
   claim and the `references.bib` entry.
2. If reproduced with a concrete discrepancy → **CONFIRMED**.
3. If plausible on a read but not pinned to specific text → **PLAUSIBLE** (needs human triage; does
   not auto-loop).
4. If it dissolves under scrutiny → drop it silently.

Default to dropping when uncertain. A single model reviewing prose it (or a sibling) wrote has
self-preference bias even in a fresh context — lean on *quoted evidence*, not opinion. Silence on a
clean section is a valid, valuable result; a gap-hunting reviewer manufactures gaps and drives
over-writing.

## Severity vocabulary (shared with external reviewers) · [reviewer-facing]

Matches the vocabulary already used in this repo's `reviews/` and `outline/notes/review-feedback-*`:

| Severity | Meaning |
|---|---|
| **must-fix** | Factual error, unsupported claim, dangling/incorrect citation, a page-budget or ACM-policy violation (see `invariants.md`), or a fidelity break (tex ≠ outline). Blocks release. |
| **should-fix** | A real weakness: awkward framing, choppy structure, an over-clever phrase, a thin argument. Fix before submission if budget allows. |
| **consider** | Optional polish or a judgment call for the human (tone, an em-dash that might stay, a pun to keep). |

## `/paper-draft` pass B — two honest regimes · [reviewer-facing]

Pass B is delegated to a **fresh subagent** to remove authoring bias. "Blind" is used precisely — one
regime cannot be blind, the other can:

- **(i) Fidelity cold-read (NOT blind — needs both sources).** The reviewer re-reads each
  `outline/0N-*.md` `## Draft` and the corresponding `manuscript.tex` section (via the `PAPER.md`
  anchor map) *from scratch*, sentence by sentence: no dropped/added/reordered words, no stale text,
  paragraph breaks match, LaTeX prose conventions applied (`invariants.md` §2). This is the cold-read
  the legacy `latex-integration-second-pass` did — the value is a fresh context, not hidden inputs.
- **(ii) Claim + citation + invariant audit (genuinely blind).** The reviewer sees the C-ID claims
  (statements + `evidence`), `references.bib`, and `manuscript.tex` — **but NOT the outline
  rationale** — and asks: is each claim actually supported by its cited evidence? Does every `\cite`
  resolve (defer to `check_paper.py` for the mechanical pass)? Any `invariants.md` violation?
  Withholding the outline avoids grading-its-own-homework on the claim logic. **Make blindness
  structural:** the three inputs are handed to the subagent *inline*, and it is told it may **NOT** read
  `outline/`, `plans/`, `reviews/`, the `PAPER.md` **body**, or `META.md` off disk — each leaks author
  intent (and `META.md` leaks harness meta-notes). If the harness cannot enforce the path restriction,
  spawn the subagent with only those inputs and state the prohibition explicitly.

Pass B **reports and STOPS** — it never auto-fixes, and the reviewer subagent **leaves a clean working
tree** (no edits, no commits). Findings carry section + line + severity + CONFIRMED/PLAUSIBLE, most-severe
first (emit via `ReportFindings` when available, and/or write into the draft session log). The human
decides what to apply; then the **orchestrator** applies fixes with an **explicit `git add <files>`**
(never `git add -A`, so nothing a subagent stranded rides into the commit) and advances sections
`review → integrated`. After a clean pass, the orchestrator records the audited commit
(`set_status.py --reviewed-commit "$(git rev-parse HEAD)"`) so `/paper-release` can gate on the shipped
manuscript actually having been audited.

**Later cycles.** When `/paper-review` reopens sections and `/paper-draft` re-runs pass B, the re-run
**declares its mode**: default is a *fresh blind pass over the reopened sections*; the human may scope it
to verifying named `FB-N.NN` items were remediated. Record the choice in the session log.

## `/paper-review` — external distillation · [orchestrator-only]

Turn a raw human review (call transcript, email, committee notes) into the tracked spine:

- **Capture** verbatim into `reviews/review_phase_N.md` (fix only transcription errors, noting them).
- **Distill** into `outline/notes/review-feedback-*.md`: one `[FB-N.NN]` per point with **Type**,
  **Severity** (above), **Quote/context** (verbatim), **Action**. Map each to the section id and any
  C-ID it touches.
- **Synthesize** cross-cutting themes into `outline/notes/review-synthesis.md`, each with a
  resolution status and a section-priority order.
- **Drive**: write `plans/N-revision.md`, then `set_status.py` to bump `review.cycle`, set
  `macro_phase: revising`, and reopen the affected sections.

## Bounded loops & escalation · [orchestrator-only]

Two distinct loops, two distinct file-backed counters — **do not conflate them**:

- **Internal draft↔audit loop** (per section, inside `/paper-draft`): bounded by the section's
  **`attempts`** field. On a pass-B RED the orchestrator records it
  (`set_status.py --section <id> --record-attempt`, committed so the count survives a context reset); at
  **`attempts ≥ 3`** `paper_status.py` warns and the section is a raised hand — **stop-and-re-shape or
  escalate to a human**, do not keep looping. Self-correction does not reliably converge.
- **External review↔revise loop** (whole paper, across `/paper-review` cycles): counted by
  **`review.cycle`** (bumped by `/paper-review` with `--bump-cycle`). Human-paced; `paper_status.py`
  warns when it exceeds ~3, signalling the paper is thrashing on external feedback.

## Mandatory human gate · [orchestrator-only]

A human approves before `/paper-release` whenever a CONFIRMED **must-fix** finding touches a factual
claim, a citation, the AI-use disclosure, or the page/ACM-policy invariants. `check_paper.py` errors
(dangling cite, over page limit) are hard release blockers regardless of the audit verdict.
