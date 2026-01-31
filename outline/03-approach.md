---
status: draft
target_words: 500
---

# Approach / Our Work

## Key Points
- RCAC's multi-pronged strategy for supporting agentic AI in HPC
- System-wide configurations and agent prompts
- MCP server development (RCAC-MCP, Globus-MCP)
- User documentation and guidance
- This paper itself as an example of the workflow

## RCAC Initiatives

### 1. System-Wide Agent Configurations
- Where: cluster-wide dotfiles, module system integration
- What: Rules files that tools like Gemini/Claude pick up automatically
- Examples:
  - "Do not do X" prohibitions (security, resource abuse)
  - "Use the `myquota` command" tips (HPC-specific guidance)
  - Cluster-specific context (scheduler, filesystems, policies)

### 2. RCAC-MCP Server
- Purpose: Let agents manage Slurm jobs and cluster operations
- Capabilities:
  - Submit/monitor/cancel jobs
  - Query queue status
  - Check quotas and allocations
  - Basic file operations within policy
- Architecture notes: Python, FastMCP framework

### 3. Globus-MCP Server
- Purpose: Agentic data transfer management
- Capabilities:
  - Initiate transfers between endpoints
  - Monitor transfer status
  - Manage collections and permissions
- Integration with RCAC authentication

### 4. User Documentation
- Updated RCAC docs with AI guidance
- Best practices for using agents on clusters
- Security considerations and policies

## Notes
- This is where the MCP/TRON joke goes (see snippets/mcp-joke.md)
- Could include a small code snippet or architecture diagram
- Emphasize: we're not just allowing AI—we're actively enabling it well

## Meta-Point
- This very paper was written using the tools we describe
- Warp + Claude 4.5 Opus as the development environment
- Dogfooding our own approach

## Draft

[To be written]
