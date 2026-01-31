---
created: "2026-01-31"
status: "completed"
related_logs:
  - logs/2026-01-31T21-18-00.md
---

# Manuscript Structure and Outline Workflow

## Context

This plan establishes the content structure for "Hello Computer: HPC in the Agentic Era" - a PEARC'26 extended abstract that combines technical documentation of RCAC's AI initiatives with pop-culture whimsy and personal narrative. The manuscript serves as both a poster presentation and a "love letter/cautionary tale" on agentic AI in HPC.

## Goals

1. Create an `outline/` directory for iterative content development
2. Define the manuscript section structure with easter-egg headings
3. Update `manuscript.tex` with correct title and section scaffolding
4. Set up the Acknowledgements section with AI attribution
5. Establish a workflow for developing content in outline files before integrating into main body

## Decisions Made

- **Easter-egg headings**: Use directly as `\section{}` and `\subsection{}` titles (not formal titles with epigraphs)
- **Page limit**: 4 pages (confirmed by first author, former proceedings chair)
- **MCP/TRON joke**: Inline in Approach section, not footnote
- **Background section**: Intentionally more formal/dry for contrast

## Section Structure

| Section | Heading | Topic |
|---------|---------|-------|
| Title | "Hello Computer: HPC in the Agentic Era" | Star Trek IV reference |
| 1 | "Shall We Play a Game?" | Introduction (WarGames) |
| 1.1 | "Mostly Harmless" | Motivations (Hitchhiker's Guide) |
| 2 | Background | AI timeline, technical context |
| 3 | Approach | RCAC initiatives, MCP servers |
| 4.1 | "I'm Sorry, Dave" | User support (2001) |
| 4.2 | "Tea, Earl Grey, Hot" | Prompt engineering (TNG) |
| 4.3 | "I Know Kung Fu" | User expectations (Matrix) |
| 4.4 | "The Answer is 42" | AI outcomes (Hitchhiker's Guide) |
| 4.5 | "Don't Cross the Streams" | Cautionary notes (Ghostbusters) |
| 5 | "End of Line" | Conclusion (TRON) |

## Outline Workflow

Files in `outline/` follow this pattern:
1. Draft content in markdown section files
2. Iterate and refine before touching LaTeX
3. Migrate polished content to `manuscript.tex`
4. Keep outline files as reference/rationale

## Implementation Outcome

All goals completed:
- Created `outline/` directory with README, section files, notes, and snippets
- Updated `manuscript.tex` with title, section scaffolding, and acknowledgements
- MCP joke captured in `outline/snippets/mcp-joke.md`
- Easter eggs tracked in `outline/notes/easter-eggs.md`
- Build verified successful
