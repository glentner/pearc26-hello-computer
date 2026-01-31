---
created: "2026-01-31"
status: "completed"
---

# LaTeX Build System with Makefile and CI/CD

## Context

The project needs a modern build system for the PEARC'26 manuscript that:
- Isolates build artifacts in a `build/` directory
- Supports iterative development with live-reload (latexmk -pvc + Skim)
- Produces versioned release PDFs
- Integrates with GitHub Actions for automated release builds

## Current State

- `manuscript.tex` at repo root with `references.bib`
- Build artifacts (`.aux`, `.log`, `.bbl`, etc.) currently in repo root
- `.gitignore` already excludes LaTeX artifacts and PDFs
- Using `latexmk` for compilation (per AGENTS.md)

## Proposed Approach

### 1. Makefile Targets

| Target | Purpose |
|--------|--------|
| `all` | Default: build PDF to `build/` |
| `build` | Single incremental build via `latexmk` |
| `release` | Full clean rebuild with multi-pass, copy to `lentner-{date}-{rev}.pdf` |
| `watch` | Live mode: `latexmk -pvc` for continuous rebuild |
| `open` | Open PDF in Skim |
| `clean` | Remove build artifacts but keep release PDFs |
| `distclean` | Remove everything including releases |

### 2. Build Directory Structure

```
build/
├── manuscript.pdf      # Working build
├── manuscript.aux
├── manuscript.bbl
└── ... (all intermediates)
lentner-2026-abc1234.pdf  # Release artifact at root
```

### 3. Key Improvements Over Old Makefiles

**From Alpha Spectroscopy:**
- Good: `build/` output directory, `draft` vs `final` distinction, date-stamped copies
- Improve: Use `latexmk` instead of manual multi-pass pdflatex/bibtex

**From Faculty Interview:**
- Good: `live` target with fswatch, cleaner variable organization
- Improve: Use `latexmk -pvc` for continuous mode (simpler than fswatch pipe)

**Modern approach:**
- `latexmk -pvc` has built-in file watching and continuous preview
- `-output-directory=build` isolates all artifacts
- `latexmk -C` handles cleanup comprehensively
- Add git short-rev to release filename for traceability

### 4. GitHub Actions Release Workflow

`.github/workflows/release.yml` triggered on tag push:
1. Checkout code
2. Install TeX Live (use `xu-cheng/latex-action`)
3. Build PDF with latexmk
4. Upload PDF as release asset

### 5. Release Shipping Procedure

1. Squash WIP commits on `wip` branch
2. Merge `wip` → `main`
3. Tag with semantic version (e.g., `v0.1.0`)
4. Push tag → triggers CI build
5. CI attaches `lentner-{year}-{hash}.pdf` to GitHub release

## Decisions

1. **Skim refresh**: Use Skim's built-in file-change detection (no post-build hook needed)
2. **Release naming**: `lentner-2026-{hash}.pdf` format
3. **Manuscript location**: Keep at root for now
4. **Watch mechanism**: Use `latexmk -pvc` (simpler, built-in)
