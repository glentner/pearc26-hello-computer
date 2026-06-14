---
timestamp: "2026-06-14T18:20:31Z"
duration_minutes: ~8
user_input: |
  We're ready to upload our final camera-ready paper to ACM's TAPS system. This is to be a zip archive with named pearc26-36.zip where 36 is our TAPS Paper ID (not 160 as in EasyChair). I want to add an 'upload' target to the Makefile that automates this as part of the release where we run 'release' to create the publication-ready PDF and then package it with the source code for the upload. We have a tight size constraint so this isn't a naive 'zip -r'. We definitely don't want the .git or planning material. I think the manuscript.tex should be enough to compile the document. I'm not sure what they want for the name though so let's just try the simple thing first and I'll report back if it was able to build it after the web upload.

  We need '/pdf' to include manuscript.pdf and '/src' to continue the manuscript.tex and any other necessary assets (bib).
files_modified:
  - Makefile
  - .gitignore
  - AGENTS.md
  - README.md
  - logs/2026-06-14T18-20-31-add-taps-upload-target.md
commits:
  - "e77f7ea: WIP: Add make upload target for ACM TAPS camera-ready package"
  - "7d626a4: WIP: Use Source/ instead of src/ in TAPS upload archive"
---

# Add `make upload` Target for ACM TAPS Camera-Ready Package

## Summary

Added an `upload` target to the `Makefile` that produces `pearc26-36.zip`, the
camera-ready submission package for ACM TAPS (TAPS Paper ID 36, distinct from the
EasyChair submission ID 160). The target chains off `release` so a single command
builds the publication PDF and packages it with the minimal LaTeX source.

## Work Completed

- **`Makefile`**: Added `TAPS_ID`, `UPLOAD`, `STAGEDIR`, `PDFDIR`, and `SRCDIR`
  variables; a new `upload: release` target; added `upload` to `.PHONY`; and
  extended `distclean` to remove `pearc26-*.zip`.
  - The target stages only what TAPS needs into `build/taps/` (gitignored) and
    zips it: `pdf/manuscript.pdf` (the author PDF, copied from
    `build/manuscript.pdf`) and `Source/manuscript.tex` + `Source/references.bib`
    (the sources required to recompile). It then removes the staging directory.
  - The in-archive folder names are centralized as `PDFDIR` (`pdf`) and `SRCDIR`
    (`Source`) so tuning them for TAPS is a one-line change.
  - This is deliberately **not** a naive `zip -r` of the repository: by staging an
    explicit allowlist of files, the archive excludes `.git/`, `build/` cruft, and
    all planning/process material (`plans/`, `logs/`, `reviews/`, `outline/`,
    `rules/`, `tips/`), keeping it well under TAPS size limits.
  - Uses `/bin/rm` in the recipe per `rules/file_deletion.md` (shell aliases do not
    apply in Makefile recipes) and `zip -r -X` to strip macOS extended attributes.
  - The output path is `$(CURDIR)/$(UPLOAD)` so the zip lands at the repo root
    regardless of the staging subdirectory.
- **`.gitignore`**: Ignore `pearc26-*.zip` (mirrors the existing `*.pdf` handling
  for release artifacts).
- **`AGENTS.md`**: Documented `make upload` in the Build Commands block and added
  the `pearc26-*.zip` artifact to the Build output listing.
- **`README.md`**: Added `make upload` to the Building the Manuscript command list.

### Verification

Ran `make upload` end-to-end (exit 0). It performed a clean `release` rebuild via
`latexmk` and produced `pearc26-36.zip` (~402 KB) containing exactly:

```
pdf/manuscript.pdf
Source/manuscript.tex
Source/references.bib
```

Confirmed the `build/taps/` staging directory was removed afterward and that the
zip is gitignored (only the four tracked files appear as modifications). The
BibTeX warnings emitted during the build (empty publisher/address, missing page
numbers) are pre-existing bibliography metadata issues, unrelated to this change.

## Next Steps

- **Correction (this session):** the first upload attempt used `src/`, but TAPS
  expects the source folder named `Source` (capital S). Renamed `src/` -> `Source/`
  (commit `7d626a4`) and re-ran `make upload` to confirm the archive now lists
  `Source/manuscript.tex`, `Source/references.bib`, and `pdf/manuscript.pdf`.
- The `pdf/` folder name and single-`manuscript.tex` source layout remain a first
  attempt. Pending confirmation that TAPS compiles the upload via the web
  interface; adjust folder names or the main source filename if TAPS expects
  different conventions.
