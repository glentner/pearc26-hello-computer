---
timestamp: "2026-02-02T01:35:56Z"
duration_minutes: ~10
user_input: |
  Github actions refinements.

  I want to take a look at our github actions workflow on release. When I look at the assets on the tag/release page there are actually 2 PDFs attached. I think this might actually have to do with us force-pushing tags. If that's the case, we just need to be better about sticking to our workflow rules on the WIP commits so that we do clean merges into the 'main' branch so we don't have relicate PDFs.

  Beyond that, I think I want to update our release workflow to actually only build on true *release* creation instead of all tags. This is how we normally handle CI and here I think I'll be doing a lot more tags and we don't need a build of the PDF for every one of those tags that is pushed. I'll create a stored prompt (slash-command) to trigger an actual release and you can use the 'gh' command-line to handle our release from the latest tag.

  Finally, I want to rename the workflow to .github/workflows/release_pdf.yml because here soon we're going to work on an interactive web interface for our work here as a Wasm-compiled PWA client application in Rust using Leptos. That we'll want to have that build in CI with a release_wasm.yml workflow and setup Github Pages with our index.html scaffolding to have it server our .wasm bundle.
user_followup: |
  Before I push our current commits on 'wip', I also want to revise our naming strategy. Before we were naming our built PDFs as `lentner-{year}-{hash}.pdf` but I've decided it makes more sense (especially with our new change) to instead follow `lentner-{year}-{release}.pdf`.

  Please make that change. Then we can log our interaction in logs/ and do another WIP commit.
files_modified:
  - .github/workflows/release.yml → .github/workflows/release_pdf.yml
  - .warp/prompts/release.md
  - AGENTS.md
  - README.md
  - Makefile
commits:
  - "df10716: WIP: Refine GitHub Actions release workflow"
---

# GitHub Actions Refinements

## Summary

Investigated and fixed duplicate PDF artifacts in GitHub releases. Restructured the release workflow to only trigger on explicit GitHub Release creation rather than tag pushes, and updated the PDF naming convention from commit hash to release version.

## Root Cause Analysis

Using `gh api repos/glentner/pearc26-hello-computer/releases` confirmed:
- v0.3.0, v0.1.1, v0.1.2, v0.1.3 all have duplicate PDFs
- The `softprops/action-gh-release@v2` action auto-creates releases on tag push
- Force-pushing tags (during WIP workflow cleanup) re-triggers the workflow, uploading another PDF to the same release

## Work Completed

### Workflow Changes
- Renamed `.github/workflows/release.yml` → `release_pdf.yml` (prep for future `release_wasm.yml`)
- Changed trigger from `push: tags: - 'v*'` to `release: types: [published]`
- Tags can now be created/pushed freely without triggering builds

### PDF Naming Convention
- Changed from `lentner-2026-{hash}.pdf` to `lentner-2026-{version}.pdf`
- CI workflow strips 'v' prefix from tag (v0.4.0 → 0.4.0)
- Local Makefile uses `git describe --tags --abbrev=0` for version

### New Stored Prompt
- Created `.warp/prompts/release.md` — the `/release` slash-command
- Instructions for manual release workflow via `gh` CLI
- Verifies on `main` branch, suggests next version, creates release

### Documentation Updates
- `AGENTS.md` — added Stored Prompts section referencing `/release`
- `README.md` — updated `make release` description
- `Makefile` — updated comments and variable names

## Next Steps

- Push commits to `wip` branch
- Test the new workflow by creating a release via `/release` prompt after merging to `main`
