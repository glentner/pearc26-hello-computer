---
bibkey: "vaswani2017attention"
title: "Attention Is All You Need"
authors: "Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, Illia Polosukhin"
year: 2017
source_type: "paper"
url: "https://arxiv.org/abs/1706.03762"
venue: "NeurIPS 2017 (NIPS'17)"
status: "complete"
key_findings:
  - "Introduced the Transformer architecture based solely on attention mechanisms, eliminating recurrence and convolutions"
  - "Self-attention enables parallel processing of all tokens simultaneously, unlike sequential RNNs"
  - "Multi-head attention allows the model to jointly attend to information from different representation subspaces"
  - "Achieved state-of-the-art on machine translation (41.8 BLEU English-French) with dramatically reduced training cost"
  - "Training time: 3.5 days on 8 GPUs vs. weeks for prior SOTA models"
sample_sentences: |
  The Transformer architecture, introduced by Vaswani et al. (2017), replaced recurrent and
  convolutional layers with pure attention mechanisms, enabling unprecedented parallelization
  during training. This architectural innovation became the foundation for all subsequent
  large language models, with the paper accumulating over 173,000 citations by 2025.
---

# Attention Is All You Need

## Overview

Published in June 2017 at NeurIPS (then NIPS), "Attention Is All You Need" introduced the
Transformer architecture—arguably the most influential machine learning paper of the decade.
The eight equal-contribution authors, all working at Google at the time, proposed replacing
the dominant sequence-to-sequence models (based on RNNs and CNNs) with a simpler architecture
built entirely on attention mechanisms.

## The Problem Being Solved

Prior to the Transformer, sequence transduction models (e.g., machine translation) relied on
encoder-decoder architectures using recurrent neural networks (RNNs) or convolutional neural
networks (CNNs). While the best models incorporated attention mechanisms to connect encoder
and decoder, they retained recurrent layers that processed tokens sequentially. This
sequential nature created two fundamental problems:

1. **Parallelization barrier**: RNNs process one token at a time, preventing efficient use
   of modern parallel hardware (GPUs/TPUs)
2. **Long-range dependencies**: The number of operations required to relate distant positions
   grew linearly (ConvS2S) or logarithmically (ByteNet), making it difficult to learn
   relationships between far-apart tokens

## The Transformer Innovation

The Transformer's key insight: attention mechanisms alone are sufficient for capturing
dependencies, and removing recurrence unlocks massive parallelization. The architecture
introduced several key components:

### Self-Attention

Self-attention (intra-attention) relates different positions within a single sequence to
compute representations. Unlike RNNs, self-attention connects any two positions with a
constant number of operations, regardless of distance.

### Scaled Dot-Product Attention

The attention function is computed as:

```
Attention(Q, K, V) = softmax(QK^T / √d_k) V
```

Where queries (Q), keys (K), and values (V) are linear projections of the input. The scaling
factor √d_k prevents the dot products from growing too large for effective softmax gradients.

### Multi-Head Attention

Rather than a single attention function, the model uses multiple parallel attention "heads,"
each with learned linear projections to different subspaces. This allows the model to
"jointly attend to information from different representation subspaces at different
positions." The paper used 8 heads in the base model.

### Position Encodings

Since the architecture has no recurrence or convolution, it has no inherent notion of token
order. The solution: add sinusoidal position encodings to the input embeddings. These
encodings use sine and cosine functions of different frequencies, allowing the model to
generalize to sequence lengths longer than those seen during training.

### Encoder-Decoder Structure

The full Transformer consists of:
- **Encoder**: 6 identical layers, each with multi-head self-attention and feed-forward sublayers
- **Decoder**: 6 identical layers, adding cross-attention to encoder outputs

Each sublayer uses residual connections and layer normalization.

## Results and Impact

### Machine Translation Performance

On WMT 2014 benchmarks:
- **English-to-German**: 28.4 BLEU (>2 BLEU improvement over prior best, including ensembles)
- **English-to-French**: 41.8 BLEU (new single-model SOTA)

### Training Efficiency

The "big" Transformer model trained in 3.5 days on 8 P100 GPUs—a fraction of the compute
required by prior state-of-the-art models. The estimated training cost was ~0.089
petaFLOP/s-days for the base model.

### Generalization

The authors demonstrated the architecture's generality by successfully applying it to
English constituency parsing, achieving strong results with both large and limited training
data. This hinted at the Transformer's potential as a general-purpose architecture beyond
machine translation.

## Why This Paper Matters for Our Paper

The Transformer is the architectural foundation for everything that followed in the LLM
revolution. Without this paper:

- GPT wouldn't exist (decoder-only Transformer)
- BERT wouldn't exist (encoder-only Transformer)
- No GPT-3, GPT-4, Claude, Gemini, or any modern LLM

The key insight for our "HPC in the Agentic Era" thesis: **the Transformer's parallelizability
is what made scaling possible**. RNNs couldn't effectively use thousands of GPUs; Transformers
can. This architectural choice directly enabled the scale-up from millions to trillions of
parameters that characterizes the current AI boom.

## Citation Statistics

As of 2025, the paper has been cited over 173,000 times, placing it among the top ten
most-cited papers of the 21st century. All eight authors have since left Google to found
startups or join other companies, underscoring the paper's transformative impact on the
field and industry.

## Trivia

- The paper's title is a reference to The Beatles' song "All You Need Is Love"
- The name "Transformer" was chosen by Jakob Uszkoreit simply because he liked how it sounded
- As early as spring 2017, before the preprint was published, the team experimented with
  decoder-only variants to generate Wikipedia articles—foreshadowing GPT
