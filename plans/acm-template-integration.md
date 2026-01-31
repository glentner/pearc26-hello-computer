---
created: "2026-01-31"
status: "completed"
related_logs:
  - logs/2026-01-31T19-34-08.md
---

# ACM Template Integration for PEARC'26 Extended Abstract

## Context

The repository needed a properly configured LaTeX manuscript using the ACM `acmart` template for submission to PEARC'26 (Practice & Experience in Advanced Research Computing 2026). The existing `manuscript.tex` had placeholder content from the ACM template examples.

## Goals

- Produce a minimum-viable LaTeX document that compiles successfully
- Configure correct PEARC'26 conference metadata
- Set up author information with ORCIDs and affiliations
- Prepare TODOs for content that will be filled in later (CCS codes, keywords, abstract)
- Ensure no demo assets are committed to version control

## Current State (Before)

- `manuscript.tex` existed with `[manuscript, screen, authorversion]` options
- Placeholder conference metadata ("Woodstock" conference, 2018 dates)
- Placeholder author (Ben Trovato)
- Placeholder CCS codes and keywords
- No `.bib` file
- No `.gitignore` for LaTeX auxiliary files

## Decision

- Use `\documentclass[manuscript]{acmart}` per PEARC submission guidelines (switch to `sigconf` for camera-ready)
- Rely on TexLive's bundled `acmart.cls` and `ACM-Reference-Format.bst` rather than copying files into the repository
- Comment out CCS codes and keywords with TODO markers rather than removing them entirely

## Implementation Notes

- PEARC'26 conference details: July 26–30, 2026, Minneapolis Convention Center, Minneapolis, MN
- Both authors affiliated with Rosen Center for Advanced Computing, Purdue University
- The document builds with expected warnings about empty bibliography (no citations yet)
- `TotPages` reference warning is expected and will resolve with subsequent builds

## Outcome

All goals met. The manuscript compiles successfully and is ready for content.
