---
session_start: "2026-02-01T00:37:34Z"
session_end: "2026-02-01T00:42:04Z"
task: "Reference deep-dive #9: godoy2024llm"
user_input: |
  Continue our PEARC'26 paper work. See plan <plan:a91aeec6-aca9-4fdd-999f-52f7174c213a> for context.

  Do the next reference deep-dive. Check `outline/notes/refs/README.md` for the next pending item.

  For this reference:
  1. Research the source material (fetch/read the paper, blog, or document)
  2. Create `outline/notes/refs/<bibkey>.md` with full YAML frontmatter and long-form summary
  3. Mark it complete in the tracking README
  4. Create a session log
  5. Commit with "WIP: deep-dive <bibkey>"
files_modified:
  - outline/notes/refs/godoy2024llm.md (created)
  - outline/notes/refs/README.md (updated checkbox and progress counter)
  - logs/2026-02-01T00-42-deep-dive-godoy2024llm.md (created)
---

# Session Log: Deep-Dive godoy2024llm

## Reference Details

- **Bibkey**: godoy2024llm
- **Title**: Large Language Model Evaluation for High-Performance Computing Software Development
- **Authors**: William F. Godoy, Pedro Valero-Lara, Keita Teranishi, Prasanna Balaprakash, Jeffrey S. Vetter
- **Source**: Concurrency and Computation: Practice and Experience, Vol. 36, Issue 26 (2024)
- **DOI**: 10.1002/cpe.8269
- **Affiliation**: Oak Ridge National Laboratory

## Research Process

1. Searched for the paper via web search, found primary source at Wiley Online Library
2. Found OSTI.GOV entry confirming DOE/ORNL authorship and publication details
3. Located earlier conference paper (ICPP Workshops 2023, arXiv:2306.15121) that this extends
4. Gathered details on methodology, kernels tested, programming models evaluated
5. Identified key findings on LLM correctness correlation with programming model maturity

## Key Takeaways for Our Paper

This is the most directly relevant prior work for our paper's thesis:

1. **Training Data Gap**: LLMs are trained on general-purpose code with far fewer HPC-specific examples, limiting their effectiveness for parallel programming tasks

2. **Maturity Correlation**: Correctness correlates with programming model maturity—OpenMP/CUDA perform well, newer frameworks like HIP lag behind

3. **Stochastic Nature**: No experiments achieved perfect scores, highlighting that LLM output requires human review

4. **Iterative Potential**: The auto-parallelization experiments used ChatGPT "interactively giving simple prompts as in a dialogue"—this hints at the agentic approach we advocate

5. **National Lab Credibility**: Coming from ORNL researchers, this carries weight in the HPC community

## Sample Sentences for Background Section

> Prior work from Oak Ridge National Laboratory systematically evaluated GPT-3/Codex capabilities for HPC kernel generation across C++, Fortran, Python, and Julia, finding that correctness correlated with programming model maturity—mature frameworks like OpenMP and CUDA performed well while newer options like HIP showed gaps. This work established that while LLMs show promise for HPC code assistance, their training data underrepresents the specialized parallel programming patterns common in scientific computing.

## Progress Update

- **Completed**: 9/13 references
- **Remaining**: openai2025mcp, deelman2025hpc, whitehouse2025genesis, anthropic2025aaif
