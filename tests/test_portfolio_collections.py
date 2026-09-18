from __future__ import annotations
import json
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"data"/"repositories.json"

class PortfolioCollectionsTests(unittest.TestCase):
    def setUp(self):
        self.repos=json.loads(DATA.read_text(encoding="utf-8"))["repositories"]
        self.by={r["name"]:r for r in self.repos}

    def test_flagships(self):
        expected={"synergy_system","synergy_financial_os","synergy_pay_system","midas_ai","agi_nexus","agi_autopilot","synergy_ai_company","synergy_eurasian","nexus_science_agent","shttps","synergynet","synergy_meta_os","turbo_linux","synergy_ai_blockchain","ai_compress","ai_language","synergy_messenger","synergy_app"}
        self.assertTrue(expected.issubset({r["name"] for r in self.repos if r["flagship"]}))

    def test_trading_lineage(self):
        self.assertEqual(self.by["synergy_agi_trader"]["lifecycle"],"R&D")
        self.assertEqual(self.by["synergy_agi_trader"]["canonical_successor"],"midas_ai")
        for name in ("quantum-trading_metatrader5","computer_vision_trading_metatrader_5","swap_arbitrage_metatrader_5","cross_forex_arbitrage_trading_metatrader_5","3D_bars_market_structure"):
            self.assertIn(name,self.by)

    def test_frontier_research(self):
        for name in ("binary_quantum_theory","cold_nuclear","dlp_solver","motherboard_xpu_xml","qr_compress","agi_olga"):
            self.assertIn(name,self.by)

    def test_products(self):
        for name in ("synergy_app","synergy_messenger","ai_language","synergychain"):
            self.assertTrue(self.by[name]["product"],name)

if __name__=="__main__":
    unittest.main()
