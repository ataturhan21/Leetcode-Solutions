import importlib.util
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/build_index.py"
SPEC = importlib.util.spec_from_file_location("build_index", SCRIPT)
indexer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(indexer)


class IndexTests(unittest.TestCase):
    def test_numeric_order_and_language_filters(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in ["10-zeta/zeta.py", "2-alpha/alpha.py", "2-alpha/query.sql", "2-alpha/solve.js", "scripts/tool.py"]:
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("raise RuntimeError('solution files must never execute')\n")
            indexes = indexer.build_indexes(root)
            python = indexes[Path("docs/solutions-python.md")]
            self.assertLess(python.index("2-alpha"), python.index("10-zeta"))
            self.assertNotIn("tool.py", python)
            self.assertNotIn("query.sql", python)
            self.assertIn("query.sql", indexes[Path("docs/solutions-sql.md")])
            self.assertIn("solve.js", indexes[Path("docs/solutions-javascript.md")])

    def test_nested_paths_and_markdown_characters(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "1-a[b]|c" / "nested folder" / "solution [v2].py"
            path.parent.mkdir(parents=True)
            path.touch()
            text = indexer.build_indexes(root)[Path("docs/solutions-python.md")]
            self.assertIn(r"1-a\[b\]\|c", text)
            self.assertIn("../1-a%5Bb%5D%7Cc/nested%20folder/solution%20%5Bv2%5D.py", text)

    def test_empty_tree_and_repeat_runs_are_deterministic(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            first = indexer.build_indexes(root)
            self.assertEqual(first, indexer.build_indexes(root))
            self.assertEqual(len(first), 3)
            self.assertTrue(all(text.endswith("\n") for text in first.values()))


if __name__ == "__main__":
    unittest.main()
