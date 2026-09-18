from __future__ import annotations
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
INDEX=ROOT/"index.html"
CSS=ROOT/"assets"/"portfolio.css"

class PortfolioQualityTests(unittest.TestCase):
    def test_metadata_and_semantics(self):
        html=INDEX.read_text(encoding="utf-8")
        for token in ('<html lang="ru"','rel="canonical" href="https://shtenco.github.io/"','property="og:title"','application/ld+json','<nav','<main','aria-label='):
            self.assertIn(token,html)
        self.assertIn('rel="noopener noreferrer"',html)

    def test_accessibility_css(self):
        css=CSS.read_text(encoding="utf-8")
        self.assertIn(":focus-visible",css)
        self.assertIn("prefers-reduced-motion",css)

if __name__=="__main__":
    unittest.main()
