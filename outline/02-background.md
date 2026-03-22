---
status: draft
target_words: 300
actual_words: ~280
citations:
  - vaswani2017attention  # Transformer (used)
  - brown2020gpt3         # GPT-3 scaling (used)
  - openai2022chatgpt     # ChatGPT launch (used)
  - yao2023react          # ReAct (used)
  - warp2024agentmode     # Warp ADE (used)
  - anthropic2024mcp      # MCP announcement (used)
  - openai2025mcp         # OpenAI adopts MCP (used)
  - anthropic2025aaif     # MCP → AAIF (used)
  - deelman2025hpc        # HPC at Crossroads (ADD - before Genesis)
  - whitehouse2025genesis # Genesis Mission (used)
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

The trajectory from research curiosity to practical tool was swift. In 2017, Vaswani et al.
introduced the Transformer architecture, replacing recurrence with attention mechanisms. By
2020, GPT-3's 175 billion parameters demonstrated that scale alone could yield emergent
capabilities. ChatGPT's November 2022 launch brought these capabilities to the general
public, reaching 100 million users in two months.

A parallel development transformed chatbots into *agents*. The ReAct framework formalized
this shift: agentic systems interleave reasoning traces with task-specific actions,
interfacing with external tools and knowledge sources rather than relying solely on
training data. Today's agentic development environments implement this pattern: reading
files, executing commands, editing code, and iterating based on observed results.

The infrastructure for agentic AI has matured rapidly. Anthropic's Model Context Protocol
(MCP), released November 2024, provides a standardized interface for AI systems to connect
with external data sources and tools, analogous to how the Language Server Protocol unified
IDE tooling. By March 2025, OpenAI and Google had adopted MCP; by December, Anthropic
donated it to the Linux Foundation's Agentic AI Foundation, with over 10,000 active public
servers.

For HPC, this convergence is consequential. Deelman et al. argue that high-performance
computing stands at a crossroads. The Genesis Mission executive order (November 2025)
charges DOE with uniting national laboratories, supercomputers, and AI capabilities for
scientific discovery. The question is no longer whether AI will integrate with HPC
workflows, but how, and who will shape that integration.
