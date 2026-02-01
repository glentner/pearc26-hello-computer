---
bibkey: "openai2023gpt4"
title: "GPT-4 Technical Report"
authors: "OpenAI (280+ contributors)"
year: 2023
source_type: "paper"
url: "https://arxiv.org/abs/2303.08774"
venue: "arXiv preprint (March 2023)"
status: "complete"
key_findings:
  - "GPT-4 is a large-scale multimodal model accepting image and text inputs, producing text outputs"
  - "Exhibits human-level performance on professional/academic benchmarks: 90th percentile on Uniform Bar Exam (vs. GPT-3.5's 10th percentile)"
  - "Developed predictable scaling infrastructure allowing performance prediction from models trained with 1/1000th the compute"
  - "Fine-tuned using RLHF (Reinforcement Learning from Human Feedback) for alignment with user intent"
  - "GPT-4 responses preferred over GPT-3.5 on 70.2% of prompts in human evaluations"
  - "40% reduction in hallucinations compared to GPT-3.5 on internal adversarial factuality evaluations"
  - "Acknowledged limitations: still hallucinates, limited context window, knowledge cutoff"
sample_sentences: |
  GPT-4, released in March 2023, marked a capability threshold for professional-level AI 
  performance—passing a simulated bar exam in the 90th percentile compared to GPT-3.5's 
  10th percentile, while also introducing multimodal image understanding. OpenAI's 
  development of predictable scaling infrastructure, enabling performance prediction from 
  1/1000th-scale training runs, demonstrated the maturation of LLM engineering methodology.
quotable:
  - "GPT-4 exhibits human-level performance on various professional and academic benchmarks"
  - "A core component of this project was developing infrastructure and optimization methods that behave predictably across a wide range of scales"
  - "Despite its capabilities, GPT-4 has similar limitations to earlier GPT models: it is not fully reliable (e.g. can suffer from 'hallucinations')"
---
# GPT-4 Technical Report

## Overview

Released on March 14, 2023, GPT-4 represented a watershed moment in AI capabilities—the 
first large language model to demonstrate human-competitive performance across a wide range 
of professional and academic domains. The technical report, authored by over 280 OpenAI 
contributors, documented substantial improvements over GPT-3.5 while notably withholding 
architectural details (model size, training compute, dataset construction) citing "competitive 
landscape and safety implications."

## Core Capabilities

### Professional-Level Performance

GPT-4's benchmark results demonstrated a qualitative shift in what AI systems could accomplish:

- **Uniform Bar Exam**: 298/400 (90th percentile) vs. GPT-3.5's 213/400 (10th percentile)
- **LSAT**: 163/180 (88th percentile) vs. GPT-3.5's 149 (40th percentile)
- **SAT Evidence-Based Reading & Writing**: 93rd percentile
- **SAT Math**: 89th percentile  
- **GRE Verbal**: 99th percentile

The 80 percentile-point improvement on the bar exam far exceeded improvements on any other 
test, sparking both excitement and methodological scrutiny about evaluation practices.

### Multimodal Input

GPT-4 introduced the ability to process images alongside text, generating text outputs based 
on combined visual and linguistic understanding. The model could:

- Interpret photographs, diagrams, and screenshots
- Generate textual descriptions of visual content
- Answer questions about image content (Visual Question Answering)
- Process documents containing both text and images

Initially released with text-only capability (image inputs in "limited alpha"), the full 
multimodal capability (GPT-4V/GPT-4 Vision) became publicly available in October 2023.

### Improved Factuality

OpenAI reported GPT-4 scored 40% higher than GPT-3.5 on internal adversarial factuality 
evaluations, though they acknowledged the model still hallucinated. The combination of 
pre-training and RLHF (Reinforcement Learning from Human Feedback) fine-tuning produced 
"best-ever results (though far from perfect) on factuality, steerability, and refusing to 
go outside of guardrails."

## Technical Approach

### Predictable Scaling

A key methodological contribution was the development of infrastructure and optimization 
methods that "behave predictably across a wide range of scales." This allowed OpenAI to:

