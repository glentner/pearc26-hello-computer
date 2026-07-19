#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Deterministic paper linters (wired into ``make check``).

The paper-invariants (`.agents/factory/invariants.md`) are mostly grep-able; a
script catches them reliably rather than trusting a cold-read. Three checks:

1. **Citation integrity** — every ``\\cite`` key in ``manuscript.tex`` exists in
   ``references.bib`` (dangling cite = ERROR), and every ``.bib`` entry is cited
   (uncited entry = WARNING). Both directions, from the tex+bib pair only — NOT
   from the outline ``citations:`` frontmatter, which is incomplete (present in
   only 3 of 7 section files).
2. **Prose conventions** — raw ``---`` em-dashes (a recurring reviewer complaint,
   FB-1.02), straight double quotes (should be `` ``...'' ``), and a stale
   generative-AI disclosure naming a superseded harness.
3. **Budget** — PDF page count vs the venue limit (via ``pdfinfo``, if available),
   and per-section outline word counts vs their ``target_words``.

Usage:
    python3 .agents/factory/bin/check_paper.py [REPO_ROOT] [--page-limit N]

Exit codes: 0 clean (WARNINGs allowed) · 1 one or more ERRORs.
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

try:
    from _fsm import split_frontmatter
except ImportError:  # pragma: no cover
    split_frontmatter = None  # word-budget check degrades gracefully

_CITE_RE = re.compile(r"\\cite[tp]?\*?(?:\[[^\]]*\])*\{([^}]*)\}")
_BIBKEY_RE = re.compile(r"@\w+\s*\{\s*([^,\s]+)\s*,")
_EMDASH_RE = re.compile(r"-{3,}")


class Findings:
    def __init__(self) -> None:
        self.items: list[tuple[str, str, str]] = []  # (severity, check, message)

    def error(self, check: str, msg: str) -> None:
        self.items.append(("ERROR", check, msg))

    def warn(self, check: str, msg: str) -> None:
        self.items.append(("WARN", check, msg))

    @property
    def errors(self) -> int:
        return sum(1 for s, _, _ in self.items if s == "ERROR")


def _strip_comments(tex: str) -> str:
    """Drop LaTeX line comments (a '%' not preceded by a backslash to EOL)."""
    out = []
    for line in tex.splitlines():
        cut = None
        for i, ch in enumerate(line):
            if ch == "%" and (i == 0 or line[i - 1] != "\\"):
                cut = i
                break
        out.append(line if cut is None else line[:cut])
    return "\n".join(out)


def check_citations(tex: str, bib: str, f: Findings) -> None:
    body = _strip_comments(tex)
    cited: set[str] = set()
    for m in _CITE_RE.finditer(body):
        for key in m.group(1).split(","):
            key = key.strip()
            if key:
                cited.add(key)
    defined = {m.group(1) for m in _BIBKEY_RE.finditer(bib)}
    for key in sorted(cited - defined):
        f.error("citations", f"\\cite{{{key}}} has no entry in references.bib (dangling)")
    for key in sorted(defined - cited):
        f.warn("citations", f"references.bib entry '{key}' is never \\cite'd (uncited)")
    if not (cited - defined):
        print(f"  citations: {len(cited)} \\cite keys, all resolve in references.bib "
              f"({len(defined)} entries).")


def check_prose(tex: str, f: Findings) -> None:
    body_lines = _strip_comments(tex).splitlines()
    for n, line in enumerate(body_lines, 1):
        if _EMDASH_RE.search(line):
            f.warn("prose", f"line {n}: raw em-dash '---' (project convention: comma or reword)")
        if '"' in line:
            f.warn("prose", f"line {n}: straight double-quote '\"' (use ``...'' in LaTeX)")
    # Stale AI-use disclosure (harness migration).
    acks = re.search(r"\\begin\{acks\}(.*?)\\end\{acks\}", tex, re.DOTALL)
    if acks and re.search(r"\bWarp\b", acks.group(1)):
        f.warn("disclosure", "generative-AI disclosure in \\begin{acks} names 'Warp'; "
               "update it for the current harness (not auto-edited)")


def check_budget(root: Path, page_limit: int, f: Findings) -> None:
    pdf = root / "build" / "manuscript.pdf"
    if shutil.which("pdfinfo") and pdf.exists():
        try:
            out = subprocess.run(["pdfinfo", str(pdf)], capture_output=True,
                                 text=True, check=True).stdout
            m = re.search(r"^Pages:\s*(\d+)", out, re.MULTILINE)
            if m:
                pages = int(m.group(1))
                if pages > page_limit:
                    f.error("budget", f"PDF is {pages} pages (limit {page_limit})")
                else:
                    print(f"  budget: PDF is {pages}/{page_limit} pages.")
        except subprocess.CalledProcessError:
            f.warn("budget", "pdfinfo failed on build/manuscript.pdf")
    else:
        print("  budget: page check skipped (need pdfinfo + build/manuscript.pdf; run `make build`).")

    paper = root / "PAPER.md"
    if split_frontmatter is None or not paper.exists():
        return
    try:
        data, _ = split_frontmatter(paper.read_text(encoding="utf-8"))
    except Exception:
        return
    for sec in data.get("sections") or []:
        sid, target = sec.get("id"), sec.get("target_words")
        if not isinstance(target, int):
            continue
        text = (root / "outline" / f"{sid}.md")
        if not text.exists():
            continue
        m = re.search(r"^## Draft\s*$(.*?)(?=^## |\Z)", text.read_text(encoding="utf-8"),
                      re.MULTILINE | re.DOTALL)
        if not m:
            continue
        words = len(m.group(1).split())
        if words > target * 1.15:
            f.warn("budget", f"{sid}: draft is ~{words} words (target {target})")


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Deterministic paper linters.")
    ap.add_argument("root", nargs="?", default=".", help="repo root")
    ap.add_argument("--page-limit", type=int, default=4)
    args = ap.parse_args(argv)
    root = Path(args.root).resolve()

    tex_path = root / "manuscript.tex"
    bib_path = root / "references.bib"
    if not tex_path.exists() or not bib_path.exists():
        print(f"cannot find manuscript.tex / references.bib under {root}", file=sys.stderr)
        return 2
    tex = tex_path.read_text(encoding="utf-8")
    bib = bib_path.read_text(encoding="utf-8")

    print("Checking paper invariants...")
    f = Findings()
    check_citations(tex, bib, f)
    check_prose(tex, f)
    check_budget(root, args.page_limit, f)

    if f.items:
        print()
        for severity, check, msg in f.items:
            print(f"  [{severity}] {check}: {msg}")
    print()
    print(f"{f.errors} error(s), {len(f.items) - f.errors} warning(s).")
    return 1 if f.errors else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
