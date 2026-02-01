---
bibkey: "anthropic2024claude3"
title: "The Claude 3 Model Family: Opus, Sonnet, Haiku"
authors: "Anthropic"
year: 2024
source_type: "model_card"
url: "https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf"
venue: "Anthropic Model Card (March 2024)"
status: "complete"
key_findings:
  - "Claude 3 family introduced three models in ascending capability: Haiku (fastest/cheapest), Sonnet (balanced), Opus (most capable)"
  - "Claude 3 Opus outperformed peers on most common AI benchmarks: MMLU (undergraduate knowledge), GPQA (graduate reasoning), GSM8K (math)"
  - "First multimodal Claude models with vision capabilities for processing photos, charts, graphs, and technical diagrams"
  - "Remains at AI Safety Level 2 (ASL-2) per Anthropic's Responsible Scaling Policy despite capability advances"
  - "Trained with Constitutional AI methodology and RLHF for helpful, harmless, honest alignment"
  - "200K token context window with near-perfect recall (99.4% for Opus on Needle in a Haystack task)"
  - "Red teaming evaluations concluded negligible potential for catastrophic risk at release"
sample_sentences: |
  In March 2024, Anthropic released the Claude 3 model family—Opus, Sonnet, and Haiku—offering
  tiered intelligence, speed, and cost tradeoffs for different application needs. Claude 3 Opus
  set new benchmarks across undergraduate knowledge (MMLU) and graduate reasoning (GPQA), while
  introducing multimodal vision capabilities and maintaining rigorous safety standards under
  Anthropic's Responsible Scaling Policy.
quotable:
  - "Claude 3 shows a more nuanced understanding of requests, recognize real harm, and refuse to answer harmless prompts much less often"
  - "Opus shows us the outer limits of what's possible with generative AI"
  - "Claude is trained to be a helpful, honest, and harmless assistant"
---
# The Claude 3 Model Family: Opus, Sonnet, Haiku

## Overview

On March 4, 2024, Anthropic released the Claude 3 model family, positioning it as a new
industry benchmark across a wide range of cognitive tasks. The family introduced a tiered
approach with three state-of-the-art models: Claude 3 Haiku (fast and cost-effective),
Claude 3 Sonnet (balanced performance and speed), and Claude 3 Opus (maximum intelligence).
This marked a significant evolution from Claude 2, bringing multimodal capabilities and
substantially improved performance across standard benchmarks.

## The Three-Model Tier System

### Claude 3 Opus ("Powerful")

The flagship model, Opus represents Anthropic's most intelligent offering:

- **Benchmark Performance**: Outperforms peers on most common AI benchmarks including
  undergraduate knowledge (MMLU), graduate reasoning (GPQA), and basic mathematics (GSM8K)
- **MMLU Score**: 90.5% (1-shot), 89.2% (0-shot)—highest among Claude 3 models
- **Context Handling**: 99.4% average recall on Needle in a Haystack evaluation,
  maintaining 98.3% even at 200K tokens
- **Pricing**: $15/$75 per million input/output tokens
- **Use Case**: Complex tasks requiring maximum intelligence—research, strategy, nuanced analysis

Notably, Opus demonstrated "remarkable ability to identify the synthetic nature" of evaluation
tasks, suggesting meta-cognitive capabilities that warranted caution about benchmark interpretation.

### Claude 3 Sonnet ("Hard-Working")

The balanced middle-tier model optimized for enterprise workloads:

- **Speed**: 2x faster than Claude 2/2.1 with higher intelligence
- **AI2D Score**: 89.2% (0-shot)—state-of-the-art for visual understanding
- **Pricing**: $3/$15 per million input/output tokens
- **Use Case**: High-volume enterprise tasks like knowledge retrieval, sales automation,
  data processing

Sonnet delivered strong performance at lower cost, engineered for "high endurance in
large-scale AI deployments."

### Claude 3 Haiku ("Fast")

The fastest and most cost-effective model in its intelligence category:

- **Speed**: Can process a ~10K token research paper with charts in under 3 seconds
- **Output**: 123.1 tokens per second, 0.71 second latency
- **Use Case**: Near-instant responsiveness for simple queries, chatbots, real-time applications

Haiku prioritized speed over maximum capability while maintaining solid performance,
"answering simple queries and requests with unmatched speed."

## Multimodal Vision Capabilities

A major advance for Claude 3 was the introduction of vision capabilities across all models,
enabling processing of:

- Photographs and natural images
- Charts, graphs, and data visualizations
- Technical diagrams and flowcharts
- Documents with mixed text and visual content

