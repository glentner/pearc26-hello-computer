# Annotated Bibliography

References for the Background section and throughout the manuscript.

## Foundational AI Papers

### Transformer Architecture (2017)

**Vaswani et al. (2017). "Attention Is All You Need."**
- **Citation**: Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you need. In *Advances in Neural Information Processing Systems* (NeurIPS 2017).
- **arXiv**: https://arxiv.org/abs/1706.03762
- **BibTeX key**: `vaswani2017attention`
- **Relevance**: The foundational paper introducing the Transformer architecture. All modern LLMs derive from this work. The title is itself a Beatles reference ("All You Need Is Love"), fitting our whimsical theme.
- **Key quote for paper**: Proposed "a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely."

### GPT-3 and Scaling Laws (2020)

**Brown et al. (2020). "Language Models are Few-Shot Learners."**
- **Citation**: Brown, T. B., Mann, B., Ryder, N., et al. (2020). Language Models are Few-Shot Learners. In *Advances in Neural Information Processing Systems* (NeurIPS 2020).
- **arXiv**: https://arxiv.org/abs/2005.14165
- **BibTeX key**: `brown2020gpt3`
- **Relevance**: Introduces GPT-3 with 175 billion parameters—10x larger than any previous non-sparse model. Demonstrates that scaling up enables task-agnostic few-shot performance without fine-tuning. Critical milestone showing emergent capabilities from scale.
- **Key point**: "Scaling up language models greatly improves task-agnostic, few-shot performance, sometimes even becoming competitive with prior state-of-the-art fine-tuning approaches."

### ChatGPT Public Launch (2022)

**OpenAI (2022). "Introducing ChatGPT."**
- **Citation**: OpenAI. (2022, November 30). Introducing ChatGPT. https://openai.com/blog/chatgpt
- **BibTeX key**: `openai2022chatgpt`
- **Relevance**: The public release that sparked mainstream AI awareness. Reached 100 million users in 2 months—fastest-growing consumer application in history. Triggered industry-wide response (Google "code red", Microsoft partnership).
- **Key point**: Demonstrated that conversational AI was ready for general public use, fundamentally changing public perception of AI capabilities.

### ReAct: Agentic AI Foundations (2022/2023)

**Yao et al. (2023). "ReAct: Synergizing Reasoning and Acting in Language Models."**
- **Citation**: Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2023). ReAct: Synergizing Reasoning and Acting in Language Models. In *ICLR 2023*.
- **arXiv**: https://arxiv.org/abs/2210.03629 (October 2022)
- **BibTeX key**: `yao2023react`
- **Relevance**: Foundational paper defining what makes AI systems "agentic." Introduces interleaved reasoning traces and task-specific actions—reasoning helps induce/track/update action plans while actions interface with external sources.
- **Key point**: "ReAct prompts LLMs to generate both verbal reasoning traces and actions pertaining to a task in an interleaved manner." This is the theoretical basis for tool-using AI agents.

### GPT-4 (2023)

**OpenAI (2023). "GPT-4 Technical Report."**
- **Citation**: OpenAI. (2023). GPT-4 Technical Report. arXiv:2303.08774.
- **arXiv**: https://arxiv.org/abs/2303.08774
- **BibTeX key**: `openai2023gpt4`
- **Relevance**: Documents the capabilities of GPT-4, a milestone in demonstrating LLM practical utility. Notable for benchmark performance (top 10% on bar exam) and multimodal capabilities.
- **Key point**: GPT-4 "exhibits human-level performance on various professional and academic benchmarks" while still suffering from "hallucinations" and limited context windows.

### Claude 3 Model Family (2024)

**Anthropic (2024). "The Claude 3 Model Family: Opus, Sonnet, Haiku."**
- **Citation**: Anthropic. (2024, March). The Claude 3 Model Family: Opus, Sonnet, Haiku. Model Card.
- **URL**: https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf
- **BibTeX key**: `anthropic2024claude3`
- **Relevance**: Official technical documentation for Claude 3 family. Covers three model tiers (Opus/Sonnet/Haiku), multimodal vision capabilities, safety evaluations per Responsible Scaling Policy.
- **Key point**: Claude 3 Opus "sets new industry benchmarks across a wide range of cognitive tasks" including MMLU, GPQA, and GSM8K.

