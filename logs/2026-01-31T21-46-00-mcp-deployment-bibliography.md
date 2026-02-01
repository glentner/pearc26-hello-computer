---
timestamp: "2026-01-31T21:46:00Z"
session_type: "feature"
summary: "Added MCP deployment architecture notes and annotated bibliography for Background section"
files_modified:
  - outline/notes/mcp-deployment-architecture.md
  - outline/notes/bibliography.md
  - outline/02-background.md
  - outline/03-approach.md
  - references.bib
related_plans:
  - plans/manuscript-structure-outline.md
user_input: |
  Outstanding - great job. I loved some of your suggestions for additional easter eggs - classic! We'll vibe for awhile on where we want to take each of these sections but I'm happy with the structure I think, we'll make refinements as we go along. We'll tackle a draft phase on each section and do an preliminary integration to push a release PDF as a zero-th version of our paper.

  First, I want to shape up a few things I saw during our outlining phase. I want to add something to our RCAC-MCP and Globus-MCP projects that is worth discussion in the paper. I've gone through a few iterations and am building a 3-mode deployment configuration to allow for what I think is going to be the common usage pattern with agentic environments to run the MCP server locally and rely on other layers for delegation; that is, for the HPC clusters a local server in 'stdio' mode relies on a background SSH bridge (using users actual config and keys) to offload tool use via SSH instead of hosting the server directly as a shared asset with JWT or OIDC auth and local shell or sudo-spawning delagation based on an identity file - both of which I've built. Similarly for globus the users can run the server locally as a Python package just like the 'globus-cli' tool and do local login as they otherwise would which the server will pick up on instead of an online shared hosted solution. Again, a choice and one driven by where the ecosystem moves in terms of preference.

  Second, I think we should then tackle our annotated bibliography for our background section first and find the appropriate subject-matter references and discuss those in our outline/.

  Let's handle these two additions and update our logs/ and do another commit.
---

# Session Log

## User Input

(See `user_input` in frontmatter for verbatim input.)

User requested two additions to the manuscript preparation:

1. **MCP Deployment Architecture**: Document the 3-mode deployment configuration being developed for RCAC-MCP and Globus-MCP servers:
   - Local STDIO mode with SSH bridge (recommended default)
   - Hosted service with JWT/OIDC authentication
   - Hosted service with sudo/identity delegation

2. **Annotated Bibliography**: Research and document key references for the Background section, including foundational AI papers and HPC+AI intersection literature.

## Agent Actions

### MCP Deployment Architecture
Created `outline/notes/mcp-deployment-architecture.md` documenting:
- The problem: where should MCP servers run and how should they authenticate?
- Three deployment modes with ASCII architecture diagrams
- Design philosophy: build all three, default to local-first
- Key insight for paper: "The question isn't just 'can AI manage HPC resources?' but 'where should that capability live?'"

Updated `outline/03-approach.md` with summary of deployment architecture as a key technical contribution.

### Annotated Bibliography
Researched via web search:
- Transformer paper (Vaswani et al., 2017)
- GPT-4 Technical Report (OpenAI, 2023)
- MCP announcement and adoption timeline (Anthropic, 2024)
- HPC+AI market data (Hyperion Research, Intersect360)
- LLM for HPC software development (Godoy et al., 2024)
- HPC at a crossroads (Deelman et al., Science 2025)

Created `outline/notes/bibliography.md` with:
- Annotated entries for each reference
- Timeline for Background section
- BibTeX entries ready to use
- Notes on where each reference belongs

Updated `outline/02-background.md` with:
- Key references list
- Timeline table
- Technical context with market statistics

Added BibTeX entries to `references.bib` (5 entries).

## Outcome

The manuscript now has:
- Documented deployment architecture as a technical contribution for the Approach section
- Annotated bibliography with 5 key references and BibTeX entries
- Updated outline files linking to the new notes
- Build verified successful

Next steps: Continue developing prose content in outline files, potentially starting with Introduction or Background.
