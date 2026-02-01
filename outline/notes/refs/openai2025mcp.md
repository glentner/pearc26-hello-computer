---
bibkey: "openai2025mcp"
title: "OpenAI adopts rival Anthropic's standard for connecting AI models to data"
authors: "Kyle Wiggers"
year: 2025
source_type: "article"
url: "https://techcrunch.com/2025/03/26/openai-adopts-rival-anthropics-standard-for-connecting-ai-models-to-data/"
date: "March 26, 2025"
status: "complete"
key_findings:
  - "OpenAI CEO Sam Altman announced full MCP adoption across OpenAI products, including Agents SDK immediately and ChatGPT Desktop/Responses API coming soon"
  - "Signals industry consensus: OpenAI adopting a rival's standard demonstrates MCP has achieved critical mass as the de facto protocol for AI-tool connectivity"
  - "Within weeks, Google DeepMind followed (April 2025), with CEO Demis Hassabis calling MCP 'a good protocol rapidly becoming an open standard for the AI agentic era'"
  - "Anthropic's CPO Mike Krieger welcomed the move, noting MCP had become 'a thriving open standard with thousands of integrations'"
  - "Microsoft released Playwright MCP the same week, and the spec was upgraded with JSON-RPC batching and OAuth 2.1 authorization"
quotable_phrases:
  - "People love MCP and we are excited to add support across our products"
  - "a thriving open standard with thousands of integrations"
  - "a good protocol and it's rapidly becoming an open standard for the AI agentic era"
sample_sentences: |
  In March 2025, OpenAI announced adoption of Anthropic's Model Context Protocol across its products—a significant validation given their competitive relationship—with CEO Sam Altman noting simply, "People love MCP."
  Within weeks, Google DeepMind followed suit, cementing MCP's status as the industry-standard protocol for connecting AI models to external tools and data sources, transforming what began as Anthropic's open-source experiment into shared infrastructure.
---

# OpenAI Adopts MCP: Industry Consensus Emerges

## Overview

On March 26, 2025, OpenAI CEO Sam Altman announced via X (formerly Twitter) that OpenAI would adopt Anthropic's Model Context Protocol across its products. This announcement was significant not just for its technical implications, but for what it signaled about industry convergence: the ChatGPT developer embracing an open standard created by its "best-funded startup rival" demonstrated that MCP had achieved critical mass.

MCP support launched immediately in the OpenAI Agents SDK, with ChatGPT Desktop and Responses API integration promised "coming soon."

## The Announcement

Altman's post was characteristically brief: "People love MCP and we are excited to add support across our products. [It's] available today in the Agents SDK and support for [the] ChatGPT desktop app [and] Responses API [is] coming soon!"

The response from Anthropic was notably warm for a competitor announcement. Mike Krieger, Anthropic's Chief Product Officer, responded: "Excited to see the MCP love spread to OpenAI – welcome! MCP has [become a] thriving open standard with thousands of integrations and growing. LLMs are most useful when connecting to the data you already have and software you already use."

## Technical Details

OpenAI's adoption coincided with Anthropic releasing a new MCP specification version:

**New Features in the March 2025 Spec:**
- **JSON-RPC Batching**: Ability to package multiple LLM data requests into a single request, improving efficiency
- **Improved Notifications**: Enhanced mechanisms for MCP servers to send notifications to connected LLMs
- **OAuth 2.1 Authorization**: Upgraded authentication to the latest OAuth standard for secure connections

**Initial OpenAI MCP Support:**
- **Agents SDK**: Open-source toolkit for building AI agents (available immediately)
- **ChatGPT Desktop**: Consumer-facing application (coming soon at announcement)
- **Responses API**: Developer API for accessing OpenAI models (coming soon at announcement)

MCP enables LLMs to both retrieve data from external systems and perform actions in those systems. As TechCrunch's Kyle Wiggers explained: "An LLM optimized for coding tasks could use the protocol to run a configuration script on a cloud instance. An AI-powered marketing tool, meanwhile, can enter ad performance metrics into an analytics application."

