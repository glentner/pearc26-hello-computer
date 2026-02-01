# Reference Deep-Dive Tracking

Progress tracker for systematic literature review. See `plans/` for full plan details.

## Status Legend

- `[ ]` — Pending
- `[~]` — In Progress  
- `[x]` — Complete

## References (13 total)

### Foundational AI (2017-2023)

- [x] `vaswani2017attention` — Vaswani et al. 2017 — Attention Is All You Need
- [x] `brown2020gpt3` — Brown et al. 2020 — Language Models are Few-Shot Learners
- [x] `openai2022chatgpt` — OpenAI 2022 — Introducing ChatGPT
- [x] `yao2023react` — Yao et al. 2023 — ReAct: Synergizing Reasoning and Acting
- [x] `openai2023gpt4` — OpenAI 2023 — GPT-4 Technical Report

### Agentic Infrastructure (2024)

- [x] `anthropic2024claude3` — Anthropic 2024 — Claude 3 Model Family
- [x] `warp2024agentmode` — Warp 2024 — Agent Mode: LLM in the Terminal
- [x] `anthropic2024mcp` — Anthropic 2024 — Introducing the Model Context Protocol

### HPC + AI Intersection (2024-2025)

- [x] `godoy2024llm` — Godoy et al. 2024 — LLM Evaluation for HPC Software Development
- [x] `openai2025mcp` — OpenAI 2025 — MCP Adoption (TechCrunch)
- [x] `deelman2025hpc` — Deelman et al. 2025 — HPC at a Crossroads (Science)
- [x] `whitehouse2025genesis` — White House 2025 — Genesis Mission Executive Order
- [x] `anthropic2025aaif` — Anthropic 2025 — MCP → Agentic AI Foundation

## Progress

**Completed**: 13/13 ✓

## Session Prompt Template

Use this prompt to start a new deep-dive session:

```
Continue our PEARC'26 paper work. See plan <plan:a91aeec6-aca9-4fdd-999f-52f7174c213a> for context.

Do the next reference deep-dive. Check `outline/notes/refs/README.md` for the next pending item.

For this reference:
1. Research the source material (fetch/read the paper, blog, or document)
2. Create `outline/notes/refs/<bibkey>.md` with full YAML frontmatter and long-form summary
3. Mark it complete in the tracking README
4. Create a session log
5. Commit with "WIP: deep-dive <bibkey>"
```
