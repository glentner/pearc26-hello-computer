---
bibkey: "godoy2024llm"
title: "Large Language Model Evaluation for High-Performance Computing Software Development"
authors: "William F. Godoy, Pedro Valero-Lara, Keita Teranishi, Prasanna Balaprakash, Jeffrey S. Vetter"
year: 2024
source_type: "paper"
url: "https://doi.org/10.1002/cpe.8269"
journal: "Concurrency and Computation: Practice and Experience"
volume: 36
issue: 26
doi: "10.1002/cpe.8269"
affiliation: "Oak Ridge National Laboratory"
status: "complete"
key_findings:
  - "LLM correctness correlates with programming model maturity—OpenMP/CUDA score high, HIP lags behind"
  - "Fortran performs well due to legacy HPC code abundance in training data"
  - "No experiments achieved perfect correctness, illustrating stochastic nature of current LLMs"
  - "Adding language keywords to prompts improves results for Fortran and Python"
  - "First systematic evaluation of LLM code generation specifically for HPC parallel programming models"
sample_sentences: |
  Prior work from Oak Ridge National Laboratory systematically evaluated GPT-3/Codex 
  capabilities for HPC kernel generation across C++, Fortran, Python, and Julia, finding 
  that correctness correlated with programming model maturity—mature frameworks like 
  OpenMP and CUDA performed well while newer options like HIP showed gaps. This work 
  established that while LLMs show promise for HPC code assistance, their training 
  data underrepresents the specialized parallel programming patterns common in 
  scientific computing.
---

# Large Language Model Evaluation for High-Performance Computing Software Development

This paper from Oak Ridge National Laboratory (ORNL) represents one of the first systematic evaluations of large language model capabilities specifically targeting high-performance computing code generation. The work builds on an earlier conference paper (ICPP Workshops 2023) and expands it into a comprehensive journal article published in Concurrency and Computation: Practice and Experience in September 2024.

## Research Scope

The authors evaluated AI-assisted code generation using GPT-3 (via GitHub Copilot powered by OpenAI Codex) for two primary tasks:
1. **Code generation**: Creating parallel implementations from simple prompts
2. **Auto-parallelization**: Converting serial code to parallel using ChatGPT interactively

### Kernels Tested
Six fundamental numerical kernels common in HPC:
- AXPY (vector addition with scaling)
- GEMV (general matrix-vector multiplication)
- GEMM (general matrix-matrix multiplication)
- SpMV (sparse matrix-vector multiplication)
- Jacobi Stencil
- Conjugate Gradient (CG)

### Languages and Programming Models
Four languages with multiple parallel programming models each:
- **C++**: OpenMP (including offload), OpenACC, Kokkos, SYCL, CUDA, HIP
- **Fortran**: OpenMP (including offload), OpenACC
- **Python**: numpy, Numba, cuPy, pyCUDA
- **Julia**: Threads, CUDA.jl, AMDGPU.jl, KernelAbstractions.jl

## Methodology

The evaluation used GitHub Copilot in Visual Studio Code (as of April 2023) with a structured prompt pattern: `<kernel> + <programming model> + <optional hints>`. For each combination, they obtained multiple suggestions and developed a proficiency metric based on the initial 10 suggestions to quantify correctness.

For auto-parallelization, they used ChatGPT interactively with dialogue-style prompts, including simple prompt engineering follow-ups—mimicking how a developer might actually use these tools.

## Key Results

### Programming Model Maturity Matters
Results for C++ showed strong correlation between output correctness and the adoption/maturity of programming models:
- **High scores**: OpenMP and CUDA (well-established, abundant training data)
- **Poor scores**: HIP (newer, less training data available)
- **Intermediate**: Kokkos, SYCL, OpenACC

### Language-Specific Findings

**Fortran**: Surprisingly good results across kernels, including complex ones like CG and Jacobi. The authors attribute this to the abundance of legacy HPC Fortran code available for training—"it is not surprising that Copilot can obtain correct kernel implementations with higher complexity kernels."

**Python**: Benefits from being the most-used general-purpose language in AI/ML. Adding language keywords (like `def` for function definitions) improved results.

**Julia**: Acceptable performance for Threads and CUDA.jl programming models, though less data availability compared to Python.

### Stochastic Nature
A critical observation: "none of the experiments reached a perfect score of 1, which illustrates the stochastic status of the current LLM when generating code." This highlights that LLM-generated code requires human review and cannot be blindly trusted.

### AXPY Baseline
The simplest kernel (AXPY) consistently achieved the best results across all languages, providing a baseline for LLM code generation capability.

## Significance for HPC

The paper identifies a fundamental challenge: LLMs are trained predominantly on general-purpose software, with far fewer HPC-specific codes in training corpora. This means:
- Parallel performance considerations are not well-captured
- Portability across architectures is not reflected
- Reproducibility of scientific results is not a training objective

The authors conclude: "Overall, understanding the convergence of LLMs, AI, and HPC is crucial due to its rapidly evolving nature and how it is redefining human-computer interactions."

## Context and Follow-up Work

This paper is part of a broader research program at ORNL examining AI for HPC software development. Related works include:
- Comparison of Llama-2 and GPT-3 for HPC kernel generation (Valero-Lara et al. 2023)
- HPC-Coder for modeling parallel programs (Nichols et al. 2024)
- ChatBLAS: AI-generated portable BLAS library (Valero-Lara et al. 2024)
- DOE ASCR-funded projects Ellora and Durban for advancing HPC software via AI

The research team continues to be active, with work extending to ChatMPI for distributed computing and ChatHPC for building foundations of trustworthy AI-assisted HPC ecosystems.

## Relevance to Our Paper

This reference is essential for our Background section as it:
1. Represents the most rigorous prior work specifically on LLM+HPC code generation
2. Comes from DOE national laboratory researchers (credibility for HPC community)
3. Identifies the training data gap that limits current LLM effectiveness for HPC
4. Provides quantitative evidence of both capabilities and limitations
5. Sets the stage for discussing how agentic tools might address these limitations through iterative refinement rather than single-shot generation
