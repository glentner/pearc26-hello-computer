---
status: draft
target_words: 300
---

# Background

## Key Points
- Brief AI timeline: transformers (2017) → GPT series → Claude/Gemini → agentic systems
- Definition: what makes a system "agentic" (tool use, multi-step reasoning, autonomy)
- Current state of the art: coding assistants, MCP protocol, IDE integration
- Why now: capability threshold crossed for practical HPC workflows

## Notes
- This section is intentionally more formal/dry to contrast with the whimsical sections
- See `notes/bibliography.md` for full annotated bibliography

## Key References
- **Vaswani et al. (2017)**: "Attention Is All You Need" - Transformer architecture foundation
- **OpenAI (2023)**: GPT-4 Technical Report - benchmark performance milestone
- **Anthropic (2024)**: MCP announcement - standardization of tool use
- **Godoy et al. (2024)**: LLM evaluation for HPC software development
- **Deelman et al. (2025)**: "HPC at a Crossroads" - Science perspective

## Timeline to Cover
| Year | Milestone |
|------|----------|
| 2017 | Transformer architecture (Vaswani et al.) |
| 2020 | GPT-3 demonstrates scaling laws |
| 2022 | ChatGPT public release (Nov 30) - public awareness explosion |
| 2023 | GPT-4 release (March) - "human-level" benchmarks |
| 2024 | Claude 3, MCP release (Nov), agentic capabilities emerge |
| 2025 | MCP adopted by OpenAI/Google, IDE integration mainstream |
| 2026 | HPC centers actively engaging with agentic AI |

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
