#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Shared helpers for the paper-factory FSM scripts.

The finite-state machine for a paper lives in the YAML-ish frontmatter of the
repo-root ``PAPER.md``. These helpers read, validate, mutate, and re-serialize
that frontmatter so the *scripts* (not the model) own the fragile serialization
— model in-context YAML editing is the primary FSM-corruption risk (see
``.agents/factory/methodology.md``).

Design (deliberate, see ``.agents/factory/methodology.md`` "State machine"):

* **Stdlib only.** This is a LaTeX repo with no Python environment; requiring
  PyYAML would hurt portability. We vendor a *small, restricted* frontmatter
  parser/serializer instead of depending on a general YAML library.
* **All fragile free-text lives in the BODY, never the frontmatter.** The
  frontmatter is a constrained machine subset: identifiers, enums, integers, and
  flow-lists of identifiers, plus a couple of double-quoted plain-text scalars
  (``title``/``template``). Contribution-claim statements, non-goals, and the
  LaTeX heading map (with its backslashes and TeX open/close quotes) live in the
  Markdown body, which the serializer preserves **verbatim**. This keeps the
  restricted parser safe: it never has to round-trip a backslash or a colon-laden
  rhetorical section title.

The supported frontmatter grammar (canonical form, which ``dump_document`` emits):

    key: <scalar>                     # scalar = bare token | "quoted" | integer
    sections:
      - {id: 01-introduction, status: integrated, satisfies: [C1, C2], target_words: 400, order: 3}
    claims:
      - {id: C1, status: supported, satisfied_by: [00-abstract], evidence: [warp2024agentmode]}
    review: {cycle: 2, verdict: approved}

Run ``python3 .agents/factory/bin/_fsm.py`` to execute the golden round-trip
self-test.
"""
from __future__ import annotations

import datetime
import re
from typing import Any


__all__ = [
    "FSMError",
    "MACRO_PHASES",
    "SECTION_STATUSES",
    "CLAIM_STATUSES",
    "VERDICTS",
    "REQUIRED_TOP",
    "FIELD_ORDER",
    "split_frontmatter",
    "dump_document",
    "validate",
    "today",
]


MACRO_PHASES = [
    "scoped", "researching", "outlining", "integrating",
    "in-review", "revising", "released",
]
SECTION_STATUSES = {"draft", "review", "integrated", "blocked"}
CLAIM_STATUSES = {"proposed", "supported", "cut"}
VERDICTS = {"none", "changes-requested", "approved"}

REQUIRED_TOP = ["slug", "title", "macro_phase", "sections"]

# Canonical key order for deterministic re-serialization.
FIELD_ORDER = [
    "slug", "title", "venue", "template", "macro_phase",
    "base", "branch", "last_updated", "sections", "claims", "review",
]
SECTION_FIELD_ORDER = ["id", "status", "satisfies", "target_words", "order", "attempts"]
CLAIM_FIELD_ORDER = ["id", "status", "satisfied_by", "evidence"]
REVIEW_FIELD_ORDER = ["cycle", "verdict", "reviewed_commit"]

# A bare (unquoted) scalar: identifiers, bibkeys, enums, ISO dates. Anything else
# (spaces, colons, digits-only that must stay a string, LaTeX) must be quoted.
_BARE_RE = re.compile(r"^[A-Za-z0-9_][A-Za-z0-9_.\-]*$")
_INT_RE = re.compile(r"^-?\d+$")


class FSMError(Exception):
    """Raised on a malformed or invalid PAPER.md frontmatter."""


def today() -> str:
    """Return today's date as an ISO-8601 string (local)."""
    return datetime.date.today().isoformat()


# --------------------------------------------------------------------------- #
# Scanning helpers                                                            #
# --------------------------------------------------------------------------- #

def _split_top(text: str, sep: str) -> list[str]:
    """Split ``text`` on ``sep`` at bracket-depth 0 and outside double quotes."""
    parts: list[str] = []
    depth = 0
    in_quote = False
    escaped = False
    cur: list[str] = []
    for ch in text:
        if in_quote:
            cur.append(ch)
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == '"':
                in_quote = False
            continue
        if ch == '"':
            in_quote = True
            cur.append(ch)
        elif ch in "[{":
            depth += 1
            cur.append(ch)
        elif ch in "]}":
            depth -= 1
            cur.append(ch)
        elif ch == sep and depth == 0:
            parts.append("".join(cur))
            cur = []
        else:
            cur.append(ch)
    parts.append("".join(cur))
    return parts


