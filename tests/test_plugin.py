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
        self.assertEqual(result["skills"], 6)
        self.assertEqual(result["commands"], 6)
        self.assertEqual(result["chase_source_cards"], 34)
        self.assertEqual(result["graph_nodes"], 101)
        self.assertEqual(result["graph_edges"], 362)

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

    def test_learning_habit_and_graph_skills(self):
        habit = (ROOT / "plugins" / "avada-product-training" / "skills" / "learning-habit-builder" / "SKILL.md").read_text()
        graph = (ROOT / "plugins" / "avada-product-training" / "skills" / "brain-graph" / "SKILL.md").read_text()
        self.assertIn("five or fewer", habit)
        self.assertIn("artifact", habit.lower())
        self.assertIn("graph.json", graph)
        self.assertIn("retrieval map, not doctrine", graph)

        run = subprocess.run(
            [sys.executable, str(ROOT / "plugins" / "avada-product-training" / "scripts" / "query_graph.py"), "path", "Product operator method", "Metric diagnosis tree"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=True,
        )
        result = json.loads(run.stdout)
        self.assertTrue(result["ok"])
        self.assertEqual(result["hops"], 1)
        self.assertEqual(result["path"][1]["edge"]["relation"], "curated")

    def test_brand_question_chain(self):
        text = (ROOT / "plugins" / "avada-product-training" / "skills" / "brand-case-clinic" / "SKILL.md").read_text()
        self.assertIn("ask these **one at a time**", text)
        self.assertIn("1. **Mission:**", text)
        self.assertIn("7. **Economics:**", text)
        self.assertIn("12. **Revision:**", text)
        self.assertIn("require evidence or calculation", text)


if __name__ == "__main__":
    unittest.main()
