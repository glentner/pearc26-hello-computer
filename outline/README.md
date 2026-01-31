# Outline Workflow

This directory contains working notes, drafts, and structure for the manuscript before content is integrated into `manuscript.tex`.

## Purpose

- **Iterate freely**: Draft prose in markdown without LaTeX friction
- **Track decisions**: Notes explain *why* we structured things a certain way
- **Preserve context**: Outline files remain as reference even after integration

## Directory Structure

```
outline/
├── README.md           # This file
├── 00-abstract.md      # Abstract drafts and notes
├── 01-introduction.md  # "Shall We Play a Game?" + "Mostly Harmless"
├── 02-background.md    # AI timeline and technical context
├── 03-approach.md      # RCAC initiatives (MCP servers, configs, etc.)
├── 04-discussion.md    # Themed subsections with easter-egg headings
├── 05-conclusion.md    # "End of Line"
├── notes/              # Freeform notes, quotes, research
│   └── easter-eggs.md  # Pop-culture reference tracking
└── snippets/           # Reusable text fragments
    └── mcp-joke.md     # The TRON/MCP quip
```

## Section File Format

Each section file follows this structure:

```markdown
---
status: draft | review | integrated
target_words: <number>
---

# Section Title

## Key Points
- Point 1
- Point 2

## Notes
[Research, references, decisions]

## Draft
[Iterative prose development]
```

## Workflow

1. **Draft**: Write rough content in the appropriate section file
2. **Refine**: Multiple passes—structure first, then prose quality
3. **Review**: Mark as `review` when ready for co-author feedback
4. **Integrate**: Copy polished content to `manuscript.tex`
5. **Update status**: Mark as `integrated` (don't delete—keeps rationale)

## Page Budget

PEARC'26 extended abstract: **4 pages** total

Rough allocation:
- Abstract: ~150 words
- Introduction: ~400 words (1 column)
- Background: ~300 words
- Approach: ~500 words
- Discussion: ~600 words (5 subsections)
- Conclusion: ~200 words
- References + Acknowledgements: remainder