def _split_key_value(text: str) -> tuple[str, str]:
    """Split ``k: v`` on the first top-level colon."""
    depth = 0
    in_quote = False
    escaped = False
    for i, ch in enumerate(text):
        if in_quote:
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == '"':
                in_quote = False
            continue
        if ch == '"':
            in_quote = True
        elif ch in "[{":
            depth += 1
        elif ch in "]}":
            depth -= 1
        elif ch == ":" and depth == 0:
            return text[:i], text[i + 1:]
    raise FSMError(f"expected 'key: value', found: {text!r}")


# --------------------------------------------------------------------------- #
# Parsing                                                                      #
# --------------------------------------------------------------------------- #

def _parse_quoted(text: str) -> str:
    """Parse a double-quoted scalar, handling \\" and \\\\ escapes."""
    out: list[str] = []
    escaped = False
    for ch in text[1:]:
        if escaped:
            out.append(ch)
            escaped = False
        elif ch == "\\":
            escaped = True
        elif ch == '"':
            return "".join(out)
        else:
            out.append(ch)
    raise FSMError(f"unterminated quoted string: {text!r}")


def _parse_value(text: str) -> Any:
    """Parse a scalar / flow-list / flow-mapping value."""
    s = text.strip()
    if s == "":
        return ""
    if s[0] == '"':
        return _parse_quoted(s)
    if s[0] == "[":
        if s[-1] != "]":
            raise FSMError(f"malformed flow list: {text!r}")
        inner = s[1:-1].strip()
        if inner == "":
            return []
        return [_parse_value(p) for p in _split_top(inner, ",")]
    if s[0] == "{":
        if s[-1] != "}":
            raise FSMError(f"malformed flow mapping: {text!r}")
        inner = s[1:-1].strip()
        out: dict[str, Any] = {}
        if inner == "":
            return out
        for part in _split_top(inner, ","):
            if part.strip() == "":
                continue
            k, v = _split_key_value(part)
            out[k.strip()] = _parse_value(v)
        return out
    if _INT_RE.match(s):
        return int(s)
    return s


def split_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    """Split a Markdown document into (frontmatter dict, body string).

    The document must open with a ``---`` fence and close the YAML block with a
    line that is exactly ``---``. Everything after is the body (preserved
    verbatim by ``dump_document``).
    """
    if not text.startswith("---"):
        raise FSMError("PAPER.md must begin with a '---' frontmatter fence.")
    lines = text.splitlines(keepends=True)
    close = None
    for i in range(1, len(lines)):
        # rstrip "\r\n" (not just "\n") so a CRLF-saved file's fence still matches.
        if lines[i].rstrip("\r\n") == "---":
            close = i
            break
    if close is None:
        raise FSMError("Unterminated frontmatter: no closing '---' fence found.")
    fm_lines = [ln.rstrip("\r\n") for ln in lines[1:close]]
    body = "".join(lines[close + 1:])
    return _parse_frontmatter(fm_lines), body


def _parse_frontmatter(fm_lines: list[str]) -> dict[str, Any]:
    data: dict[str, Any] = {}
    i = 0
    n = len(fm_lines)
    while i < n:
        raw = fm_lines[i]
        if raw.strip() == "" or raw.lstrip().startswith("#"):
            i += 1
            continue
        if raw[0] in " \t":
            raise FSMError(f"unexpected indentation at frontmatter line: {raw!r}")
        key, rest = _split_key_value(raw)
        key = key.strip()
        rest = rest.strip()
        if rest != "":
            data[key] = _parse_value(rest)
            i += 1
            continue
        # Block sequence: subsequent indented '- ' items.
        items: list[Any] = []
        i += 1
        while i < n and (fm_lines[i].strip() == "" or fm_lines[i][:1] in (" ", "\t")):
            item = fm_lines[i].strip()
            if item == "":
                i += 1
                continue
            if not item.startswith("- "):
                raise FSMError(f"expected '- ' sequence item, found: {fm_lines[i]!r}")
            items.append(_parse_value(item[2:]))
            i += 1
        data[key] = items
    return data


