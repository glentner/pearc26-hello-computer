# LaTeX Integration — First Pass (Subphase A)

## Purpose

Delta-based integration of revised outline prose into `manuscript.tex`.

Previous integrations suffered from three failure modes: (1) citations exist in
the LaTeX but not the outline markdown, so regenerating from scratch drops them;
(2) markdown heading levels don't map 1:1 to LaTeX commands (`\subsection` vs
`\paragraph`); (3) combining prose conversion and fidelity checking in one step
compounds errors. This prompt addresses mode (1) and (2) by working diff-style
with an explicit heading map. Mode (3) is handled by separating the audit into
`prompts/latex_integration_second_pass.md`.

## When to Use

Use this prompt for **task 5.1** of `plans/second-revision.md` (or any future
integration phase). Run **before** the second-pass fidelity audit. Commit the
result as a checkpoint before proceeding to the audit.

## Prompt

```
Execute Subphase A of Phase 5: delta-based LaTeX integration.

CONTEXT: Read `plans/second-revision.md` to confirm Phase 5 is current.
The outline `## Draft` sections are the ground-truth source. The goal is
to update `manuscript.tex` to match, preserving all LaTeX conventions.

PROCEDURE — for each section in order (00 through 05):

A1. LOAD BOTH SOURCES. Read the outline file (`outline/0N-*.md`) and
    identify the corresponding line range in `manuscript.tex`.

A2. IDENTIFY DELTAS ONLY. Compare the outline `## Draft` prose against
    the current LaTeX prose. List the specific passages that differ.
    If a section has no changes (e.g., `01-introduction.md` and
    `05-conclusion.md` were approved without revision in Phase 4),
    confirm "no delta" and skip to the next section.

A3. APPLY CHANGES SURGICALLY. For each delta, update only the changed
    passage in `manuscript.tex`. Preserve all LaTeX conventions:
    - `\cite{key}` — keep in place unless the anchor sentence moved;
      if it did, reposition using the outline frontmatter citation list
    - Quoting: ``...'' (LaTeX double quotes), never "..."
    - Emphasis: \emph{...} for italics, \texttt{...} for code/commands
    - Non-breaking spaces: ~ (e.g., 2~AM)
    - Em-dashes: this project uses commas or reworded clauses, not ---
    - Line wrapping: match the existing manuscript convention (~80 chars)

A4. HEADING MAP. Use this explicit mapping — do not infer from markdown
    heading levels:

    00-abstract.md  → \begin{abstract}...\end{abstract} (no heading)
    01-introduction.md →
      \section{Shall We Play a Game?}
      \paragraph{Mostly Harmless}
    02-background.md →
      \section{Background} (no subsections)
    03-approach.md →
      \section{Approach}
      \subsection{System-Wide Configurations}
      \subsection{MCP Servers}
      \subsection{Documentation and Guidance}
    04-discussion.md →
      \section{Discussion}
      \paragraph{``I'm Sorry, Dave'' (User Support)}
      \paragraph{``Tea, Earl Grey, Hot'' (Context Engineering)}
      \paragraph{``I Know Kung Fu'' (User Expectations)}
      \paragraph{``The Answer is 42'' (AI Outcomes)}
      \paragraph{``Don't Cross the Streams'' (Cautionary Notes)}
    05-conclusion.md →
      \section{End of Line} (no subsections)

After all six sections are processed:
- Verify `make build` succeeds.
- Commit: `WIP: Third integration from revised outline (first pass)`
  with `Co-Authored-By: Oz <oz-agent@warp.dev>`

STOP after committing. Do not begin the fidelity audit — that is a
separate prompt (`prompts/latex_integration_second_pass.md`).
Report which sections had deltas and what was changed.
```
