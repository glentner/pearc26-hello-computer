# Agent Text Editing Pitfalls

## Discovery

When working with agentic tools (Warp, Cursor, etc.) on text editing tasks—especially LaTeX manuscripts or prose—agents frequently make a specific class of error: **context truncation during edits**.

## The Problem

When an agent constructs a diff to replace text, it often:
1. Includes more context than necessary in the "search" portion
2. Accidentally truncates or drops content that follows the intended edit point
3. Loses sentences, phrases, or entire paragraphs adjacent to the edit

### Example

**Intended edit**: Change `configuration---no` to `configuration: no`

**What the agent does**:
```
search: "configuration---no new credentials, no hosted infrastructure,
no additional attack surface. This pattern respects"
replace: "configuration: no new credentials, no hosted infrastructure,"
```

**Result**: "This pattern respects..." is silently deleted.

## Why This Happens

1. **Context greed**: Agents try to include "enough context" to make the search unique, but then fail to reproduce all of it in the replacement
2. **Line-based thinking**: When crossing line boundaries, agents may stop at arbitrary points
3. **Attention drift**: In longer edits, the agent's attention to preserving trailing content diminishes

## Mitigation Strategies

### For Users

1. **Review diffs carefully** before accepting—look for truncation at the end of replacements
2. **Request minimal edits**: Ask the agent to change "only the specific character/word"
3. **Be explicit**: "Do not modify any surrounding text"
4. **Verify after edits**: Re-read the file to catch silent deletions
5. **Use version control**: Commit frequently so you can easily see and revert damage

### For Prompting

When requesting text edits, be explicit:
- "Change X to Y without modifying any surrounding content"
- "Make a single-line replacement only"
- "Do not include adjacent sentences in the diff"

## Observed Frequency

In a single editing session (this project, 2026-02-02), the agent made this error **4+ times** when asked to:
- Replace em-dashes with alternative punctuation
- Sync content between .tex and .md files
- Convert `\subsection{}` to `\paragraph{}`

Each time required user intervention to catch the truncation.

## Related

- `logs/2026-02-02T04-18-46-fix-overfull-hboxes.md` - Session where this was observed
- `rules/session_logs.md` - Why logging helps catch these issues
