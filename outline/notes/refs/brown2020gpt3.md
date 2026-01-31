---
bibkey: "brown2020gpt3"
title: "Language Models are Few-Shot Learners"
authors: "Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, Dario Amodei"
year: 2020
source_type: "paper"
url: "https://arxiv.org/abs/2005.14165"
venue: "NeurIPS 2020"
status: "complete"
key_findings:
  - "175 billion parameters—10x larger than any previous non-sparse language model and 100x larger than GPT-2"
  - "Demonstrated few-shot learning: the model learns tasks from just a handful of examples in the prompt, without gradient updates"
  - "In-context learning emerged as a capability that scales with model size—larger models make better use of context"
  - "Achieved state-of-the-art on TriviaQA (71.2%) and competitive results across 20+ NLP benchmarks without task-specific fine-tuning"
  - "Generated news articles that human evaluators struggled to distinguish from human-written content (12% accuracy in one case)"
sample_sentences: |
  Brown et al. (2020) demonstrated that scaling language models to 175 billion parameters
  unlocked emergent few-shot learning capabilities, where GPT-3 could adapt to new tasks
  from just a handful of examples without any weight updates. This discovery that scale
  alone could produce qualitatively new abilities fundamentally reshaped AI research,
  establishing the paradigm of ever-larger foundation models.
---

# Language Models are Few-Shot Learners

## Overview

Published in May 2020 on arXiv and presented at NeurIPS 2020, "Language Models are Few-Shot
Learners" introduced GPT-3—the model that proved scale is the key unlock for emergent AI
capabilities. The 31-author paper from OpenAI demonstrated that a 175 billion parameter
language model, trained on a large internet corpus, could perform a wide variety of tasks
it was never explicitly trained for, simply by being shown a few examples in its prompt.

GPT-3 was described as a "watershed moment" in AI research that definitively confirmed the
benefit of large-scale pretraining. The model is 100x larger than its predecessor GPT-2
(1.5B parameters) and remains architecturally similar—a decoder-only Transformer—but the
massive scale produced qualitatively different behavior.

## The Problem Being Solved

Prior to GPT-3, the standard approach to NLP was:
1. Pre-train a language model on large text corpora
2. Fine-tune on task-specific datasets with thousands of labeled examples

While this approach worked well, it had significant limitations:
- Required substantial labeled data for each new task
- Created task-specific models rather than general-purpose systems
- Contrasted with human learning: humans can perform new tasks from just a few examples
  or simple instructions

The paper's central hypothesis: sufficiently large language models might not need fine-tuning
at all. Instead, they could learn to perform tasks "in-context" from examples provided in
the prompt.

## The GPT-3 Scale

### Model Architecture

GPT-3 maintains the same decoder-only Transformer architecture as GPT-2, with some
modifications for training stability at scale:
- Alternating dense and sparse attention layers
- 175 billion parameters requiring 350GB of storage (16-bit precision)
- 2048 token context window
- 96 layers, 96 attention heads, 12,288 embedding dimensions (for the largest model)

The GPT-3 "family" actually includes 8 models ranging from 125M to 175B parameters, enabling
systematic study of how capabilities scale with size.

### Training Data

Training data composition (weighted):
- **Common Crawl** (60%): 410B tokens, filtered and deduplicated
- **WebText2** (22%): 19B tokens, curated web pages
- **Books1** (8%): 12B tokens
- **Books2** (8%): 55B tokens
- **Wikipedia** (3%): 3B tokens

Total: ~300 billion tokens of training data. The model was trained on NVIDIA V100 GPUs on
a high-bandwidth cluster.

## Few-Shot Learning: The Core Innovation

GPT-3 was evaluated in three settings:

### Zero-Shot
The model receives only a natural language instruction describing the task. No examples.
Example: "Translate English to French: cheese =>"

### One-Shot
The model receives one demonstration example before the actual task.
Example: "sea otter => loutre de mer. cheese =>"

### Few-Shot
The model receives multiple demonstrations (typically 10-100, limited by context window).
This is also called "in-context learning"—the model doesn't update its weights; it uses
the examples as context for generating outputs.

### Key Discovery: Scale Enables Few-Shot Learning

The critical finding: few-shot performance improves more rapidly with model size than
zero-shot performance. Larger models are dramatically better at learning from in-context
examples. This suggests in-context learning is an "emergent" capability that only manifests
at sufficient scale.

