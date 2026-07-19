---
slug: hello-computer
title: "Hello Computer: HPC in the Agentic Era"
venue: PEARC26
template: "acmart sigconf"
macro_phase: released
base: main
branch: draft
last_updated: 2026-07-14
sections:
  - {id: 00-abstract, status: integrated, satisfies: [C1, C2, C4, C5], target_words: 150, order: 6}
  - {id: 01-introduction, status: integrated, satisfies: [C1, C2, C3], target_words: 400, order: 4}
  - {id: 02-background, status: integrated, satisfies: [], target_words: 300, order: 1}
  - {id: 03-approach, status: integrated, satisfies: [C4], target_words: 500, order: 2}
  - {id: 04-discussion, status: integrated, satisfies: [C3], target_words: 600, order: 3}
  - {id: 05-conclusion, status: integrated, satisfies: [C2, C5], target_words: 200, order: 5}
  - {id: 06-acks, status: integrated, satisfies: [], target_words: 80, order: 7}
claims:
  - {id: C1, status: supported, satisfied_by: [00-abstract, 01-introduction], evidence: [openai2022chatgpt, yao2023react]}
  - {id: C2, status: supported, satisfied_by: [00-abstract, 01-introduction, 05-conclusion], evidence: [deelman2025hpc, whitehouse2025genesis]}
  - {id: C3, status: supported, satisfied_by: [01-introduction, 04-discussion], evidence: [godoy2024llm]}
  - {id: C4, status: supported, satisfied_by: [00-abstract, 03-approach], evidence: [anthropic2024mcp, anthropic2025aaif]}
  - {id: C5, status: supported, satisfied_by: [00-abstract, 05-conclusion], evidence: [warp2024agentmode]}
review: {cycle: 2, verdict: approved}
---

# Hello Computer: HPC in the Agentic Era — Paper Contract

> **This is the paper's contract and finite-state machine**, the GOAL analog of the
> `.agents/factory` toolkit. The **frontmatter above** is the machine-owned FSM
> (read it with `python3 .agents/factory/bin/paper_status.py`; mutate it with
> `set_status.py` — never hand-edit the frontmatter). **This body** holds the
> human-editable contract: thesis, contribution claims, non-goals, and the
> section→LaTeX anchor map. The body is preserved verbatim by the FSM scripts.
>
> This file was **retrofitted** onto a finished, shipped paper (v1.0.1) as the
> proof-of-concept worked example. All sections are `integrated` and the
> `macro_phase` is `released`; a fresh paper would begin at `scoped` (see
> `/paper-start`).

## Thesis

For HPC facilitators, the arrival of agentic AI is not a threat to be managed but a
shift to be led. **Proactive engagement — not prohibition — is the path forward.**
This paper reports Purdue RCAC's early practice (system-wide agent configurations,
purpose-built MCP servers, and honest user documentation) and demonstrates the thesis
in its own construction: every word was produced through a documented agent-first
workflow.

## Contribution Claims

Stable IDs (`C1`, `C2`, …) that anchor the claim → section → evidence spine. Hybrid
policy (see `.agents/factory/claims.md`): only the headline abstract/intro claims get
C-IDs; the rest of the argument stays informal `## Key Points` in the outline.

- **C1** — HPC centers face a new *category* of user need: researchers now expect
  agentic tools to be supported, not merely permitted.
- **C2** — Proactive engagement, not prohibition, is the path forward for facilitators
  who wish to remain relevant in the agentic era. *(the thesis)*
- **C3** — Agentic AI in HPC is "mostly harmless": frontier systems follow instructions
  more reliably than many users do, so the greater risk is disengagement, not the tools.
- **C4** — A concrete, reproducible facilitation approach exists today: system-wide
  `/etc/agents.d` configurations, purpose-built MCP servers (RCAC-MCP, Globus-MCP), and
  documentation that verifies rather than forbids.
- **C5** — The agent-first authoring workflow is itself a contribution: a public,
  commit-by-commit meta-demonstration of the practice the paper advocates.

## Non-goals

- Not a benchmark or quantitative evaluation of any model's HPC performance.
- Not a security audit of MCP or agentic tooling; confinement is discussed, not proven.
- Not a general survey of agentic AI; scope is the *facilitator's* practice at one center.
- Not prescriptive policy for other centers; this is a practitioner's report and invitation.

## Section → LaTeX anchor map

Machine-read by `paper_status.py` (which verifies each anchor still occurs in
`manuscript.tex`) and by `/paper-draft` (which uses it as the heading map for
outline→LaTeX integration). **Seeded from the live `manuscript.tex`, never from the
deprecated `latex-integration-*` skills.** One `id | \anchor` per line. `00-abstract`
and `06-acks` are LaTeX *environments*, not `\section`s. `01`'s "Mostly Harmless"
subsection is commented out in the manuscript (its prose merged into the section), so
it is intentionally absent here. `04-discussion` maps to five subsection anchors.

```anchors
00-abstract | \begin{abstract}
01-introduction | \section{Shall We Play a Game?}
02-background | \section{Background}
03-approach | \section{Approach}
03-approach | \subsection{System-Wide Configurations}
03-approach | \subsection{MCP Servers}
03-approach | \subsection{Documentation and Guidance}
04-discussion | \section{Discussion}
04-discussion | \subsection{``I'm Sorry, Dave'' (User Support)}
04-discussion | \subsection{``Tea, Earl Grey, Hot'' (Context Engineering)}
04-discussion | \subsection{``I Know Kung Fu'' (User Expectations)}
04-discussion | \subsection{``The Answer is 42'' (AI Outcomes)}
04-discussion | \subsection{``Don't Cross the Streams'' (Caution)}
05-conclusion | \section{End of Line}
06-acks | \begin{acks}
```

## Venue & build notes

- **Venue:** ACM PEARC '26 extended abstract, hard **4-page** limit (`make check`).
- **Template:** `acmart` — currently `\documentclass[sigconf]` (camera-ready); rights
  `\setcopyright{cc}` / `\setcctype{by}` (CC-BY); AI use disclosed in `\begin{acks}`.
- **Source of truth:** `outline/0N-*.md` `## Draft` blocks → integrated into the single
  `manuscript.tex` by `/paper-draft`. `references.bib` holds all 13 sources.
- **Known flag:** the `\begin{acks}` AI-use disclosure still names "Warp / Claude Opus
  4.6/4.7"; under the Claude Code harness this is stale content for the authors to update
  (surfaced by `check_paper.py`; not auto-edited).
