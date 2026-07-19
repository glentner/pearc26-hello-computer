# File Deletion Rules

> **Harness note (Claude Code migration).** The `del` utility and the `rm` warning-alias below are a
> **WARP-shell convenience** and are not guaranteed to be on `PATH` under Claude Code's non-interactive
> bash. Under Claude Code, prefer **`/bin/rm`** (exactly as the Makefile does) for deliberate cleanup,
> or use the editor tools. The `/paper-*` skills and the factory scripts avoid deletion where possible;
> where they must delete build cruft they use `/bin/rm`. The `del`-based guidance below still applies in
> an interactive WARP session.

## Use `del` Instead of `rm` (WARP-interactive)

On this system (in WARP), `rm` is aliased to a warning function that discourages direct use. Instead, use `del` - a command-line move-to-trash utility that provides safe, recoverable file deletion.

### Why `del`?

- **Recoverable**: Files are moved to trash, not permanently deleted
- **Indexed**: Maintains a SQLite index of deleted files
- **Queryable**: Use `del --list` to see what's in trash
- **Restorable**: Use `del --restore` to recover files

### Usage

```bash
# Delete a file (moves to trash)
del file.txt

# Delete multiple files
del file1.txt file2.txt

# List items in trash
del --list

# Restore a file from trash
del --restore file.txt
```

### Exception: Makefiles

For Makefile `clean` targets, use `/bin/rm` directly since:
1. Shell aliases don't apply in Makefile recipes
2. Build artifacts are intentionally disposable
3. The Makefile needs predictable exit codes

Example from our Makefile:
```make
clean:
	/bin/rm -rf $(BUILDDIR)
	/bin/rm -f $(MAIN).aux $(MAIN).log ...
```

### Note for Agents

When working in this repository:
- Use `del` for any ad-hoc file cleanup
- Do not use `rm` directly (it will warn and do nothing)
- The `make clean` target handles build artifacts appropriately
