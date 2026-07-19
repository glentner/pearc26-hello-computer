---
source: reviews/review_phase_{N}.md
reviewed_by: [{Reviewer One}, {Reviewer Two}]
date: {YYYY-MM-DD}
---

<!--
  REVIEW-FEEDBACK template — the distilled external-feedback file `/paper-review` produces
  (see ../review-rubric.md §"/paper-review — external distillation").

  One file per review pass part: outline/notes/review-feedback-part{K}.md. The raw human review is
  captured VERBATIM into reviews/review_phase_{N}.md first (that path is the `source:` above); this
  file is the distilled, tracked spine derived from it.

  FB-N.NN id scheme — STABLE, never renumbered:
    - N  = the review cycle (PAPER.md `review.cycle`; part-1 of cycle 1 → FB-1.NN).
    - NN = a zero-padded sequential counter, assigned in reading order across the whole part,
           NOT reset per section. Ids are permanent handles: /paper-review's synthesis
           (review-synthesis.md) and plans/N-revision.md reference items by [FB-N.NN], so once
           assigned an id is never reused or renumbered even if the item is dropped.

  Group items by `## Section: <name>` in manuscript reading order (a subsection gets its own
  `## Section: <parent> — "<subsection>"` heading, as in the real file). Every item carries the
  four bold fields below, in this order.

  **Severity is LOAD-BEARING.** Use these EXACT tokens — must-fix | should-fix | consider — they
  are matched literally by check tooling and rolled up by paper_status.py's feedback_by_severity.
  Meanings (../review-rubric.md §"Severity vocabulary"):
    - must-fix   : factual error, unsupported/dangling citation, page-budget or ACM-policy
                   violation, fidelity break. Blocks release.
    - should-fix : a real weakness (awkward framing, choppy structure, over-clever phrase, thin
                   argument). Fix before submission if budget allows.
    - consider   : optional polish or a judgment call for the human (tone, an em-dash, a pun).
  A misspelled or invented severity is invisible to the rollup — copy the token exactly.

  **Quote/context is VERBATIM.** Reviewer's own words (attribute by name); do not paraphrase into
  agreement. **Action** is your imperative distillation of what to do, and names the C-ID(s) touched
  when a claim is at stake.
-->

# Review Feedback: Part {K}

## Section: {Section name — e.g. Abstract}

### [FB-{N}.01] {Short title of the point}
- **Type**: {word-choice | tone | content | structure | framing | meta | ...}
- **Severity**: {must-fix | should-fix | consider}
- **Quote/context**: {Reviewer} flags "{verbatim reviewer words, in their voice}" — {any surrounding context needed to make the quote actionable}.
- **Action**: {Imperative distillation of the fix. Name the affected C-ID(s) if a contribution claim is touched. Offer concrete alternatives to workshop where useful.}

### [FB-{N}.02] {Short title of the next point}
- **Type**: {type}
- **Severity**: {must-fix | should-fix | consider}
- **Quote/context**: {verbatim reviewer words}.
- **Action**: {what to do}.

## Section: {Next section name — e.g. Introduction}

### [FB-{N}.03] {Short title}
- **Type**: {type}
- **Severity**: {must-fix | should-fix | consider}
- **Quote/context**: {verbatim reviewer words}.
- **Action**: {what to do}.

<!--
  Continue in reading order. Keep the NN counter monotonic across ALL sections of this part;
  add `## Section:` headings only for sections the reviewers actually touched. An approved /
  clean section may still get one `consider`/`meta` item noting "no content changes needed" —
  silence is also a valid result (../review-rubric.md), so do not manufacture items to fill gaps.
-->