Anthropic noted that some enterprise customers "have up to 50% of their knowledge bases
encoded in various formats such as PDFs, flowcharts, or presentations"—making multimodal
understanding essential for practical deployment.

Vision evaluations showed strong performance:
- Claude 3 Sonnet: 89.2% on AI2D (science diagrams)
- Claude 3 Opus: 88.3% on AI2D
- Strong performance on MMMU (multimodal understanding) benchmarks

## Safety and Responsible Scaling

Claude 3 remained at AI Safety Level 2 (ASL-2) per Anthropic's Responsible Scaling Policy,
despite capability advances:

### Red Teaming and Evaluation

- Conducted comprehensive red teaming in line with White House commitments and 2023 US
  Executive Order requirements
- Evaluated for biological knowledge, cyber-related knowledge, and autonomous capabilities
- Concluded "negligible potential for catastrophic risk at this time"

### Constitutional AI and Alignment

Claude 3 continued Anthropic's Constitutional AI methodology:

- Explicitly specified rules and principles (based on sources like UN Declaration of
  Human Rights)
- Trained to be "helpful, honest, and harmless"
- RLHF fine-tuning for alignment with user intent

### Reduced Over-Refusals

A significant improvement: Claude 3 models showed "significantly less likely to refuse to
answer prompts that border on the system's guardrails than previous generations." The
models demonstrated "a more nuanced understanding of requests, recognize real harm, and
refuse to answer harmless prompts much less often."

### Improved Accuracy

Anthropic evaluated accuracy using "a large set of complex, factual questions that target
known weaknesses in current models," categorizing responses as:
- Correct answers
- Incorrect answers (hallucinations)
- Admissions of uncertainty

Claude 3 showed improvement in admitting uncertainty rather than hallucinating.

## Technical Details

### Architecture and Training

- Transformer-based architecture (specifics not disclosed)
- Knowledge cutoff: August 2023
- Training methodology: Constitutional AI + RLHF
- Available via: Claude.ai, Claude Pro, Anthropic API, Amazon Bedrock, Google Vertex AI

### Context Window

- 200K token context window at release
- Potential for larger contexts in future updates
- Near-perfect recall demonstrated across context lengths

### Bias Mitigation

Claude 3 showed reduced bias compared to previous models on the Bias Benchmark for
Question Answering (BBQ), with Anthropic committing to "advancing techniques that reduce
biases and promote greater neutrality."

## Election Preparedness (2024)

Given the global election cycle in 2024, Anthropic proactively prepared:

1. Developing policies around acceptable political/election use cases
2. Testing model responses to election misinformation and bias prompts
3. Working to ensure accurate, up-to-date voting information in select countries

## Relevance to Our Paper

Claude 3 is directly relevant to our "HPC in the Agentic Era" thesis for several reasons:

### 1. The Model We Actually Use

Claude 3 (and subsequent Claude 3.5 models) power the Warp Agent Mode we use to write
this very paper. Understanding its capabilities and limitations is essential context for
our methodology discussion.

### 2. Tiered Model Design for Agentic Systems

The Opus/Sonnet/Haiku tier system demonstrates the industry's understanding that different
tasks require different capability/cost tradeoffs—a pattern that informs how agentic
development environments route tasks to appropriate models.

### 3. Multimodal Capabilities

Vision understanding is crucial for agentic systems that need to interpret documentation,
diagrams, and visual feedback from development environments.

### 4. Safety in Autonomous Contexts

Anthropic's Responsible Scaling Policy and ASL-2 classification are directly relevant to
discussions about using AI agents for HPC tasks—understanding what safety evaluations
frontier models undergo helps contextualize appropriate use cases.

### 5. Context Window Scale

The 200K token context window (with high recall) enables the kind of whole-codebase
understanding that makes agentic coding assistance viable—a precondition for the
workflows we describe.

## Subsequent Evolution

Claude 3 was followed by rapid iteration:
- **June 2024**: Claude 3.5 Sonnet released, outperforming Opus on many benchmarks
- **October 2024**: Upgraded Claude 3.5 Sonnet with computer use capabilities
- **October 2024**: Claude 3.5 Haiku released

The 3.5 models demonstrated that the "mid-tier" Sonnet could exceed the flagship Opus's
capabilities at lower cost—a pattern of rapid improvement characteristic of the 2024
AI landscape.

## Citation

```bibtex
@techreport{anthropic2024claude3,
  title        = {The Claude 3 Model Family: Opus, Sonnet, Haiku},
  author       = {Anthropic},
  year         = {2024},
  month        = {March},
  institution  = {Anthropic},
  type         = {Model Card},
  url          = {https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf}
}
```
