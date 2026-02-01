---
session_id: "2026-02-01T0119Z"
type: "reference-deep-dive"
bibkey: "anthropic2025aaif"
duration_minutes: ~10
files_modified:
  - outline/notes/refs/anthropic2025aaif.md (created)
  - outline/notes/refs/README.md (updated progress)
user_input: |
  Continue our PEARC'26 paper work. See plan <plan:a91aeec6-aca9-4fdd-999f-52f7174c213a> for context.

  Do the next reference deep-dive. Check `outline/notes/refs/README.md` for the next pending item.

  For this reference:
  1. Research the source material (fetch/read the paper, blog, or document)
  2. Create `outline/notes/refs/<bibkey>.md` with full YAML frontmatter and long-form summary
  3. Mark it complete in the tracking README
  4. Create a session log
  5. Commit with "WIP: deep-dive <bibkey>"

  in-line references:

  ### <plan:a91aeec6-aca9-4fdd-999f-52f7174c213a>
  I've manually updated the following plan. Ensure you take my edits into account.
  [plan content attached]
---

# Session: Deep-Dive anthropic2025aaif

## Objective

Research and document Anthropic's December 2025 donation of MCP to the Agentic AI
Foundation under the Linux Foundation — the final reference (#13 of 13) for our
PEARC'26 paper's Background section.

## Research Process

Searched for information on the AAIF formation:
1. Primary search: "Anthropic MCP Agentic AI Foundation Linux Foundation 2025"

Found comprehensive sources including:
- Anthropic official news post (December 9, 2025)
- MCP blog announcement
- Linux Foundation press release
- OpenAI co-founder announcement
- Block co-founder announcement
- TechCrunch coverage
- GitHub Blog analysis
- The New Stack coverage
- Enterprise analysis (ERP Today, Solo.io)

## Key Findings

### The Foundation

The Agentic AI Foundation (AAIF) is a "directed fund" under the Linux Foundation,
co-founded by Anthropic, Block, and OpenAI on December 9, 2025. This represents
unprecedented alignment among competing frontier model providers.

### Founding Projects

1. **Model Context Protocol (MCP)** — Anthropic
   - Universal standard for connecting AI models to tools/data/applications
   - By December 2025: adopted by ChatGPT, Cursor, Gemini, VS Code, Copilot
   - 97+ million monthly SDK downloads

2. **goose** — Block
   - Open-source, local-first AI agent framework
   - MCP-based integration, thousands of engineers using it weekly

3. **AGENTS.md** — OpenAI
   - Standard for providing agents with project-specific instructions
   - Adopted by 60,000+ open-source projects

### Membership

**Platinum**: AWS, Anthropic, Block, Bloomberg, Cloudflare, Google, Microsoft, OpenAI

**Gold/Silver**: Dozens of enterprise software vendors, developer tools companies,
and startups — representing industry-wide commitment to open agentic infrastructure.

### Quotable Findings

Mike Krieger (Anthropic CPO): "Donating MCP to the Linux Foundation as part of the
AAIF ensures it stays open, neutral, and community-driven as it becomes critical
infrastructure for AI."

David Soria Parra (MCP co-creator): "We're all better off if we have an open
integration center where you can build something once as a developer and use it
across any client."

### Significance for Our Paper

This reference completes our timeline (2017-2025) with MCP achieving "the Linux
Foundation stage" — the same institutional legitimacy as Linux kernel, Kubernetes,
Node.js. For HPC:

1. **Standards-based integration**: HPC centers can build on stable, vendor-neutral
   protocols that won't disappear or fragment
2. **Enterprise-ready governance**: Linux Foundation model provides stability
   research computing organizations require
3. **Ecosystem benefits**: Every major AI assistant will support MCP
4. **The path forward**: MCP servers for HPC tools (schedulers, modules, docs) are
   the path to AI integration

## Artifact Created

Created `outline/notes/refs/anthropic2025aaif.md` with:
- Full YAML frontmatter (bibkey, title, authors, url, key_findings, sample_sentences)
- Comprehensive long-form summary covering:
  - Overview and AAIF formation
  - Governance structure and founding projects
  - Membership roster (platinum/gold/silver)
  - MCP's one-year journey to foundation status
  - Industry significance (competition → collaboration)
  - Web analogy (AAIF as W3C for agents)
  - Enterprise implications
  - Technical continuity
  - Significance for our paper (standards, governance, ecosystem, HPC path)
  - Timeline capstone (2017-2025)
  - References

## Progress Update

Updated `outline/notes/refs/README.md`:
- Marked `anthropic2025aaif` as complete
- Progress: **13/13 references complete ✓**

## Milestone: Reference Deep-Dive Series Complete!

All 13 references now have comprehensive summaries:

### Foundational AI (2017-2023)
1. ✓ vaswani2017attention — Transformers architecture
2. ✓ brown2020gpt3 — GPT-3/scaling laws
3. ✓ openai2022chatgpt — ChatGPT public release
4. ✓ yao2023react — ReAct agentic framework
5. ✓ openai2023gpt4 — GPT-4 capabilities

### Agentic Infrastructure (2024)
6. ✓ anthropic2024claude3 — Claude 3 model family
7. ✓ warp2024agentmode — Warp Agent Mode
8. ✓ anthropic2024mcp — MCP launch

### HPC + AI Intersection (2024-2025)
9. ✓ godoy2024llm — LLM for HPC evaluation
10. ✓ openai2025mcp — Industry MCP adoption
11. ✓ deelman2025hpc — HPC at a Crossroads
12. ✓ whitehouse2025genesis — Genesis Mission EO
13. ✓ anthropic2025aaif — AAIF/MCP donation

## Next Steps

With all reference deep-dives complete, the project can proceed to:
- Writing the Background section prose using the sample sentences
- Synthesizing the timeline narrative (2017-2025)
- Connecting the dots between agentic AI infrastructure and HPC implications
