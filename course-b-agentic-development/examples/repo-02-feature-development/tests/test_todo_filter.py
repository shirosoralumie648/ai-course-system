import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from todo_filter import list_titles


class TodoFilterTests(unittest.TestCase):
    def test_list_titles_returns_all_titles_in_order(self):
        tasks = [
            {"title": "Write report", "status": "pending"},
            {"title": "Submit homework", "status": "done"},
            {"title": "Review diff", "status": "pending"},
        ]

        self.assertEqual(
            list_titles(tasks),
            ["Write report", "Submit homework", "Review diff"],
        )

    def test_list_titles_empty_list(self):
        self.assertEqual(list_titles([]), [])


if __name__ == "__main__":
    unittest.main()
