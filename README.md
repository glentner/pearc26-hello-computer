# Hello Computer: HPC in the Agentic Era

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE_MIT)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE_CC-BY-4.0)

This repository is the replication package for a PEARC'26 extended abstract exploring the intersection of agentic AI tools and high-performance computing.

## About This Project

**"Hello Computer"** — a nod to *Star Trek IV: The Voyage Home* — examines what it means to work with AI agents in the context of HPC and scientific computing. The paper presents experiences from Purdue University's Rosen Center for Advanced Computing (RCAC) in deploying agentic tooling for both facilitators and users.

### The Meta-Layer

This repository is intentionally self-referential: **we are writing a paper about agentic development while using agentic tools to write the paper**. Every aspect of this project — from manuscript drafting to build system configuration to literature review — has been conducted in collaboration with AI agents (specifically, Warp's Agent Mode powered by Claude).

The `logs/` directory contains timestamped session logs documenting every human-agent interaction. The `rules/` directory captures the prompt engineering patterns we've developed. This isn't just a paper about agentic workflows — it's a living example of one.

### Educational Intent

We hope this repository serves as:

1. **A conversation starter** — What does productive human-AI collaboration look like for technical work?
2. **An educational resource** — How do you structure prompts, rules, and workflows for effective agentic development?
3. **A reproducible example** — Every commit, every log, every decision is preserved for others to study.

## Repository Structure

```
├── manuscript.tex      # LaTeX source (ACM acmart format)
├── references.bib      # Bibliography
├── Makefile            # Build system (latexmk-based)
├── outline/            # Markdown drafts and notes
│   ├── notes/          # Research notes and bibliography
│   │   └── refs/       # Individual reference summaries
│   └── snippets/       # Draft prose fragments
├── logs/               # Session logs (human-agent interactions)
├── plans/              # Planning documents
├── rules/              # Agent workflow rules and conventions
└── tips/               # Discoveries about agentic tools
```

## Building the Manuscript

Requires a modern TeX distribution (e.g., TeX Live 2024+).

```bash
make build      # Incremental build → build/manuscript.pdf
make release    # Clean build with versioned PDF (lentner-2026-{hash}.pdf)
make watch      # Continuous build with file watching
make clean      # Remove build artifacts
```

## Licensing

This repository uses a dual-license structure:

- **Code and Data** — [MIT License](LICENSE_MIT)
- **Manuscript Content** — [CC BY 4.0](LICENSE_CC-BY-4.0)

If the final paper is published with an exclusive ACM license, the CC BY license applies only to this Author's Accepted Manuscript (AAM) version.

## Citation

If you find this work useful, please cite:

```bibtex
@inproceedings{lentner2026hello,
  author    = {Lentner, Geoffrey and Ashish},
  title     = {Hello Computer: {HPC} in the Agentic Era},
  booktitle = {Practice and Experience in Advanced Research Computing (PEARC '26)},
  year      = {2026},
  month     = {July},
  location  = {Minneapolis, MN, USA},
  publisher = {Association for Computing Machinery},
  address   = {New York, NY, USA},
  doi       = {10.1145/nnnnnnn.nnnnnnn},
  note      = {Extended Abstract}
}
```

## Acknowledgments

This work was conducted using Warp's Agent Mode with Claude (Anthropic). Per ACM policy, we disclose that generative AI tools were used extensively in drafting, editing, and developing this manuscript and its supporting materials. The authors retain full responsibility for the content.

---

*"A keyboard. How quaint."* — Scotty, Star Trek IV
