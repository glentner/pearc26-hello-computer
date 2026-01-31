# Annotated Bibliography

References for the Background section and throughout the manuscript.

## Foundational AI Papers

### Transformer Architecture

**Vaswani et al. (2017). "Attention Is All You Need."**
- **Citation**: Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you need. In *Advances in Neural Information Processing Systems* (NeurIPS 2017).
- **arXiv**: https://arxiv.org/abs/1706.03762
- **Relevance**: The foundational paper introducing the Transformer architecture. All modern LLMs derive from this work. The title is itself a Beatles reference ("All You Need Is Love"), fitting our whimsical theme.
- **Key quote for paper**: Proposed "a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely."

### GPT-4

**OpenAI (2023). "GPT-4 Technical Report."**
- **Citation**: OpenAI. (2023). GPT-4 Technical Report. arXiv:2303.08774.
- **arXiv**: https://arxiv.org/abs/2303.08774
- **Relevance**: Documents the capabilities of GPT-4, a milestone in demonstrating LLM practical utility. Notable for benchmark performance (top 10% on bar exam) and multimodal capabilities.
- **Key point**: GPT-4 "exhibits human-level performance on various professional and academic benchmarks" while still suffering from "hallucinations" and limited context windows.

## Model Context Protocol (MCP)

**Anthropic (2024). "Introducing the Model Context Protocol."**
- **Citation**: Anthropic. (2024, November 25). Introducing the Model Context Protocol. https://www.anthropic.com/news/model-context-protocol
- **Relevance**: Announcement of MCP as an open standard. Describes the problem of AI systems being "trapped behind information silos" and MCP as "a universal, open standard for connecting AI systems with data sources."
- **Key timeline**: Released November 2024, adopted by OpenAI/Google by March 2025, donated to Linux Foundation's Agentic AI Foundation December 2025.

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
- **Relevance**: Perspective piece on HPC's evolution with AI. Authoritative voices on HPC's future direction.

## Timeline for Background Section

| Year | Event |
|------|-------|
| 2017 | Transformer architecture (Vaswani et al.) |
| 2020 | GPT-3 demonstrates scaling laws |
| 2022 | ChatGPT public release (Nov 30) |
| 2023 | GPT-4 release (March), Claude 2, Gemini |
| 2024 | Claude 3, MCP release (Nov), agentic capabilities emerge |
| 2025 | MCP adoption explodes, IDE integration mainstream |
| 2026 | Present day - HPC centers engaging with agentic AI |

## Additional References to Find

- [ ] Claude 3/3.5 technical details (Anthropic)
- [ ] Warp terminal agentic features announcement
- [ ] DOE ASCR AI for Science program ($68M, 2024)
- [ ] Any PEARC/SC papers on AI + HPC support

## BibTeX Entries

```bibtex
@inproceedings{vaswani2017attention,
  title={Attention is All You Need},
  author={Vaswani, Ashish and Shazeer, Noam and Parmar, Niki and Uszkoreit, Jakob and Jones, Llion and Gomez, Aidan N and Kaiser, {\L}ukasz and Polosukhin, Illia},
  booktitle={Advances in Neural Information Processing Systems},
  volume={30},
  year={2017}
}

@article{openai2023gpt4,
  title={GPT-4 Technical Report},
  author={OpenAI},
  journal={arXiv preprint arXiv:2303.08774},
  year={2023}
}

@misc{anthropic2024mcp,
  title={Introducing the Model Context Protocol},
  author={Anthropic},
  year={2024},
  month={November},
  url={https://www.anthropic.com/news/model-context-protocol}
}

@article{godoy2024llm,
  title={Large language model evaluation for high-performance computing software development},
  author={Godoy, William F and Valero-Lara, Pedro and Teranishi, Keita and Balaprakash, Prasanna and Vetter, Jeffrey S},
  journal={Concurrency and Computation: Practice and Experience},
  volume={36},
  number={26},
  pages={e8269},
  year={2024}
}

@article{deelman2025hpc,
  title={High-performance computing at a crossroads},
  author={Deelman, Ewa and Dongarra, Jack and Hendrickson, Bruce and Randles, Amanda and Reed, Daniel and Seidel, Edward and Yelick, Katherine},
  journal={Science},
  volume={387},
  number={6736},
  pages={829--831},
  year={2025}
}
```

## Notes on Citing

- For the Background section, focus on Vaswani (transformers) and timeline events
- MCP references belong in Approach section
- HPC+AI market data could support Introduction (why now?)
- Godoy/Deelman papers show HPC community is actively engaging with this topic
