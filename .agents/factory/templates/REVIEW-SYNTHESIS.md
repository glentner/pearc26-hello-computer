<!--
  REVIEW-SYNTHESIS template — the cross-cutting distillation /paper-review produces
  after capturing a raw human review (reviews/review_phase_N.md) and splitting it into
  per-point [FB-N.NN] items (outline/notes/review-feedback-*.md).

  Role: this file is the bridge between scattered feedback and the revision plan. It
  groups every FB item into a handful of THEMES (a theme unifies several FB-IDs that say
  the same thing across sections), carries a status marker per theme, names one recommended
  action, and ends with a section-priority map that orders the revision work. /paper-review
  writes plans/N-revision.md FROM this synthesis, then advances the FSM via set_status.py
  (bump review.cycle, macro_phase: revising, reopen affected sections).

  Write to: outline/notes/review-synthesis.md  (one per review, overwritten/extended each cycle).
  Cross-reference: ../../.agents/factory/review-rubric.md (severity vocab, refutation protocol)
  and ../../.agents/factory/claims.md (C-IDs a theme may touch).

  Conventions:
  - Status markers: [MUST-FIX] | [SHOULD-FIX] | [CONSIDER] (severity, per review-rubric.md)
    combined with a resolution state: [OPEN] | [PARTIALLY RESOLVED] | [RESOLVED]. Use the
    severity when a theme is still open; mark [RESOLVED] once the driving revision landed.
  - Every theme MUST list the FB-IDs it consolidates — the synthesis adds no new findings,
    it only unifies existing ones. If a claim is affected, name the C-ID.
  - Keep it tight and honest. Silence on a clean section is valid; do not manufacture themes.
  - Replace every {placeholder}. Delete unused optional blocks. Never invent an FB-ID.
-->
---
sources:
  - outline/notes/review-feedback-{part-or-phase}.md
  - {additional feedback files, one per line}
total_items: {N}
review_cycle: {N}
phase{N}_status: {in-progress|complete}
---

# Review Synthesis: Cross-Cutting Themes (Cycle {N})

{One short paragraph: which review(s) this consolidates (who reviewed, when, which draft
version), and how to read the document — themes group the [FB-N.NN] items, each carries a
severity + resolution marker and one action, and the section-priority map at the bottom
orders the work. Note any earlier-cycle themes confirmed or re-opened here.}

---

## Theme 1: {short imperative name of the recurring issue} [{MUST-FIX|SHOULD-FIX|CONSIDER|RESOLVED}]

**FB-IDs**: {FB-N.NN, FB-N.NN, …}
**Sections**: {section names / ids the theme touches}
**Claims**: {C-IDs affected, or "none"}

{Two or three sentences stating the underlying problem these FB items share — the single
root issue, not a restatement of each item. Quote the offending phrasing where it sharpens
the point.}

**Recommended action**: {the one concrete revision that resolves the whole theme.}

**Status**: {OPEN — for cycle {N} | PARTIALLY RESOLVED — {what remains} | ✅ RESOLVED — {what
landed and where}}.

---

## Theme 2: {…} [{marker}]

**FB-IDs**: {…}
**Sections**: {…}
**Claims**: {…}

{root issue}

**Recommended action**: {…}

**Status**: {…}

---

<!-- Repeat one ## Theme block per cross-cutting cluster. Aim for a handful (roughly 5–20);
     if two clusters differ only by section, they are one theme with a longer Sections line.
     Order themes MUST-FIX first, then SHOULD-FIX, then CONSIDER, then RESOLVED. -->

## Approved sections (no changes beyond items above)

{Bullet the sections a reviewer explicitly approved, with the FB-ID that records the
approval — so the revision plan does not touch them. Delete if none.}

- **{section / subsection}** ({FB-N.NN}): {verbatim approval, e.g. "great, no changes."}

---

## Open questions

{Unresolved items that block or gate revision and need a human decision — page-budget
format, an ACM-policy call, a pun to keep or cut. Mark each with a `[NEEDS CLARIFICATION: …]`
so /paper-review stops at the gate rather than guessing. Delete if none.}

- **{question}** ({FB-N.NN}): {context and what a decision unblocks.}

---

## Revision priority by section (Cycle {N})

{Order the sections by how much work they need, most first. This is the spine the revision
plan follows and the order sections should reopen (set_status.py --section <id> --status
draft). For each, list the themes/FB-IDs driving it. Mark ✅ as items land.}

**{Section} ({0N-name.md})** — {highest-priority | …}:
- {Theme K: one-line action} → {status}
- {Theme M: one-line action} → {status}

**{Section} ({0N-name.md})** — {no changes needed — approved, or the next-priority work}:
- {…}

<!-- …one block per section, in priority order… -->

**Remaining for next cycle**:
- {Theme / FB-ID deferred to Cycle {N+1} or to integration, with why.}

---

## Drives

- Plan: [`plans/{N}-revision.md`](../../plans/{N}-revision.md) — the ordered task list this
  synthesis produces; /paper-review writes it from the priority map above.
- FSM: `set_status.py PAPER.md --bump-cycle --macro-phase revising` then
  `--section <id> --status draft` for each reopened section named in the priority map.
