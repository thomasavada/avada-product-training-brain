import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PluginContractTest(unittest.TestCase):
    def test_validator(self):
        run = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "validate.py")],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=True,
        )
        result = json.loads(run.stdout.strip())
        self.assertTrue(result["ok"])
        self.assertEqual(result["skills"], 4)
        self.assertEqual(result["commands"], 4)
        self.assertEqual(result["chase_source_cards"], 34)

    def test_teach_me_does_not_dump_answer_first(self):
        text = (ROOT / "plugins" / "avada-product-training" / "skills" / "teach-me-ecom" / "SKILL.md").read_text()
        self.assertIn("Never reveal the answer", text)
        self.assertIn("learner predicts", text)
        self.assertIn("Coverage is not learning", text)

    def test_source_boundaries(self):
        text = (ROOT / "plugins" / "avada-product-training" / "skills" / "avada-product-training-brain" / "SKILL.md").read_text()
        self.assertIn("Blume skincare", text)
        self.assertIn("Bloom Nutrition", text)
        self.assertIn("được gửi trước Session 3", text)
        self.assertIn("vendor case claim", text)

    def test_curated_learning_resources(self):
        text = (ROOT / "plugins" / "avada-product-training" / "knowledge" / "sources" / "learning-resources.md").read_text()
        self.assertIn("42uhZYnyEXU", text)
        self.assertIn("6IAgiYdUlXM", text)
        self.assertIn("ZDPlZBK6Oac", text)
        self.assertGreaterEqual(text.count("https://"), 10)
        self.assertGreaterEqual(text.count("Artifact"), 10)


if __name__ == "__main__":
    unittest.main()
