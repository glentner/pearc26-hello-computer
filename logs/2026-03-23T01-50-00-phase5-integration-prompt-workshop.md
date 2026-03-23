---
timestamp: "2026-03-23T01:50:00Z"
duration_minutes: ~15
user_input: |
  We're working on our PEARC'26 paper, we haven't fully completed all phases of our plans/second-revision.md review cycle. Please familiarize yourself with all the necessary context from there. Before we start Phase 5 to integrate our outline draft sections into the manuscript.tex source file I want to ask a few questions. 

  Do you have any recommendations about how we should approach this integration behavior? We have approved prose in our drafts in the section files in outline/ but we've had a lot of mistakes in the past pulling these into the LaTeX document. The challenge is not as simple as converting to LaTeX syntax and concatenating them in the .tex file. For some reason we're not including the bibliography references in the markdown and those need to be included in the LaTeX source. There's also some challenges with the section layouts and the differences between simple `\subsection{}` conversions and paragraph labels; which we're only really doing because we are so constrained on the page limits.

  I want you to workshop some ideas with me on how we can optimize our agent prompts (to you) to help maximize our success. What do you think?
user_followup: |
  Okay great. Can you tease that out into specific discrete instructions in a 'Subphase A: [per section delta-based updates preserving LaTex conventions]...' as individual steps as you've just described them to me, and 'Subphase B: [separate cold-read fidelity audit comparing each outline draft one at a time]...'?
user_followup_2: |
  Please see our comprehensive continuation prompt at the end of the plans/second-revision.md document. I'd like you to craft each of these as you've presented them to me just now as 2 separate documents as prompts/latex_integration_first_pass.md and prompts/latex_integration_second_pass.md respectively. Include them as literal snippets that I can copy here in Warp like we did for the continuation prompt. In their documents give them their titles and helpful descriptions like they have a mini README to guide usage and why we built these.
files_modified:
  - prompts/latex_integration_first_pass.md
  - prompts/latex_integration_second_pass.md
commits:
  - "6f8abd9: WIP: Add two-pass LaTeX integration prompts for Phase 5"
related_plans:
  - plans/second-revision.md
---

# Phase 5 Integration Prompt Workshop

## Summary

Workshopped and formalized the approach for Phase 5 LaTeX integration to avoid
the failure modes encountered in previous integrations: dropped citations,
incorrect heading-level mappings, and compounded errors from doing conversion
and auditing in a single pass.

## Work Completed

The session began as a discussion about how to approach Phase 5 (third
integration of outline drafts into `manuscript.tex`). Three recurring problems
were identified from prior integration attempts:

1. **Citation loss** — `\cite{key}` references exist in the LaTeX but not in
   the outline markdown; regenerating from scratch drops them
2. **Heading mismatches** — markdown heading levels don't map 1:1 to LaTeX
   commands (`\subsection` vs `\paragraph`), especially given page-limit
   constraints
3. **Error compounding** — combining prose conversion and fidelity checking in
   one step causes self-confirming errors

The solution was to split integration into two discrete phases:

- **Subphase A (First Pass):** Delta-based surgical updates, working
  diff-style with an explicit heading map to preserve existing LaTeX
  conventions and citations
- **Subphase B (Second Pass):** Cold-read fidelity audit, re-reading both
  sources fresh and comparing sentence-by-sentence without relying on memory
  from the first pass

These were formalized as reusable prompt documents:
- `prompts/latex_integration_first_pass.md` — contains the Subphase A prompt
  with the full heading map and LaTeX convention checklist
- `prompts/latex_integration_second_pass.md` — contains the Subphase B prompt
  with sentence-level comparison and citation cross-reference procedures

Both documents include purpose descriptions, when-to-use guidance, and
copy-pasteable prompt blocks styled after the continuation prompt in
`plans/second-revision.md`.

## Next Steps

- Execute Phase 5 using the two-pass prompts in order (first pass, then second pass)
- Address remaining Theme 9 page budget during integration
- Theme 17 (LaTeX fidelity) will be resolved by the second-pass audit