## Agentic Development Environments

**Warp (2024). "Agent Mode: LLM embedded in the terminal for multi-step workflows."**
- **Citation**: Warp. (2024, June 17). Agent Mode: LLM embedded in the terminal for multi-step workflows. https://www.warp.dev/blog/agent-mode
- **BibTeX key**: `warp2024agentmode`
- **Relevance**: Announcement of Warp's Agent Mode—the first "Agentic Development Environment" (ADE) concept. Embeds LLM directly into terminal for multi-step workflows with tool use. Represents shift from AI as assistant to AI as collaborator.
- **Key point**: "Agent Mode raises the level of abstraction in the terminal. Using natural language, you can ask the terminal to accomplish any high level task without worrying about the specific commands you need."
- **Note**: Directly relevant to our paper's tooling focus—we use Warp for this manuscript's development.

## Model Context Protocol (MCP)

**Anthropic (2024). "Introducing the Model Context Protocol."**
- **Citation**: Anthropic. (2024, November 25). Introducing the Model Context Protocol. https://www.anthropic.com/news/model-context-protocol
- **BibTeX key**: `anthropic2024mcp`
- **Relevance**: Announcement of MCP as an open standard. Describes the problem of AI systems being "trapped behind information silos" and MCP as "a universal, open standard for connecting AI systems with data sources."
- **Key timeline**: Released November 2024, adopted by OpenAI/Google by March 2025, donated to Linux Foundation's Agentic AI Foundation December 2025.

**OpenAI MCP Adoption (2025)**
- **Citation**: Wiggers, K. (2025, March 26). OpenAI adopts rival Anthropic's standard for connecting AI models to data. TechCrunch.
- **URL**: https://techcrunch.com/2025/03/26/openai-adopts-rival-anthropics-standard-for-connecting-ai-models-to-data/
- **BibTeX key**: `openai2025mcp`
- **Relevance**: Signals industry convergence on MCP as the standard for agentic tool integration. Sam Altman: "People love MCP and we are excited to add support across our products."
- **Key point**: When competitors adopt each other's standards, it indicates genuine technical merit and market demand.

**Anthropic (2025). "Donating the Model Context Protocol and establishing the Agentic AI Foundation."**
- **Citation**: Anthropic. (2025, December 9). Donating the Model Context Protocol and establishing the Agentic AI Foundation. https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation
- **BibTeX key**: `anthropic2025aaif`
- **Relevance**: MCP donated to Linux Foundation's new Agentic AI Foundation (AAIF), co-founded by Anthropic, OpenAI, and Block with support from Google, Microsoft, AWS, Cloudflare, Bloomberg. Shows maturation of agentic infrastructure into vendor-neutral open standard.
- **Key point**: "There are now more than 10,000 active public MCP servers" and "97 million monthly SDK downloads."

**MCP Specification**
- **Citation**: Anthropic. (2025). Model Context Protocol Specification. https://modelcontextprotocol.io/specification/
- **Relevance**: Technical specification for implementing MCP servers and clients. Defines tools, resources, and transport mechanisms (stdio, HTTP+SSE).
- **Note**: Compare to Language Server Protocol (LSP) for IDE tooling standardization.

## AI + HPC Intersection

**Hyperion Research (2025). HPC/AI Market Report.**
- **Citation**: Hyperion Research. (2025, April). HPC/AI Market Grew by 23.5% in 2024.
- **Relevance**: Market data showing AI integration into HPC: "AI is used by over 78% of all HPC sites around the world." Market reached $60B in 2024, projected to exceed $100B by 2028.
- **Key stat**: 92% of HPC organizations are engaging with AI in some form (Intersect360 2024 survey).

**Godoy et al. (2024). "Large Language Model Evaluation for HPC Software Development."**
- **Citation**: Godoy, W.F., Valero-Lara, P., Teranishi, K., Balaprakash, P., & Vetter, J.S. (2024). Large language model evaluation for high-performance computing software development. *Concurrency and Computation: Practice and Experience*, 36(26), e8269.
- **Relevance**: Direct evaluation of LLMs for HPC code generation. Examines OpenAI Codex for parallel programming models.