## Industry Cascade

OpenAI's move triggered a rapid cascade of industry adoption:

**Two Weeks Later (April 2025):**
Google DeepMind CEO Demis Hassabis announced MCP support for Gemini models and SDK via X: "MCP is a good protocol and it's rapidly becoming an open standard for the AI agentic era. Look forward to developing it further with the MCP team and others in the industry."

**Concurrent Developments:**
- Microsoft released Playwright MCP, combining the protocol with their browser automation tool to let LLMs interact with webpages
- Development tool companies that had already adopted MCP (Block, Apollo, Replit, Codeium, Sourcegraph) saw validation of their early bets

## Why This Matters

### Competitive Dynamics
OpenAI adopting a competitor's standard was notable because:
1. OpenAI had created its own tool-calling approaches (function calling API, ChatGPT plugins framework)
2. The companies compete directly in the frontier model market
3. Anthropic explicitly designed MCP to be vendor-neutral

The decision represented pragmatism over not-invented-here syndrome. As one industry observer noted, MCP had achieved sufficient adoption that fighting the standard was more costly than joining it.

### Protocol vs. Proprietary
Prior to MCP, both OpenAI and Anthropic had similar but subtly different approaches to tool calls—the pattern where an AI generates a response indicating desire to invoke an external function with specific parameters. Each approach required vendor-specific implementation work.

MCP's success demonstrated market preference for open standards over proprietary alternatives, even when the standard was created by a competitor.

### Critical Mass Indicators
By March 2025, MCP had accumulated enough momentum to become inevitable:
- Thousands of MCP servers in production
- Major development tool companies already integrated
- Enterprise deployments at companies like Block
- Active open-source community building connectors

## Subsequent Evolution

The OpenAI adoption proved to be a harbinger of deeper integration:

**October 2025:** OpenAI rolled out full MCP support in ChatGPT, including "Developer Mode" with read/write connector capabilities.

**December 2025:** OpenAI became a co-founder of the Agentic AI Foundation (AAIF) under the Linux Foundation, alongside Anthropic and Block. OpenAI contributed AGENTS.md (a markdown specification for providing coding agents with project-specific instructions) while Anthropic donated MCP itself.

As Nick Cooper from OpenAI explained the foundation's goal: "We're just looking to drive to create this open, neutral space where we can get meaningful contributions from others, get feedback from the developer community and the user community, and really help build and refine all these protocols to be really quite meaningful."

## Significance for Our Paper

The March 2025 MCP adoption announcement marks a crucial milestone in the agentic infrastructure timeline. It demonstrates:

1. **Industry Consensus**: When competitors adopt shared standards, it signals the technology has matured beyond experimental into foundational infrastructure.

2. **Developer-Driven Standards**: MCP succeeded because developer adoption (thousands of servers, millions of SDK downloads) created market pressure that even competing vendors couldn't ignore.

3. **Ecosystem Over Vendor Lock-In**: The AI industry chose interoperability over proprietary moats, similar to how the web standardized on HTTP/HTML despite commercial competitors.

For HPC contexts, this matters because:
- MCP is now the standard protocol any AI coding assistant will use
- HPC centers adopting agentic tools benefit from this standardization
- Building MCP servers for HPC-specific tools (scheduler interfaces, documentation systems, data access) becomes a tractable path to AI integration

## References

- Primary: https://techcrunch.com/2025/03/26/openai-adopts-rival-anthropics-standard-for-connecting-ai-models-to-data/
- Google adoption: https://techcrunch.com/2025/04/09/google-says-itll-embrace-anthropics-standard-for-connecting-ai-models-to-data/
- SiliconANGLE coverage: https://siliconangle.com/2025/03/27/openai-adds-support-anthropics-mcp-llm-connectivity-protocol/
- Wikipedia: https://en.wikipedia.org/wiki/Model_Context_Protocol
