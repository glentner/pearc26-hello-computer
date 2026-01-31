---
timestamp: "2026-01-31T22:08:00Z"
session_type: "documentation"
summary: "Created tips/ folder, documented Warp SQLite discovery, updated rules for mandatory verbatim inputs"
user_input: |
  Yes, before we run out of our context window, can you make note of this finding and maybe start a tips/ folder where we can store our discoveries and recommendations for working with agentic tools (in this case Warp) as markdown files. I also want to update our AGENTS.md and rules/ to make note of our more aggressive stance on storing verbatim inputs for every interaction from here on out. Also don't forget to add another logs/ entry and commit on this very interaction! (LOL)
files_modified:
  - tips/warp-conversation-history.md
  - AGENTS.md
  - rules/session_logs.md
  - logs/2026-01-31T22-08-00.md
---

# Session Log

## Context

This session followed immediately after discovering that Warp stores agent conversation inputs in a SQLite database on macOS. The discovery was made while trying to backfill verbatim user inputs for earlier session logs where we had only captured summaries.

## Agent Actions

1. Created `tips/` directory and `tips/warp-conversation-history.md` documenting:
   - Database location on macOS
   - Schema of `ai_queries` table
   - SQL and Python snippets for extracting verbatim inputs
   - Caveats (gaps in data, undocumented format)
   - Recommendation to use proactive logging rather than relying on recovery

2. Updated `AGENTS.md`:
   - Added `tips/` to repository structure listing
   - Added link to tips directory in Agent Workflow Rules section
   - Added emphasis on capturing verbatim `user_input` in Quick Reference

3. Updated `rules/session_logs.md`:
   - Made `user_input` a **required** field (moved from optional)
   - Updated User Input Section guidelines to emphasize verbatim capture
   - Added guidance for `user_input_note` when verbatim unavailable

4. Created this session log with verbatim input captured

## Outcome

The project now has:
- A `tips/` directory for documenting discoveries about agentic workflows
- Documented the Warp SQLite database finding for future reference
- Updated rules requiring verbatim input capture going forward

This discovery is also relevant content for the paper itself—dogfooding the agentic workflow and learning from the experience.
