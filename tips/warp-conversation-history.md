# Recovering Warp Agent Conversation History

## Discovery

Warp stores agent conversation inputs in a SQLite database on macOS. This can be used to recover verbatim user inputs for audit trails, documentation, or when you forget to log something.

## Database Location

```
~/Library/Group Containers/2BBY89MBSN.dev.warp/Library/Application Support/dev.warp.Warp-Stable/warp.sqlite
```

## Relevant Tables

| Table | Purpose |
|-------|---------|
| `ai_queries` | Individual user inputs with timestamps, working directory |
| `agent_conversations` | Conversation metadata (token usage, not message content) |

## Schema: ai_queries

```sql
CREATE TABLE ai_queries (
  id INTEGER PRIMARY KEY NOT NULL,
  exchange_id TEXT NOT NULL,
  conversation_id TEXT NOT NULL,
  start_ts DATETIME NOT NULL,
  input TEXT NOT NULL,  -- JSON array with Query objects
  working_directory TEXT,
  output_status TEXT NOT NULL,
  model_id TEXT NOT NULL DEFAULT '',
  ...
);
```

## Extracting User Inputs

### List recent queries for a project

```bash
sqlite3 "$HOME/Library/Group Containers/2BBY89MBSN.dev.warp/Library/Application Support/dev.warp.Warp-Stable/warp.sqlite" \
  "SELECT start_ts, substr(input, 1, 100) FROM ai_queries WHERE working_directory LIKE '%your-project%' ORDER BY start_ts DESC LIMIT 20"
```

### Extract full verbatim inputs with Python

```bash
sqlite3 "path/to/warp.sqlite" \
  "SELECT start_ts, input FROM ai_queries WHERE date(start_ts) = '2026-01-31' AND working_directory LIKE '%pearc26%' AND input != '[]' ORDER BY start_ts" \
  | python3 -c "
import sys, json
for line in sys.stdin:
    parts = line.strip().split('|', 1)
    if len(parts) < 2: continue
    ts, data = parts
    try:
        parsed = json.loads(data)
        if parsed:
            text = parsed[0].get('Query', {}).get('text', '')
            if text:
                print(f'=== {ts} ===')
                print(text)
                print()
    except: pass
"
```

## Input JSON Structure

The `input` column contains a JSON array. User text is nested:

```json
[{
  "Query": {
    "text": "Your actual input text here",
    "context": [
      {"Directory": {"pwd": "/path/to/project", ...}},
      {"Git": {"head": "branch-name"}},
      {"ProjectRules": {...}},
      ...
    ]
  }
}]
```

## Caveats

1. **Not all sessions are captured** - We observed gaps in the database (sessions from 20:01-20:33 missing while 19:16-19:41 and 21:18+ were present)
2. **Active sessions may not be persisted** - Data may only be written when a conversation ends
3. **Database path may vary** - The `2BBY89MBSN` identifier might be installation-specific
4. **This is undocumented** - Warp's internal storage format could change

## Recommendation

Don't rely on database recovery as your primary audit trail. Instead:
- Always include verbatim `user_input` in session log frontmatter
- Log sessions promptly before context is lost
- Use this recovery technique only as a backup

## Related

- `rules/session_logs.md` - Session logging requirements
- `AGENTS.md` - Agent workflow rules
