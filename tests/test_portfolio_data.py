from __future__ import annotations
import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"data"/"repositories.json"
ALLOWED={"CANONICAL","CANDIDATE","R&D","LEGACY","ARCHIVE"}

class PortfolioDataTests(unittest.TestCase):
    def load(self):
        self.assertTrue(DATA.exists(),"data/repositories.json must exist")
        return json.loads(DATA.read_text(encoding="utf-8"))

    def test_schema_and_uniqueness(self):
        d=self.load()
        self.assertEqual(d["schema"],"shtenco.portfolio-repositories/v1")
        repos=d["repositories"]
        names=[r["name"] for r in repos]
        self.assertEqual(len(names),len(set(names)))
        self.assertGreater(len(repos),0)

    def test_closed_lifecycle_and_bilingual_copy(self):
        for r in self.load()["repositories"]:
            self.assertIn(r["lifecycle"],ALLOWED,r["name"])
            self.assertTrue(r["role_ru"],r["name"])
            self.assertTrue(r["role_en"],r["name"])
            self.assertTrue(r["claim_boundary_ru"],r["name"])
            self.assertTrue(r["claim_boundary_en"],r["name"])

    def test_visibility_link_boundary(self):
        for r in self.load()["repositories"]:
            if r["visibility"]=="private":
                self.assertIsNone(r["public_url"],r["name"])
            else:
                self.assertTrue(r["public_url"].startswith("https://github.com/Shtenco/"),r["name"])

    def test_known_boundaries(self):
        by={r["name"]:r for r in self.load()["repositories"]}
        self.assertEqual(by["midas_ai"]["lifecycle"],"CANONICAL")
        self.assertEqual(by["midas_ai"]["domain"],"TRADING")
        self.assertEqual(by["synergy_agi_trader"]["lifecycle"],"R&D")
        self.assertEqual(by["synergy_agi_trader"]["canonical_successor"],"midas_ai")
        self.assertNotEqual(by["synergy_messenger"].get("maturity"),"PRODUCTION_READY")
        self.assertEqual(by["shhts"]["lifecycle"],"ARCHIVE")

    def test_counts_are_data_derived(self):
        d=self.load()
        self.assertNotIn("total",d)
        repos=d["repositories"]
        self.assertEqual(sum(1 for r in repos if r["visibility"]=="public")+sum(1 for r in repos if r["visibility"]=="private"),len(repos))

if __name__=="__main__":
    unittest.main()
