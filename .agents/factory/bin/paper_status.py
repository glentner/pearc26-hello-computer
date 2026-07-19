#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Report the paper-factory FSM state as JSON (the ``next_phase.py`` analog).

The ``/paper-*`` skills run this at the top of every invocation instead of
parsing ``PAPER.md`` themselves. The emitted JSON is the ground truth for "where
is the paper and what is actionable next"; the model executes, the script
computes the state.

Unlike hypershell's linear phase FSM, a paper lifecycle is cyclic and additive,
so this reporter does NOT return a single authoritative "next phase". It returns
section **status buckets** (ordered by the section ``order`` field, so the
abstract — written last — never floats to the top), a per-``macro_phase``
completion predicate, and a set of reconciliation **warnings** (the analog of
hypershell's ``current_phase`` pointer-drift signal).

Usage:
    python3 .agents/factory/bin/paper_status.py [PAPER.md]

Exit codes: 0 ok (warnings, if any, are in the JSON) · 2 parse/validation error.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from _fsm import FSMError, split_frontmatter, validate

__all__ = ["main"]

_CYCLE_BOUND = 3  # review<->revise cycles before we recommend escalation

_ANCHORS_FENCE = re.compile(r"```anchors\n(.*?)```", re.DOTALL)
_STATUS_LINE = re.compile(r"^status:\s*(.+?)\s*$", re.MULTILINE)


def _read(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return None


def _parse_anchor_map(body: str) -> list[tuple[str, str]]:
    """Parse the ```anchors fenced block: one 'id | \\anchor' per line."""
    m = _ANCHORS_FENCE.search(body)
    if not m:
        return []
    pairs: list[tuple[str, str]] = []
    for line in m.group(1).splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if " | " not in line:
            continue
        sid, anchor = line.split(" | ", 1)
        pairs.append((sid.strip(), anchor.strip()))
    return pairs


def _scan_outline_status(outline_dir: Path, sid: str) -> str | None:
    """Extract the ``status:`` scalar from outline/<sid>.md frontmatter."""
    text = _read(outline_dir / f"{sid}.md")
    if text is None:
        return None
    # Only look inside the leading frontmatter block.
    if text.startswith("---"):
        end = text.find("\n---", 3)
        text = text[:end] if end != -1 else text
    m = _STATUS_LINE.search(text)
    return m.group(1) if m else None


def _scan_refs(refs_readme: Path) -> dict[str, int]:
    text = _read(refs_readme) or ""
    return {
        "complete": len(re.findall(r"^- \[x\]", text, re.MULTILINE)),
        "in_progress": len(re.findall(r"^- \[~\]", text, re.MULTILINE)),
        "pending": len(re.findall(r"^- \[ \]", text, re.MULTILINE)),
    }


def _scan_feedback(notes_dir: Path) -> dict[str, int]:
    counts = {"must-fix": 0, "should-fix": 0, "consider": 0}
    for fb in sorted(notes_dir.glob("review-feedback-*.md")):
        text = _read(fb) or ""
        for sev in counts:
            counts[sev] += len(re.findall(
                r"\*\*Severity\*\*:\s*" + re.escape(sev), text))
    return counts


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Report the paper-factory FSM state.")
    ap.add_argument("path", nargs="?", default="PAPER.md", help="path to PAPER.md")
    ap.add_argument("--summary", action="store_true",
                    help="print a one-line human summary instead of the full JSON")
    args = ap.parse_args(argv)
    path = Path(args.path)
    text = _read(path)
    if text is None:
        print(f"cannot read {path}", file=sys.stderr)
        return 2
    try:
        data, body = split_frontmatter(text)
    except FSMError as exc:
        print(f"{path}: {exc}", file=sys.stderr)
        return 2
    errors = validate(data)
    if errors:
        print(f"{path}: invalid PAPER.md frontmatter:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 2

    root = path.resolve().parent
    outline_dir = root / "outline"
    notes_dir = outline_dir / "notes"
    sections = data.get("sections") or []
    claims = data.get("claims") or []
    warnings: list[str] = []

    # Section status buckets, ordered by the writing-order field (not file order).
    buckets: dict[str, list[str]] = {
        "draft": [], "review": [], "integrated": [], "blocked": []}
    for sec in sorted(sections, key=lambda s: s.get("order", 999)):
        buckets.setdefault(sec.get("status", "draft"), []).append(sec.get("id"))

    # Durable per-section draft<->audit attempts (the internal circuit breaker; distinct
    # from review.cycle, which is the external review<->revise loop).
    section_attempts: dict[str, int] = {}
    for sec in sections:
        n = sec.get("attempts")
        if isinstance(n, int) and n > 0:
            section_attempts[sec.get("id")] = n
            if n >= 3:
                warnings.append(
                    f"section {sec.get('id')}: {n} draft<->audit attempts (>=3) — not converging; "
                    "stop-and-re-shape or escalate to a human")

    # Drift: PAPER.md section status vs the outline file's own frontmatter.
    for sec in sections:
        sid, want = sec.get("id"), sec.get("status")
        have = _scan_outline_status(outline_dir, sid)
        if have is not None and have != want:
            warnings.append(
                f"section {sid}: PAPER.md says {want!r} but outline/{sid}.md says {have!r} "
                "(reconcile with set_status.py before acting)")

    # Anchor-existence check against the live manuscript.
    manuscript = _read(root / "manuscript.tex") or ""
    anchor_map = _parse_anchor_map(body)
    missing_anchors = [a for (_sid, a) in anchor_map if a and a not in manuscript]
    for a in missing_anchors:
        warnings.append(f"tex_anchor not found in manuscript.tex: {a}")

    # Claims lacking evidence.
    claims_no_evidence = [
        c.get("id") for c in claims
        if c.get("status") != "cut" and not (c.get("evidence") or [])]

    # Blocked sections.
    if buckets["blocked"]:
        warnings.append(f"blocked sections: {', '.join(buckets['blocked'])}")

    # Review-cycle bound.
    review = data.get("review") or {}
    cycle = review.get("cycle", 0)
    if isinstance(cycle, int) and cycle > _CYCLE_BOUND:
        warnings.append(
            f"review.cycle is {cycle} (> {_CYCLE_BOUND}); self-correction is not "
            "converging — escalate to a human decision")

    # Completion predicates.
    no_draft = not buckets["draft"]
    all_integrated = bool(sections) and all(
        s.get("status") == "integrated" for s in sections)
    no_blocked = not buckets["blocked"]
    feedback = _scan_feedback(notes_dir)
    release_ready = all_integrated and no_blocked

    macro = data.get("macro_phase")
    completion = {
        "outlining_complete": no_draft and no_blocked,
        "integrating_complete": all_integrated and no_blocked,
        "release_ready": release_ready,
    }
    if macro == "released" and not release_ready:
        warnings.append(
            "macro_phase is 'released' but not all sections are integrated / clean")

    # The actionable bucket for the current macro_phase (ordered candidates).
    actionable = {
        "researching": "refs pending (see refs tracker)",
        "outlining": buckets["draft"],
        "integrating": buckets["review"],
        "revising": buckets["review"] or buckets["draft"],
        "in-review": "awaiting external feedback (run /paper-review on the transcript)",
    }.get(macro, [])

    report = {
        "slug": data.get("slug"),
        "title": data.get("title"),
        "venue": data.get("venue"),
        "macro_phase": macro,
        "branch": data.get("branch"),
        "base": data.get("base"),
        "sections_by_status": buckets,
        "section_attempts": section_attempts,
        "actionable_next": actionable,
        "completion": completion,
        "claims_total": len(claims),
        "claims_lacking_evidence": claims_no_evidence,
        "refs": _scan_refs(notes_dir / "refs" / "README.md"),
        "feedback_by_severity": feedback,
        "review": review,
        "anchors_checked": len(anchor_map),
        "anchors_missing": missing_anchors,
        "warnings": warnings,
    }
    if args.summary:
        b = report["sections_by_status"]
        c = report["completion"]
        fb = report["feedback_by_severity"]
        print(
            "macro_phase=%s | integrated=%d review=%d draft=%d blocked=%d | release_ready=%s | "
            "claims_no_evidence=%d | feedback(mf/sf/c)=%d/%d/%d | anchors_missing=%d | warnings=%d"
            % (report["macro_phase"], len(b["integrated"]), len(b["review"]), len(b["draft"]),
               len(b["blocked"]), c["release_ready"], len(report["claims_lacking_evidence"]),
               fb.get("must-fix", 0), fb.get("should-fix", 0), fb.get("consider", 0),
               len(report["anchors_missing"]), len(report["warnings"])))
        return 0
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