# --------------------------------------------------------------------------- #
# Serialization                                                                #
# --------------------------------------------------------------------------- #

def _dump_scalar(value: Any) -> str:
    if isinstance(value, bool):  # guard: bool is an int subclass
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, list):
        return "[" + ", ".join(_dump_scalar(v) for v in value) + "]"
    if isinstance(value, str):
        if value != "" and _BARE_RE.match(value) and not _INT_RE.match(value):
            return value
        escaped = value.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{escaped}"'
    raise FSMError(f"cannot serialize value of type {type(value).__name__}: {value!r}")


def _ordered(d: dict[str, Any], order: list[str]) -> list[str]:
    keys = [k for k in order if k in d]
    keys += [k for k in d if k not in order]
    return keys


def _dump_flow_mapping(d: dict[str, Any], order: list[str]) -> str:
    keys = _ordered(d, order)
    return "{" + ", ".join(f"{k}: {_dump_scalar(d[k])}" for k in keys) + "}"


def dump_document(data: dict[str, Any], body: str) -> str:
    """Re-serialize (frontmatter dict, body) into a full Markdown document.

    Serialization is canonical and deterministic: keys are emitted in a fixed
    order; the body is preserved verbatim.
    """
    out: list[str] = []
    for key in _ordered(data, FIELD_ORDER):
        value = data[key]
        if key == "sections" and isinstance(value, list):
            out.append("sections:")
            for sec in value:
                out.append("  - " + _dump_flow_mapping(sec, SECTION_FIELD_ORDER))
        elif key == "claims" and isinstance(value, list):
            out.append("claims:")
            for claim in value:
                out.append("  - " + _dump_flow_mapping(claim, CLAIM_FIELD_ORDER))
        elif key == "review" and isinstance(value, dict):
            out.append("review: " + _dump_flow_mapping(value, REVIEW_FIELD_ORDER))
        else:
            out.append(f"{key}: {_dump_scalar(value)}")
    # The closing fence carries its own newline; ``body`` is everything after it,
    # verbatim (its leading blank line, if any, is preserved).
    return "---\n" + "\n".join(out) + "\n---\n" + body


# --------------------------------------------------------------------------- #
# Validation                                                                   #
# --------------------------------------------------------------------------- #

def validate(data: dict[str, Any]) -> list[str]:
    """Return a list of human-readable validation errors (empty == valid)."""
    errors: list[str] = []
    for key in REQUIRED_TOP:
        if key not in data:
            errors.append(f"missing required top-level key: {key}")
    if "macro_phase" in data and data["macro_phase"] not in MACRO_PHASES:
        errors.append(f"macro_phase {data['macro_phase']!r} not in {MACRO_PHASES}")

    sections = data.get("sections")
    if not isinstance(sections, list) or not sections:
        errors.append("sections must be a non-empty list")
        sections = []
    sec_ids: set[str] = set()
    for idx, sec in enumerate(sections):
        if not isinstance(sec, dict):
            errors.append(f"section[{idx}] is not a mapping")
            continue
        sid = sec.get("id")
        if not sid:
            errors.append(f"section[{idx}] missing id")
            continue
        if sid in sec_ids:
            errors.append(f"duplicate section id: {sid}")
        sec_ids.add(sid)
        if sec.get("status") not in SECTION_STATUSES:
            errors.append(f"section {sid} status {sec.get('status')!r} not in {sorted(SECTION_STATUSES)}")
        att = sec.get("attempts")
        if att is not None and (isinstance(att, bool) or not isinstance(att, int) or att < 0):
            errors.append(f"section {sid} attempts {att!r} must be a non-negative integer")

    claims = data.get("claims") or []
    claim_ids: set[str] = set()
    for idx, claim in enumerate(claims):
        if not isinstance(claim, dict):
            errors.append(f"claim[{idx}] is not a mapping")
            continue
        cid = claim.get("id")
        if not cid:
            errors.append(f"claim[{idx}] missing id")
            continue
        if cid in claim_ids:
            errors.append(f"duplicate claim id: {cid}")
        claim_ids.add(cid)
        if claim.get("status") not in CLAIM_STATUSES:
            errors.append(f"claim {cid} status {claim.get('status')!r} not in {sorted(CLAIM_STATUSES)}")
        for sid in claim.get("satisfied_by") or []:
            if sid not in sec_ids:
                errors.append(f"claim {cid} satisfied_by unknown section {sid}")

    for sec in sections:
        if isinstance(sec, dict):
            for cid in sec.get("satisfies") or []:
                if cid not in claim_ids:
                    errors.append(f"section {sec.get('id')} satisfies unknown claim {cid}")

    review = data.get("review")
    if review is not None:
        if not isinstance(review, dict):
            errors.append("review must be a mapping")
        else:
            if review.get("verdict") not in VERDICTS:
                errors.append(f"review.verdict {review.get('verdict')!r} not in {sorted(VERDICTS)}")
            rc = review.get("reviewed_commit")
            if rc is not None and not isinstance(rc, str):
                errors.append("review.reviewed_commit must be a string")
    return errors


