from __future__ import annotations
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
CSS=ROOT/"assets"/"portfolio.css"

class PortfolioCssTests(unittest.TestCase):
    def test_visual_contract(self):
        self.assertTrue(CSS.exists(),"assets/portfolio.css must exist")
        text=CSS.read_text(encoding="utf-8")
        for token in (":root",".site-nav",".hero",".metric-grid",".system-map",".card-grid",".repo-card",".status-badge",".filter-bar",".registry-grid",".principles-grid",".contact-panel","@media",":focus-visible","prefers-reduced-motion"):
            self.assertIn(token,text)

if __name__=="__main__":
    unittest.main()
