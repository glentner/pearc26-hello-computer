# MCP Deployment Architecture

Notes on the 3-mode deployment configuration for RCAC-MCP and Globus-MCP servers.

## The Problem

Agentic environments (Warp, Cursor, VS Code + Copilot, etc.) need to connect to MCP servers. The question: where does the server run, and how does it authenticate/delegate?

## Three Deployment Modes

### 1. Local STDIO Mode (Recommended for Most Users)

```
[User's Machine]
    └── Agentic IDE (Warp, Cursor, etc.)
        └── MCP Server (local process, stdio)
            └── SSH Bridge → [HPC Cluster]
                            └── Tool execution via SSH
```

**Characteristics:**
- Server runs locally as a subprocess of the IDE
- Communication via stdin/stdout (stdio transport)
- Relies on user's existing SSH config and keys
- No additional authentication layer needed
- Tools execute remotely via SSH commands

**For Globus:**
- Same pattern: local server, local `globus login`
- Picks up existing Globus CLI credentials
- No hosted service needed

**Why this is likely the common pattern:**
- Zero infrastructure for HPC centers to maintain
- Users already have SSH keys configured
- Matches mental model of "AI assistant on my laptop talks to cluster"
- Privacy: sensitive operations stay on user's machine

### 2. Hosted Service with JWT/OIDC Auth

```
[User's Machine]                    [HPC Center Infrastructure]
    └── Agentic IDE ──HTTP/SSE──→ MCP Server (shared service)
                                      └── JWT/OIDC validation
                                      └── Tool execution (local shell)
```

**Characteristics:**
- Centrally hosted MCP server
- Authentication via JWT tokens or OIDC (CILogon, Keycloak, etc.)
- Server runs with elevated access, executes on behalf of users
- Requires infrastructure investment

**When this makes sense:**
- Web-based interfaces (no local IDE)
- Environments where SSH isn't available
- Centralized logging/auditing requirements

### 3. Hosted Service with Sudo/Identity Delegation

```
[User's Machine]                    [HPC Center Infrastructure]
    └── Agentic IDE ──HTTP/SSE──→ MCP Server (shared service)
                                      └── Identity mapping
                                      └── sudo -u $USER or setuid
                                      └── Tool execution as user
```

**Characteristics:**
- Like mode 2, but server delegates to actual user identity
- Requires careful security design
- Identity file maps authenticated identity → local username

**When this makes sense:**
- Need centralized service but also user-level isolation
- Compliance requirements around identity

## Design Philosophy

The ecosystem is still evolving. Our approach:

1. **Build all three modes** - let the community discover preferences
2. **Default to local/stdio** - lowest friction, most secure
3. **Document trade-offs** - let HPC centers make informed choices

## Implications for Paper

This is worth discussing in the Approach section because:
- Shows thoughtful security consideration
- Demonstrates understanding of HPC authentication landscape
- Acknowledges ecosystem uncertainty with flexible design
- The local-first approach aligns with "Mostly Harmless" philosophy

## Code References

- RCAC-MCP: `/Users/geoffrey/Software/github.com/purduercac/rcac-mcp/`
- Globus-MCP: (path TBD)

## Key Insight for Paper

> The question isn't just "can AI manage HPC resources?" but "where should that capability live?" Our 3-mode architecture reflects uncertainty about where the ecosystem will land, while betting that local-first (stdio + SSH bridge) will be the common case—it's the pattern that respects existing authentication infrastructure and keeps sensitive operations on the user's machine.
