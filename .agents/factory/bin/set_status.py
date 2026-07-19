#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Mutate the paper-factory FSM (the ``set_phase.py`` analog).

The ``/paper-*`` skills call this to advance state rather than hand-editing the
``PAPER.md`` frontmatter (surgical in-place edits corrupt structure). It parses
the frontmatter, applies the requested mutations, re-serializes canonically, and
writes ``PAPER.md`` back with the body preserved verbatim.

To eliminate two-source drift (PAPER.md is authoritative for section status, but
each ``outline/<id>.md`` also carries a human-visible ``status:``), a
``--section`` mutation ALSO rewrites that one outline file's ``status:`` line via
a targeted single-line replace — safe against the outline files' block scalars,
comments, and flow lists.

Usage examples:
    # advance a section (updates PAPER.md AND outline/03-approach.md), stamp today
    python3 .agents/factory/bin/set_status.py PAPER.md --section 03-approach --status review --touch

    # move the whole paper into a revision cycle after external feedback
    python3 .agents/factory/bin/set_status.py PAPER.md --macro-phase revising --bump-cycle --verdict changes-requested --touch

    # mark a contribution claim supported by its evidence
    python3 .agents/factory/bin/set_status.py PAPER.md --claim C1 --claim-status supported

Exit codes: 0 ok · 2 parse/validation error · 3 unknown --section/--claim id.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from _fsm import (
    FSMError,
    CLAIM_STATUSES,
    MACRO_PHASES,
    SECTION_STATUSES,
    VERDICTS,
    dump_document,
    split_frontmatter,
    today,
    validate,
)

__all__ = ["main"]


def _parse_args(argv: list[str]) -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Advance the PAPER.md FSM.")
    ap.add_argument("path", nargs="?", default="PAPER.md", help="path to PAPER.md")
    ap.add_argument("--section", help="section id to mutate (e.g. 03-approach)")
    ap.add_argument("--status", choices=sorted(SECTION_STATUSES), help="new status for --section")
    ap.add_argument("--record-attempt", action="store_true",
                    help="increment --section's draft<->audit attempts counter (durable circuit breaker)")
    ap.add_argument("--claim", help="claim id to mutate (e.g. C1)")
    ap.add_argument("--claim-status", choices=sorted(CLAIM_STATUSES), help="new status for --claim (or default for --add-claim)")
    ap.add_argument("--add-evidence", metavar="BIBKEY",
                    help="append a bibkey to --claim's evidence list (idempotent)")
    ap.add_argument("--add-section", metavar="ID",
                    help="append a new section (status default draft) through the validated serializer")
    ap.add_argument("--add-claim", metavar="ID",
                    help="append a new claim (status default proposed) through the validated serializer")
    ap.add_argument("--satisfies", help="comma-separated C-IDs (for --add-section)")
    ap.add_argument("--satisfied-by", dest="satisfied_by", help="comma-separated section ids (for --add-claim)")
    ap.add_argument("--target-words", dest="target_words", type=int, help="target_words (for --add-section)")
    ap.add_argument("--order", type=int, help="writing order (for --add-section)")
    ap.add_argument("--macro-phase", choices=MACRO_PHASES, help="set the top-level macro_phase")
    ap.add_argument("--verdict", choices=sorted(VERDICTS), help="set review.verdict")
    ap.add_argument("--reviewed-commit", dest="reviewed_commit",
                    help="set review.reviewed_commit (the commit the pass-B audit graded)")
    ap.add_argument("--review-cycle", type=int, help="set review.cycle explicitly")
    ap.add_argument("--bump-cycle", action="store_true", help="increment review.cycle by 1")
    ap.add_argument("--touch", action="store_true", help="set last_updated to today")
    return ap.parse_args(argv)