# --------------------------------------------------------------------------- #
# Self-test                                                                    #
# --------------------------------------------------------------------------- #

_GOLDEN = """\
---
slug: hello-computer
title: "Hello Computer: HPC in the Agentic Era"
venue: PEARC26
template: "acmart sigconf"
macro_phase: released
base: main
branch: draft
last_updated: 2026-07-14
sections:
  - {id: 00-abstract, status: integrated, satisfies: [C1, C2], target_words: 150, order: 7}
  - {id: 04-discussion, status: integrated, satisfies: [], target_words: 600, order: 5}
claims:
  - {id: C1, status: supported, satisfied_by: [00-abstract], evidence: [warp2024agentmode, godoy2024llm]}
  - {id: C2, status: proposed, satisfied_by: [00-abstract], evidence: []}
review: {cycle: 2, verdict: approved}
---

# Hello Computer

## Contribution Claims

- **C1** — Proactive engagement, not prohibition, is the path forward: this is a
  section title with a colon and ``curly quotes'' to stress the body parser.

## Section -> LaTeX anchor map

| id | file | tex_anchor |
|----|------|------------|
| 04-discussion | outline/04-discussion.md | \\subsection{``I'm Sorry, Dave'' (User Support)} |
"""


def _selftest() -> int:
    data, body = split_frontmatter(_GOLDEN)
    errors = validate(data)
    if errors:
        print("SELFTEST FAIL: golden document did not validate:")
        for err in errors:
            print(f"  - {err}")
        return 1
    rendered = dump_document(data, body)
    if rendered != _GOLDEN:
        print("SELFTEST FAIL: round-trip is not byte-stable.")
        import difflib
        for line in difflib.unified_diff(
            _GOLDEN.splitlines(), rendered.splitlines(),
            "golden", "rendered", lineterm="",
        ):
            print(line)
        return 1
    # Re-parse the rendered output (idempotence).
    data2, body2 = split_frontmatter(rendered)
    if dump_document(data2, body2) != _GOLDEN:
        print("SELFTEST FAIL: second round-trip diverged.")
        return 1
    # Adversarial body content survived verbatim.
    assert "\\subsection{``I'm Sorry, Dave'' (User Support)}" in body2, "body corrupted"
    assert data2["title"] == "Hello Computer: HPC in the Agentic Era", "title corrupted"
    # Validation rejects a bad enum.
    bad = dict(data)
    bad["macro_phase"] = "bogus"
    if not validate(bad):
        print("SELFTEST FAIL: validate() accepted a bogus macro_phase.")
        return 1
    # CRLF frontmatter must parse (F15 regression guard: a \r must not leak into a scalar).
    crlf = _GOLDEN.replace("\n", "\r\n")
    cdata, _cbody = split_frontmatter(crlf)
    if validate(cdata):
        print("SELFTEST FAIL: CRLF golden did not validate.")
        return 1
    if cdata.get("title") != "Hello Computer: HPC in the Agentic Era":
        print("SELFTEST FAIL: CRLF parse left a stray carriage return in a scalar.")
        return 1
    print("SELFTEST OK: golden round-trip byte-stable; CRLF parses; validation rejects bad enums.")
    return 0


if __name__ == "__main__":
    raise SystemExit(_selftest())
