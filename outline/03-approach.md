---
status: draft
target_words: 500
actual_words: ~460
---

# Approach / Our Work

## Key Points
- RCAC's multi-pronged strategy for supporting agentic AI in HPC
- System-wide configurations and agent prompts
- MCP server development (RCAC-MCP, Globus-MCP)
- User documentation and guidance
- This paper itself as an example of the workflow

## Notes
- MCP/TRON joke sets up "End of Line" conclusion
- See `notes/mcp-deployment-architecture.md` for detailed 3-mode architecture
- Key insight: "Where should the capability live?"

## Draft

Our approach at RCAC combines three complementary strategies: system-wide agent
configurations, purpose-built MCP servers, and user documentation that acknowledges
the reality of agentic tool adoption.

### System-Wide Configurations

Modern agentic tools (Warp, Cursor, Claude Code) look for rules files in well-known
locations. We deploy cluster-wide configurations through an `/etc/agents.d` directory
hierarchy, injecting HPC-specific context: which commands to use for quota checks
(`myquota`) and interactive sessions (`sinteractive`), how to load software via
environment modules, and which filesystems serve which purposes. These configurations
also encode prohibitions: don't run computationally intensive work on login nodes,
don't store sensitive data in world-readable locations, don't submit jobs without time
limits. The agent absorbs the cluster's policies before the user asks their first
question.

### MCP Servers

We developed MCP servers (the Model Context Protocol, not the Master Control Program,
though the naming coincidence feels appropriate). RCAC-MCP exposes Slurm operations
(job submission, queue queries, resource monitoring), filesystem navigation, and
cluster-specific tools like `myquota` and `jobinfo`. Globus-MCP provides agentic data
transfers between storage endpoints. Both are publicly available on GitHub.

Both servers implement a local-first architecture (Figure 1). The MCP server runs as
a subprocess of the user's IDE, communicating via stdin/stdout. Commands execute
remotely through the user's existing SSH configuration: no new credentials, no hosted
infrastructure, no additional attack surface. If you can SSH to the cluster, your
agent can too. For environments requiring centralized control, we also support hosted
deployment with JWT/OIDC authentication and identity delegation.

### Documentation and Guidance

Perhaps most importantly, we updated our user documentation to address agentic tools
directly. We don't pretend they don't exist or discourage their use. We explain what
they can and cannot do, how to verify their suggestions, and how to report issues when
AI-generated commands go wrong. We treat agentic AI as we would any other tool in the
HPC ecosystem: powerful, useful, and requiring appropriate guidance.

## Figures

### Figure 1: Local STDIO Mode with SSH Bridge

```
┌───────────────────────────────────────────────────────────────────────────┐
│  USER'S WORKSTATION                                                       │
│                                                                           │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │  Agentic Development Environment (Warp, Cursor, VS Code + Copilot)  │  │
│  │                                                                     │  │
│  │    ┌───────────────────┐         ┌───────────────────┐              │  │
│  │    │   LLM Backend     │◄───────►│   MCP Client      │              │  │
│  │    │   (Claude, etc.)  │         │                   │              │  │
│  │    └───────────────────┘         └─────────┬─────────┘              │  │
│  │                                            │ stdio                  │  │
│  └────────────────────────────────────────────┼────────────────────────┘  │
│                                               │                           │
│  ┌────────────────────────────────────────────▼────────────────────────┐  │
│  │  MCP Server (rcac-mcp / globus-mcp)                                 │  │
│  │  • Runs as local subprocess          • Uses ~/.ssh/config           │  │
│  │  • Zero authentication overhead      • Executes tools via SSH       │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                               │                           │
└───────────────────────────────────────────────┼───────────────────────────┘
                                                │ SSH
                                                ▼
┌───────────────────────────────────────────────────────────────────────────┐
│  HPC CLUSTER                                                              │
│                                                                           │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │  Login Node                                                         │  │
│  │                                                                     │  │
│  │    ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                │  │
│  │    │   Slurm     │  │   LMOD      │  │  Filesystem │                │  │
│  │    │   Commands  │  │   Modules   │  │  Operations │                │  │
│  │    └─────────────┘  └─────────────┘  └─────────────┘                │  │
│  │                                                                     │  │
│  │    ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                │  │
│  │    │   myquota   │  │   jobinfo   │  │   sfeatures │                │  │
│  │    │             │  │             │  │             │                │  │
│  │    └─────────────┘  └─────────────┘  └─────────────┘                │  │
│  │                                                                     │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                           │
└───────────────────────────────────────────────────────────────────────────┘
```

The local-first pattern: MCP server runs on the user's machine, commands execute
remotely via SSH. No hosted infrastructure required. User's existing SSH keys and
config provide authentication.
