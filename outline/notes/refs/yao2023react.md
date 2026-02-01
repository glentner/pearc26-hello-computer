---
bibkey: "yao2023react"
title: "ReAct: Synergizing Reasoning and Acting in Language Models"
authors: "Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao"
year: 2023
source_type: "paper"
url: "https://arxiv.org/abs/2210.03629"
venue: "ICLR 2023 (International Conference on Learning Representations)"
status: "complete"
key_findings:
  - "Introduces the ReAct paradigm: interleaving reasoning traces and task-specific actions in LLMs"
  - "Reasoning traces help induce, track, and update action plans; actions interface with external sources like knowledge bases"
  - "Outperforms pure chain-of-thought (reasoning only) and pure action generation on diverse benchmarks"
  - "On ALFWorld and WebShop, ReAct beats imitation and reinforcement learning by 34% and 10% absolute success rate with only 1-2 in-context examples"
  - "Overcomes hallucination and error propagation in chain-of-thought by grounding reasoning in external observations"
  - "Enables human-in-the-loop behavior correction by editing reasoning traces mid-execution"
sample_sentences: |
  The ReAct framework introduced a paradigm for agentic AI by demonstrating how 
  language models could interleave reasoning traces with task-specific actions, 
  enabling them to interface with external tools and knowledge sources while 
  maintaining interpretable, human-like problem-solving trajectories. This 
  "thought-action-observation" loop became the foundational pattern adopted by 
  virtually all modern agentic AI frameworks.
quotable:
  - "reasoning traces help the model induce, track, and update action plans as well as handle exceptions, while actions allow it to interface with external sources"
  - "ReAct overcomes issues of hallucination and error propagation prevalent in chain-of-thought reasoning"
---
# ReAct: Synergizing Reasoning and Acting in Language Models

## Overview

The ReAct paper, published at ICLR 2023 by researchers from Google Research and 
Princeton University, is widely recognized as the foundational work that defined 
what it means for a language model to be "agentic." Prior to ReAct, the AI 
research community had explored reasoning (via chain-of-thought prompting) and 
acting (via action plan generation) as separate capabilities. ReAct unified these 
into a single paradigm where models alternate between explicit reasoning and 
task-specific actions.

## Core Innovation

The key insight is that reasoning and acting are synergistic:

1. **Reasoning traces** allow the model to:
   - Decompose complex tasks into manageable sub-goals
   - Track progress and maintain working memory
   - Handle exceptions and adjust plans dynamically
   - Make decisions interpretable to humans

2. **Actions** allow the model to:
   - Interface with external knowledge bases (e.g., Wikipedia API)
   - Gather real-time information not present in training data
   - Ground reasoning in actual observations rather than hallucinated facts
   - Affect the environment to make progress toward goals

The interleaved "thought-action-observation" cycle creates a feedback loop where 
the model can course-correct based on actual outcomes rather than proceeding 
blindly through a pre-planned sequence.

## Experimental Results

The paper evaluated ReAct on four diverse benchmarks:

### Knowledge-Intensive Tasks
- **HotpotQA** (multi-hop question answering): ReAct interacts with Wikipedia to 
  retrieve relevant passages, overcoming the hallucination problem in pure 
  chain-of-thought approaches
- **Fever** (fact verification): Similar improvements through grounded retrieval

### Interactive Decision Making
- **ALFWorld** (text-based game): ReAct achieved 34% absolute improvement over 
  imitation and reinforcement learning baselines
- **WebShop** (web navigation): 10% absolute improvement with only 1-2 in-context 
  examples

The combination of ReAct with chain-of-thought (allowing both internal reasoning 
and external information retrieval) produced the best overall performance.

## Impact on Agentic AI

ReAct's influence on the field cannot be overstated:

1. **LangChain** implemented ReAct as its primary agent architecture 
   (ZERO_SHOT_REACT_DESCRIPTION), making it the default pattern for building 
   LLM-powered applications with tool use

2. **LangGraph** uses ReAct's thought-action-observation loop as the foundation 
   for its graph-based agent design

3. **Every major agentic framework** (CrewAI, AutoGPT, BabyAGI, etc.) implements 
   variations of the ReAct pattern

4. **Modern ADEs like Warp** implement ReAct-style workflows where the agent 
   reasons about tasks, takes actions (file edits, shell commands), observes 
   results, and adjusts its approach

## Human-in-the-Loop Capability

A particularly notable finding is that ReAct's explicit reasoning traces enable 
easy human intervention. By editing just a few thought traces, humans can 
redirect agent behavior—far easier than editing model parameters or retraining. 
This foreshadows the collaborative human-AI workflows that define modern agentic 
development environments.

## Relevance to Our Paper

ReAct provides the theoretical foundation for the "agentic" paradigm we examine:

- **Defines "agentic"**: The paper's framework of reasoning + acting + observing 
  is precisely what distinguishes an agent from a chatbot
- **Tool use pattern**: The thought-action-observation loop is exactly what Warp 
  implements when it reasons about code, runs commands, and adjusts based on 
  output
- **Human collaboration**: ReAct's interpretable traces and editability prefigure 
  the human-AI collaboration model we explore for HPC development

The paper answers a key question for our Background section: What makes an AI 
system "agentic"? ReAct's answer—interleaved reasoning and acting with external 
tool integration—is now the consensus definition used throughout industry and 
academia.

## Citation

```bibtex
@inproceedings{yao2023react,
  title     = {{ReAct}: Synergizing Reasoning and Acting in Language Models},
  author    = {Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and 
               Shafran, Izhak and Narasimhan, Karthik and Cao, Yuan},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year      = {2023},
  url       = {https://arxiv.org/abs/2210.03629}
}
```
