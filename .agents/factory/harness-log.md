# Harness change log (`/paper-harness`)

The cross-job ledger of every harness self-improvement **decision** — the *act* side of the paper
factory's self-improvement loop. `/paper-harness` appends one entry per **applied** / **rejected** (and
notable **deferred**) finding, and **reads this file before applying**: a proposed fix that reverts a
recent change, or repeats a previously-rejected one, is flagged to the human rather than silently
re-applied. This is the loop's **anti-thrash memory**. (Findings themselves live in the repo-root
`META.md`; this file is the durable record of what was *done* about them.)

Unlike `META.md`, this ledger lives **inside `.agents/factory/`** so it **travels** when the `.agents/`
tree is copied to bootstrap a new paper — cross-paper memory of what harness changes worked. Every
entry's commit uses the `[harness]` subject and keeps the configurable co-author trailer.

Entry format — one section per decision, newest at the bottom:

```markdown
## {YYYY-MM-DD} — {F#}: {one-line title}
`decision=applied|rejected|deferred commit={sha|—} target={file}`
- **Rationale:** what was changed (and why it generalizes) / why rejected (overfit, stale, would-weaken-a-gate) / why deferred.
```

Read `origin`/`severity`/`category` from the finding in `META.md`; this ledger records the *outcome*.

---

<!-- Decisions are appended below this line by /paper-harness. -->