def _sync_outline_status(outline_dir: Path, sid: str, status: str) -> str:
    """Targeted single-line rewrite of outline/<sid>.md 'status:' (returns a note)."""
    path = outline_dir / f"{sid}.md"
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return f"(no outline/{sid}.md to sync)"
    if not text.startswith("---"):
        return f"(outline/{sid}.md has no frontmatter to sync)"
    end = text.find("\n---", 3)
    if end == -1:
        return f"(outline/{sid}.md frontmatter not terminated)"
    fm, rest = text[:end], text[end:]
    new_fm, n = re.subn(r"(?m)^status:\s*.*$", f"status: {status}", fm, count=1)
    if n == 0:
        return f"(outline/{sid}.md has no status: line)"
    if new_fm == fm:
        return f"outline/{sid}.md status already {status}"
    path.write_text(new_fm + rest, encoding="utf-8")
    return f"synced outline/{sid}.md status -> {status}"


def main(argv: list[str]) -> int:
    args = _parse_args(argv)
    path = Path(args.path)
    try:
        text = path.read_text(encoding="utf-8")
        data, body = split_frontmatter(text)
    except (OSError, FSMError) as exc:
        print(f"{path}: {exc}", file=sys.stderr)
        return 2

    notes: list[str] = []

    # Additions route through the canonical serializer; validate() below refuses a
    # duplicate id, so a section/claim is never hand-added to the frontmatter.
    if args.add_section:
        sections = data.setdefault("sections", [])
        sections.append({
            "id": args.add_section,
            "status": args.status or "draft",
            "satisfies": [s.strip() for s in (args.satisfies or "").split(",") if s.strip()],
            "target_words": args.target_words if args.target_words is not None else 0,
            "order": args.order if args.order is not None else len(sections) + 1,
        })
        notes.append(f"added section {args.add_section} (create outline/{args.add_section}.md in the skill)")
    if args.add_claim:
        claims = data.setdefault("claims", [])
        claims.append({
            "id": args.add_claim,
            "status": args.claim_status or "proposed",
            "satisfied_by": [s.strip() for s in (args.satisfied_by or "").split(",") if s.strip()],
            "evidence": [],
        })
        notes.append(f"added claim {args.add_claim}")

    if args.section:
        sections = data.get("sections") or []
        target = next((s for s in sections if s.get("id") == args.section), None)
        if target is None:
            print(f"{path}: unknown section id {args.section!r}", file=sys.stderr)
            return 3
        if args.status:
            target["status"] = args.status
            notes.append(_sync_outline_status(path.resolve().parent / "outline",
                                              args.section, args.status))
        if args.record_attempt:
            target["attempts"] = int(target.get("attempts") or 0) + 1
            notes.append(f"section {args.section} attempts -> {target['attempts']}")
    else:
        if args.record_attempt:
            print("--record-attempt requires --section", file=sys.stderr)
            return 2
        if args.status and not args.add_section:
            print("--status requires --section (or --add-section)", file=sys.stderr)
            return 2

    if args.claim:
        claims = data.get("claims") or []
        target = next((c for c in claims if c.get("id") == args.claim), None)
        if target is None:
            print(f"{path}: unknown claim id {args.claim!r}", file=sys.stderr)
            return 3
        if args.claim_status:
            target["status"] = args.claim_status
        if args.add_evidence:
            ev = target.get("evidence") or []
            if args.add_evidence not in ev:
                ev.append(args.add_evidence)
            target["evidence"] = ev
    else:
        if (args.claim_status or args.add_evidence) and not args.add_claim:
            print("--claim-status/--add-evidence require --claim (or --add-claim)", file=sys.stderr)
            return 2

    if args.macro_phase:
        data["macro_phase"] = args.macro_phase

    if (args.verdict or args.review_cycle is not None or args.bump_cycle
            or args.reviewed_commit is not None):
        review = data.get("review")
        if not isinstance(review, dict):
            review = {"cycle": 0, "verdict": "none"}
        if args.verdict:
            review["verdict"] = args.verdict
        if args.review_cycle is not None:
            review["cycle"] = args.review_cycle
        if args.bump_cycle:
            review["cycle"] = int(review.get("cycle", 0)) + 1
        if args.reviewed_commit is not None:
            review["reviewed_commit"] = args.reviewed_commit
        data["review"] = review

    if args.touch:
        data["last_updated"] = today()

    errors = validate(data)
    if errors:
        print(f"{path}: refusing to write — resulting frontmatter is invalid:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 2

    path.write_text(dump_document(data, body), encoding="utf-8")
    print(f"updated {path}")
    for note in notes:
        print(f"  {note}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
