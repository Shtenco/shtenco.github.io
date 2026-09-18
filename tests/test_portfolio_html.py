from __future__ import annotations
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
INDEX=ROOT/"index.html"

class PortfolioHtmlTests(unittest.TestCase):
    def setUp(self):
        self.html=INDEX.read_text(encoding="utf-8")

    def test_required_sections_and_assets(self):
        for section in ("hero","architecture","flagships","lineage","research","products","registry","principles","contacts"):
            self.assertIn(f'id="{section}"',self.html)
        self.assertIn('assets/portfolio.css',self.html)
        self.assertIn('assets/portfolio.js',self.html)

    def test_primary_github_identity_is_current(self):
        self.assertIn("https://github.com/Shtenco",self.html)
        self.assertNotIn('href="https://github.com/koshtenko"',self.html)

    def test_no_stale_visible_repo_total(self):
        self.assertNotIn(">59 repositories<",self.html.lower())
        self.assertNotIn(">60 repositories<",self.html.lower())

    def test_architecture_boundary_and_fallback(self):
        self.assertIn("repository ≠ federation principal",self.html.lower())
        self.assertIn('data-fallback-flagship',self.html)

if __name__=="__main__":
    unittest.main()
