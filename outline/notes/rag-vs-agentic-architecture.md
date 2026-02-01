---
title: "RAG vs Agentic Architecture: A Paradigm Shift"
created: "2026-02-01T01:56:00Z"
tags:
  - architecture
  - rag
  - mcp
  - acp
  - frontier-models
  - genai-studio
relates_to:
  - outline/02-background.md
  - outline/03-approach.md
  - outline/notes/mcp-deployment-architecture.md
status: "draft"
---

# RAG vs Agentic Architecture: A Paradigm Shift

> I'm not sure the right approach at describing our approach here and the ways that agentic research workflows differ from mere "RAG" models. We've spent the last 18 months deploying, supporting, and innovating on a RAG-based GenAI service "GenAI Studio" which is merely Open WebUI backed by our on-prem scale-out infrastructure. In that paradigm researchers are deploying mostly open-source foundation models (e.g., Llama 4) plus some knowledge base that we host - all exposed as an API to have chats with your knowledge base. This already feels antiquated. We should properly articulate the technical distinction with the way models like Claude 4.5 and Gemini 3 Pro are able to self-RAG on the fly as they work, in particular how that relates to MCP toolkits. We don't bother bundling knowledge bases as distinct models any more, we expose them as capabilities that large frontier models can use as primary agents who can now use ACP (Agent Context Protocol) to delegate with sub-agents.

## Commentary

This observation identifies a critical architectural evolution that the paper must articulate clearly. The shift from RAG to agentic architectures isn't merely incremental—it represents a fundamental change in how knowledge and capability are composed with language models.

### The Traditional RAG Paradigm

The GenAI Studio model represents the state-of-the-art circa 2023-2024:

```
[User] → [Open WebUI] → [Foundation Model (Llama 4)]
                              ↓
                        [Vector Store]
                        [Knowledge Base]
                              ↓
                        [Retrieved Context]
                              ↓
                        [Generated Response]
```

**Characteristics:**
- Knowledge is pre-indexed into vector embeddings
- Retrieval happens *before* generation (retrieve-then-read)
- The model is passive—it receives retrieved context, doesn't seek it
- Each knowledge base is essentially a distinct "capability bundle"
- Scaling means deploying more model+KB pairs

This architecture served us well for domain-specific Q&A, but it has fundamental limitations:
1. The model can't decide *what* to retrieve or *when*
2. Knowledge bases are static snapshots
3. No ability to take actions or verify information
4. Each new capability requires infrastructure deployment

### The Agentic Paradigm Shift

Frontier models (Claude 4.5, Gemini 3 Pro, GPT-5) with tool use flip the architecture:

```
[User] → [Frontier Model as Primary Agent]
              ↓
         [Tool Selection & Invocation]
              ↓
    ┌─────────┼─────────┬─────────┐
    ↓         ↓         ↓         ↓
 [MCP:KB]  [MCP:Code] [MCP:Web] [ACP:Sub-Agent]
    ↓         ↓         ↓         ↓
    └─────────┴─────────┴─────────┘
              ↓
         [Synthesized Response]
```

**Key Distinctions:**
- The model is *active*—it decides when and what to retrieve
- "Self-RAG on the fly": retrieval is a tool call, not a pipeline stage
- Knowledge bases become MCP servers, not model accessories
- New capabilities are exposed via protocols, not infrastructure
- One frontier model can orchestrate many capability sources

### MCP as the Enabler

The Model Context Protocol transforms knowledge bases from monolithic deployments to composable services:

| RAG Model | MCP Model |
|-----------|-----------|
| KB bundled with specific model | KB exposed as tool any model can call |
| Retrieve-then-read pipeline | On-demand retrieval during reasoning |
| Static index at deployment time | Live queries against current data |
| One model ↔ one KB | Many models ↔ many KBs (M:N) |

This is why "GenAI Studio feels antiquated"—it's solving yesterday's composition problem with yesterday's architecture.

### ACP and Sub-Agent Delegation

The Agent Context Protocol (ACP) extends this further by allowing frontier models to delegate to specialized sub-agents. This creates a hierarchy:

1. **Primary Agent** (frontier model): Understands user intent, plans approach
2. **MCP Tools**: Provide specific capabilities (file access, search, APIs)
3. **ACP Sub-Agents**: Handle complex sub-tasks requiring their own reasoning

For HPC contexts, this might mean:
- Primary: Claude 4.5 understanding researcher's goal
- MCP: RCAC-MCP for cluster status, job submission
- ACP: Specialized agent for workflow optimization or data analysis

### Implications for the Paper

This distinction deserves prominent treatment, likely in Section 2 (Background) or Section 3 (Approach):

1. **Historical context**: Acknowledge RAG's contributions (it got us here)
2. **Technical distinction**: Self-RAG vs pipeline-RAG, active vs passive retrieval
3. **Architectural shift**: From bundled deployments to protocol-based composition
4. **HPC relevance**: Why MCP matters for research computing specifically
5. **Forward-looking**: ACP and the emergence of agent hierarchies

### Suggested Framing

Rather than positioning RAG as "wrong," frame it as an evolutionary step:

> Traditional RAG architectures pioneered the integration of domain knowledge with language models, but required tight coupling between models and knowledge sources. The emergence of standardized protocols (MCP, ACP) decouples these concerns, allowing frontier models to dynamically compose capabilities at runtime rather than deployment time.

### Open Questions

- How do we handle the transition? GenAI Studio users have invested in RAG workflows
- What's the right abstraction level for MCP servers? Per-KB? Per-domain? Per-capability?
- How does latency compare? RAG pre-retrieval vs MCP on-demand retrieval
- What role remains for smaller, specialized models in an agentic world?
- How do we explain this shift to researchers who just learned RAG terminology?