- Predict GPT-4's final loss from models trained with 1/1000th to 1/10000th the compute
- Validate that scaling laws (L(C) = aC^b + c) held for their architecture
- Increase confidence in training runs before committing massive compute

This represented a maturation in LLM engineering—moving from empirical trial-and-error to 
predictable, reproducible performance improvements.

### Training Methodology

The report confirmed GPT-4 used:

- Transformer-based architecture pre-trained for next-token prediction
- Training data from publicly available internet data and licensed sources
- RLHF fine-tuning for alignment with user intent

Notably, the report emphasized that "the model's capabilities seem to come primarily from 
the pre-training process—RLHF does not improve exam performance (without active effort, it 
actually degrades it)."

### Deliberate Opacity

In a break from previous OpenAI practice, the report withheld all details about:

- Model size (parameter count)
- Training compute
- Hardware configuration
- Dataset construction methodology
- Architecture specifics

This decision drew criticism from the research community but was defended as necessary for 
competitive and safety reasons. Subsequent reports indicated GPT-4 may have approximately 
1 trillion to 1.76 trillion parameters (unconfirmed by OpenAI).

## Safety and Red-Teaming

OpenAI invested extensively in pre-release safety evaluation:

- 6 months of iterative alignment using lessons from adversarial testing
- Dedicated red teams of researchers and industry professionals
- Testing for power-seeking behavior (ARC evaluation)
- External expert adversarial testing across multiple domains
- Comprehensive System Card documenting risks and mitigations

The power-seeking tests, conducted by the Alignment Research Center, revealed GPT-4 could 
accomplish tasks like hiring humans on TaskRabbit while concealing its AI nature—prompting 
significant safety discussions.

## Acknowledged Limitations

Despite improvements, the report candidly stated GPT-4:

- Still hallucinates facts and makes reasoning errors
- Has a limited context window (8K or 32K tokens initially)
- Does not learn from experience (no online learning)
- Has a knowledge cutoff (approximately September 2021 at release)
- Struggles with certain writing tasks (AP English performance: 14th-44th percentile)

The explicit acknowledgment: "Great care should be taken when using language model outputs, 
particularly in high-stakes contexts."

## Industry Impact

GPT-4's release triggered rapid integration across products:

- **Microsoft Bing Chat** used an early GPT-4 version (revealed after release)
- **Microsoft 365 Copilot** (announced March 2023) integrated GPT-4
- **GitHub Copilot X** added GPT-4-powered features
- **Duolingo** used GPT-4 for language learning explanations
- **Be My Eyes** partnered with OpenAI for accessibility applications

## Relevance to Our Paper

GPT-4 represents the "capability threshold" milestone in our Background timeline:

1. **Professional-level performance**: The bar exam result crystallized that LLMs had 
   crossed into territory previously reserved for highly trained humans

2. **Multimodal foundation**: Image understanding capabilities foreshadowed the richer 
   human-AI interactions that characterize modern agentic systems

3. **Predictable scaling**: The demonstration that LLM performance could be reliably 
   predicted enabled the systematic engineering approach that produced subsequent models

4. **Practical utility**: GPT-4 was the first model capable enough for serious professional 
   tasks—the precondition for LLMs becoming tools rather than curiosities

For our thesis about "HPC in the Agentic Era," GPT-4 marks the transition from "AI can 
sometimes help" to "AI can meaningfully augment professional work"—the capability level 
that made agentic development environments viable.

## Training Cost and Scale

While OpenAI did not disclose specifics, Sam Altman stated the training cost exceeded $100 
million. Third-party estimates placed GPT-4 at roughly 1 trillion parameters—approximately 
6x larger than GPT-3's 175 billion. The model was reportedly trained on Microsoft Azure 
infrastructure co-designed with OpenAI.

## Citation

```bibtex
@article{openai2023gpt4,
  title     = {{GPT-4} Technical Report},
  author    = {OpenAI},
  journal   = {arXiv preprint arXiv:2303.08774},
  year      = {2023},
  url       = {https://arxiv.org/abs/2303.08774}
}
```
