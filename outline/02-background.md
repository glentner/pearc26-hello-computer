---
status: draft
target_words: 300
---

# Background

## Key Points
- Brief AI timeline: transformers (2017) → GPT series → Claude/Gemini → agentic systems
- Definition: what makes a system "agentic" (tool use, multi-step reasoning, autonomy) → cite ReAct
- Current state of the art: coding assistants, MCP protocol, ADE integration
- Why now: capability threshold crossed for practical HPC workflows + Genesis Mission policy

## Notes
- This section is intentionally more formal/dry to contrast with the whimsical sections
- See `notes/bibliography.md` for full annotated bibliography (13 references)

## Key References (Complete Set)

**Foundational AI:**
- `vaswani2017attention`: Transformer architecture foundation (2017)
- `brown2020gpt3`: GPT-3 scaling laws - 175B parameters (2020)
- `openai2022chatgpt`: ChatGPT public launch - 100M users in 2 months (2022)
- `yao2023react`: ReAct - defines "agentic" (reasoning + acting) (2022/2023)
- `openai2023gpt4`: GPT-4 - "human-level" benchmarks (2023)
- `anthropic2024claude3`: Claude 3 model family (2024)

**Agentic Infrastructure:**
- `warp2024agentmode`: Warp Agent Mode - first ADE concept (2024)
- `anthropic2024mcp`: MCP announcement (2024)
- `openai2025mcp`: OpenAI adopts MCP (2025)
- `anthropic2025aaif`: MCP → Linux Foundation/AAIF (2025)

**HPC + AI:**
- `godoy2024llm`: LLM evaluation for HPC software development (2024)
- `deelman2025hpc`: "HPC at a Crossroads" - Science (2025)
- `whitehouse2025genesis`: Genesis Mission EO - DOE AI+science initiative (2025)

## Timeline to Cover
| Year | Milestone | Citation |
|------|-----------|----------|
| 2017 | Transformer architecture | `vaswani2017attention` |
| 2020 | GPT-3 demonstrates scaling laws | `brown2020gpt3` |
| 2022 | ChatGPT public release (Nov 30) | `openai2022chatgpt` |
| 2022 | ReAct defines "agentic" systems | `yao2023react` |
| 2023 | GPT-4 - "human-level" benchmarks | `openai2023gpt4` |
| 2024 | Claude 3 model family | `anthropic2024claude3` |
| 2024 | Warp Agent Mode - first ADE | `warp2024agentmode` |
| 2024 | MCP release (November) | `anthropic2024mcp` |
| 2025 | OpenAI/Google adopt MCP | `openai2025mcp` |
| 2025 | Genesis Mission EO (November) | `whitehouse2025genesis` |
| 2025 | MCP → Linux Foundation (December) | `anthropic2025aaif` |
| 2026 | Present day - HPC centers engaging with agentic AI | — |

## Technical Context
- What is MCP (Model Context Protocol)?
  - Standardized way for AI to connect to external data/tools
  - Compared to LSP (Language Server Protocol) for IDEs
  - Transports: stdio (local), HTTP+SSE (remote)
- How do agentic systems differ from chatbots?
  - Tool use: read files, run commands, make edits
  - Multi-step reasoning and planning
  - Autonomy with guardrails
- Why HPC matters:
  - 78% of HPC sites using AI (Hyperion 2025)
  - 92% of HPC orgs engaging with AI (Intersect360 2024)
  - $60B market in 2024, projected $100B by 2028

## Draft

[To be written]