The paper states that GPT-3 "achieves promising results in the zero-shot and one-shot
settings, and in the few-shot setting is sometimes competitive with or even occasionally
surpasses state-of-the-art (despite state-of-the-art being held by fine-tuned models)."

## Benchmark Results

### Language Understanding

On SuperGLUE benchmark tasks:
- Performance increased steadily with model size
- Few-shot GPT-3 approached fine-tuned BERT-Large with 8 examples per context
- The gap between GPT-3 with one example vs. eight examples roughly equaled the gap between
  BERT-Large and BERT++

### Question Answering

- **TriviaQA** (closed-book): 71.2% few-shot accuracy—state-of-the-art for closed-book setting
- **CoQA**: 85.0 F1 in few-shot setting (from 81.5 zero-shot, 84.0 one-shot)

### Arithmetic

Perhaps the most surprising emergent capability. The largest GPT-3 model could:
- Reliably perform 2-digit arithmetic
- Usually correctly perform 3-digit arithmetic
- Correctly solve 4-5 digit arithmetic and 2-digit multiplication a "significant fraction"
  of the time

There was a dramatic jump from the 13B parameter model to the 175B model on arithmetic
tasks—evidence of emergence at scale.

### Text Generation

GPT-3 generated news articles that human evaluators had difficulty distinguishing from
human-written articles. In one case, evaluators correctly identified GPT-3 text only 12%
of the time (near random chance).

## Limitations Acknowledged

The paper is notably honest about GPT-3's limitations:

1. **Text generation weaknesses**: Repetition, loss of coherence over long passages,
   self-contradiction

2. **Structural reasoning**: Difficulty with tasks requiring systematic comparison or
   knowledge of which examples to learn from

3. **Bidirectional context**: As a unidirectional model, GPT-3 may struggle on tasks
   requiring bidirectional context (where BERT-style models excel)

4. **Sample efficiency**: While few-shot learning is impressive, it's still less sample-
   efficient than human learning

5. **Interpretability**: No insight into what the model actually "learns" from in-context
   examples or whether it's truly learning vs. pattern matching

6. **Training data issues**: Methodological concerns about benchmark contamination from
   training on large web corpora

## Why This Paper Matters for Our Paper

GPT-3 established the central insight driving the current AI revolution: **scale produces
emergent capabilities**. This has profound implications for HPC:

1. **Compute hunger**: Training GPT-3 required approximately 3.14 × 10²³ FLOPs. This level
   of compute is only achievable through large-scale distributed training on specialized
   hardware clusters.

2. **Foundation model paradigm**: GPT-3 demonstrated that a single, general-purpose model
   could replace dozens of task-specific systems. This "foundation model" paradigm now
   dominates AI development.

3. **The path to agentic AI**: GPT-3's few-shot learning showed that LLMs could adapt to
   novel tasks at inference time. This flexibility is the foundation of agentic systems
   that reason, plan, and use tools.

4. **Scale as moat**: The paper sparked an arms race in model scale, with significant
   implications for HPC infrastructure investment and the democratization (or concentration)
   of AI capabilities.

The paper's framing of "humans can generally perform a new language task from only a few
examples or from simple instructions" directly anticipated the agentic use case where
models assist with complex, multi-step tasks.

## Key Quotes

From the abstract: "scaling up language models greatly improves task-agnostic, few-shot
performance, sometimes even reaching competitiveness with prior state-of-the-art fine-tuning
approaches."

On in-context learning: "For all tasks, GPT-3 is applied without any gradient updates or
fine-tuning, with tasks and few-shot demonstrations specified purely via text interaction
with the model."

## Legacy

GPT-3 led directly to:
- **InstructGPT** (2022): GPT-3 fine-tuned with RLHF for instruction-following
- **ChatGPT** (November 2022): InstructGPT variant that brought LLMs to mainstream consciousness
- **GPT-4** (2023): Multimodal successor that pushed capabilities further

The paper's 31 authors include many who would go on to leadership positions across the AI
industry, including Dario Amodei (co-founder, Anthropic) and several other Anthropic founders.

## Citation Impact

As of 2025, the paper has been cited over 50,000 times, making it one of the most influential
AI papers ever published. It fundamentally shifted the field from "train specialized models
for each task" to "scale up general-purpose models and prompt them."
