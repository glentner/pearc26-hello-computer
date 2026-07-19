# SPDX-License-Identifier: MIT
"""Stdlib unit tests for the deterministic linters (check_paper.py)."""
import sys
import unittest
from pathlib import Path

BIN = Path(__file__).resolve().parents[1] / ".agents" / "factory" / "bin"
sys.path.insert(0, str(BIN))

import check_paper  # noqa: E402

BIB = """\
@article{good2020, title={A}, year={2020}}
@misc{orphan2021, title={B}, year={2021}}
"""


class TestCitations(unittest.TestCase):
    def test_clean_pair_no_errors(self):
        f = check_paper.Findings()
        check_paper.check_citations(r"Text \cite{good2020} more.", "@article{good2020, year={2020}}", f)
        self.assertEqual(f.errors, 0)

    def test_dangling_cite_is_error(self):
        f = check_paper.Findings()
        check_paper.check_citations(r"See \cite{missing}.", BIB, f)
        self.assertEqual(f.errors, 1)
        self.assertTrue(any("dangling" in m for _, _, m in f.items))

    def test_orphan_entry_is_warning_not_error(self):
        f = check_paper.Findings()
        check_paper.check_citations(r"See \cite{good2020}.", BIB, f)
        self.assertEqual(f.errors, 0)
        self.assertTrue(any("uncited" in m for _, _, m in f.items))

    def test_multi_key_cite(self):
        f = check_paper.Findings()
        check_paper.check_citations(r"\cite{good2020,orphan2021}", BIB, f)
        self.assertEqual(f.errors, 0)  # both resolve

    def test_comment_line_cite_ignored(self):
        f = check_paper.Findings()
        # a \cite inside a LaTeX comment must not count as a real citation
        check_paper.check_citations("%% \\cite{missing}\nreal text", "@x{y}", f)
        self.assertEqual(f.errors, 0)


class TestProse(unittest.TestCase):
    def test_raw_emdash_warns(self):
        f = check_paper.Findings()
        check_paper.check_prose("A sentence --- with an em-dash.", f)
        self.assertTrue(any("em-dash" in m for _, _, m in f.items))

    def test_endash_range_ok(self):
        f = check_paper.Findings()
        check_paper.check_prose("July 26--30, 2026.", f)
        self.assertFalse(any("em-dash" in m for _, _, m in f.items))

    def test_straight_quote_warns(self):
        f = check_paper.Findings()
        check_paper.check_prose('He said "hi".', f)
        self.assertTrue(any("straight" in m for _, _, m in f.items))

    def test_warnings_are_not_errors(self):
        f = check_paper.Findings()
        check_paper.check_prose("--- and a \" quote", f)
        self.assertEqual(f.errors, 0)


if __name__ == "__main__":
    unittest.main()
