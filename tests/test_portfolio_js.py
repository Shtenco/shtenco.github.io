from __future__ import annotations
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
JS=ROOT/"assets"/"portfolio.js"

class PortfolioJsTests(unittest.TestCase):
    def test_controller_contract(self):
        self.assertTrue(JS.exists(),"assets/portfolio.js must exist")
        text=JS.read_text(encoding="utf-8")
        for token in ("data/repositories.json","repositories.length","lifecycle","domain","visibility","search","flagshipOnly","aria-pressed","public_url","lang"):
            self.assertIn(token,text)
        for fn in ("loadRepositories","deriveMetrics","filterRepositories","renderRepositoryCard","renderRegistry","renderFlagships","renderDomainCollections"):
            self.assertIn(f"function {fn}",text)

if __name__=="__main__":
    unittest.main()