**Deelman et al. (2025). "High-Performance Computing at a Crossroads."**
- **Citation**: Deelman, E., Dongarra, J., Hendrickson, B., Randles, A., Reed, D., Seidel, E., & Yelick, K. (2025). High-performance computing at a crossroads. *Science*, 387(6736), 829-831.
- **BibTeX key**: `deelman2025hpc`
- **Relevance**: Perspective piece on HPC's evolution with AI. Authoritative voices on HPC's future direction.

## AI + Science Policy

**The White House (2025). "Launching the Genesis Mission."**
- **Citation**: The White House. (2025, November 24). Launching the Genesis Mission. Executive Order.
- **URL**: https://www.whitehouse.gov/presidential-actions/2025/11/launching-the-genesis-mission/
- **BibTeX key**: `whitehouse2025genesis`
- **Relevance**: DOE-led national initiative to accelerate AI for scientific discovery. Framed as "Manhattan Project-scale" effort. Partners include Microsoft, OpenAI, Google, Nvidia, AMD, AWS, Anthropic. Establishes American Science and Security Platform integrating national lab supercomputers, datasets, and AI capabilities.
- **Key point**: "The Genesis Mission charges the Secretary of Energy with leveraging our National Laboratories to unite America's brightest minds, most powerful computers, and vast scientific data into one cooperative system for research."
- **Priority domains**: Advanced manufacturing, biotechnology, critical materials, nuclear fission/fusion, quantum information science, semiconductors.

## Timeline for Background Section

| Year | Event | BibTeX Key |
|------|-------|------------|
| 2017 | Transformer architecture | `vaswani2017attention` |
| 2020 | GPT-3 demonstrates scaling laws | `brown2020gpt3` |
| 2022 | ChatGPT public release (Nov 30) | `openai2022chatgpt` |
| 2022 | ReAct paper defines "agentic" | `yao2023react` |
| 2023 | GPT-4 release (March) | `openai2023gpt4` |
| 2024 | Claude 3 model family (March) | `anthropic2024claude3` |
| 2024 | Warp Agent Mode / first ADE (June) | `warp2024agentmode` |
| 2024 | MCP release (November) | `anthropic2024mcp` |
| 2024 | LLM evaluation for HPC | `godoy2024llm` |
| 2025 | OpenAI adopts MCP (March) | `openai2025mcp` |
| 2025 | HPC at a Crossroads (Science) | `deelman2025hpc` |
| 2025 | Genesis Mission EO (November) | `whitehouse2025genesis` |
| 2025 | MCP → Linux Foundation (December) | `anthropic2025aaif` |
| 2026 | Present day - HPC centers engaging with agentic AI | — |

## Additional References (Completed)

- [x] Claude 3/3.5 technical details → `anthropic2024claude3`
- [x] Warp terminal agentic features → `warp2024agentmode`
- [x] Genesis Mission (replaces DOE ASCR) → `whitehouse2025genesis`
- [ ] Any PEARC/SC papers on AI + HPC support (optional, may not need)

## BibTeX Entries

All BibTeX entries are maintained in `references.bib` at the repository root.

**Current entries (13 total):**
- `vaswani2017attention` - Transformer architecture
- `brown2020gpt3` - GPT-3 scaling laws
- `openai2022chatgpt` - ChatGPT launch
- `yao2023react` - ReAct agentic foundations
- `openai2023gpt4` - GPT-4 technical report
- `anthropic2024claude3` - Claude 3 model card
- `warp2024agentmode` - Warp Agent Mode / ADE
- `anthropic2024mcp` - MCP announcement
- `godoy2024llm` - LLM for HPC evaluation
- `openai2025mcp` - OpenAI MCP adoption
- `deelman2025hpc` - HPC at a Crossroads
- `whitehouse2025genesis` - Genesis Mission EO
- `anthropic2025aaif` - MCP → AAIF donation

## Notes on Citing

- For the Background section, focus on Vaswani (transformers) and timeline events
- MCP references belong in Approach section
- HPC+AI market data could support Introduction (why now?)
- Godoy/Deelman papers show HPC community is actively engaging with this topic
