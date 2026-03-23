# LaTeX Integration — Second Pass (Subphase B)

## Purpose

Cold-read fidelity audit comparing each outline draft against the integrated
`manuscript.tex`. This is intentionally separated from the first-pass
integration to avoid self-confirming errors — the agent re-reads both sources
fresh and compares sentence-by-sentence without relying on memory of what it
just wrote.

## When to Use

Use this prompt for **task 5.2** of `plans/second-revision.md` (or any future
integration phase). Run **after** the first pass
(`prompts/latex_integration_first_pass.md`) has been committed.

## Prompt

```
Execute Subphase B of Phase 5: cold-read fidelity audit.

CONTEXT: Read `plans/second-revision.md` to confirm task 5.1 is complete.
The first-pass integration has been committed. This is a fresh audit pass.

PROCEDURE — for each section in order (00 through 05):

B1. RE-READ BOTH SOURCES. Read the outline file (`outline/0N-*.md`) and
    the corresponding section in `manuscript.tex` from scratch. Do NOT
    rely on memory from any previous pass.

B2. SENTENCE-LEVEL COMPARISON. Walk through the outline `## Draft` prose
    sentence by sentence. For each sentence, confirm:
    - The prose appears in the LaTeX (with appropriate LaTeX formatting)
    - No words were dropped, substituted, or reordered
    - No stale text from previous drafts remains in the LaTeX
    - Paragraph breaks match the outline structure

B3. CITATION CHECK. For each `\cite{...}` in the LaTeX section:
    - Confirm the citation key exists in `references.bib`
    - Confirm it is attached to the correct claim or sentence
    - Cross-reference the outline frontmatter `citations:` field:
      every key listed there should appear in the LaTeX section

B4. FORMATTING CHECK. Verify LaTeX conventions are correct:
    - ``...'' for double quotes (not "...")
    - \emph{...} for italics where the outline uses *...*
    - \texttt{...} for inline code where the outline uses `...`
    - Non-breaking spaces (~) where appropriate
    - No raw --- em-dashes (project convention: commas or reworded)
    - Heading commands match the A4 heading map from the first pass

B5. REPORT DISCREPANCIES. Compile all findings into a summary list:
    - Section name
    - Line number in `manuscript.tex`
    - Issue description (dropped word, stale text, misplaced cite, etc.)

    Present this report and STOP. Wait for confirmation before applying
    any fixes. Do NOT auto-correct — the user may want to review or
    make judgment calls on specific items.

After fixes are approved and applied:
- Verify `make build` succeeds.
- Commit: `WIP: Third integration fidelity audit (second pass)`
  with `Co-Authored-By: Oz <oz-agent@warp.dev>`
- Mark tasks 5.1 and 5.2 as `[x]` in `plans/second-revision.md`.
```
