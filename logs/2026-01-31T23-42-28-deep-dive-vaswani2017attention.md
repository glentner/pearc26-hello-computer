---
session_start: 2026-01-31T23:42:28Z
session_type: reference_deep_dive
reference: vaswani2017attention
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
  - outline/notes/refs/vaswani2017attention.md (created)
  - outline/notes/refs/README.md (updated progress)
commits:
  - "WIP: deep-dive vaswani2017attention"
---

# Reference Deep-Dive: vaswani2017attention

## Summary

Completed the first reference deep-dive for the PEARC'26 paper systematic literature review.
Researched "Attention Is All You Need" (Vaswani et al., 2017)—the foundational Transformer
paper that enabled the LLM revolution.

## Actions Taken

1. **Research**: Used web search to gather comprehensive information about the paper,
   including arXiv abstract, NeurIPS proceedings, Wikipedia summary, and citation statistics.

2. **Created reference file**: `outline/notes/refs/vaswani2017attention.md` with:
   - Complete YAML frontmatter (bibkey, title, authors, year, source_type, URL, venue, status)
   - Key findings (5 bullet points)
   - Sample sentences ready for Background section prose
   - Long-form summary covering:
     - Overview and context
     - The problem being solved (RNN limitations)
     - Transformer innovations (self-attention, multi-head attention, position encodings)
     - Results and benchmarks
     - Relevance to our paper's thesis
     - Citation statistics and trivia

3. **Updated tracking**: Marked complete in `outline/notes/refs/README.md`, updated
   progress counter from 0/13 to 1/13.

## Key Takeaways for Our Paper

The Transformer's **parallelizability** is the critical insight for our HPC narrative:
- RNNs processed tokens sequentially—couldn't leverage parallel hardware
- Transformers process all tokens simultaneously via attention
- This architectural choice is what made scaling to 175B+ parameters feasible
- Without this, the entire LLM revolution (and thus agentic tools) wouldn't exist

## Sample Prose for Background Section

> The Transformer architecture, introduced by Vaswani et al. (2017), replaced recurrent and
> convolutional layers with pure attention mechanisms, enabling unprecedented parallelization
> during training. This architectural innovation became the foundation for all subsequent
> large language models, with the paper accumulating over 173,000 citations by 2025.

## Progress

Reference deep-dive tracking: **1/13 complete**

Next pending: `brown2020gpt3` — Brown et al. 2020 — Language Models are Few-Shot Learners
