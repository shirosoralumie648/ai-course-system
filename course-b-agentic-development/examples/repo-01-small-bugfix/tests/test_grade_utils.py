import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from grade_utils import average_score, letter_grade, pass_rate


class GradeUtilsTests(unittest.TestCase):
    def test_average_regular_scores(self):
        self.assertEqual(average_score([80, 90, 100]), 90)

    def test_average_empty_list_returns_zero(self):
        self.assertEqual(average_score([]), 0.0)

    def test_pass_rate_counts_sixty_as_passing(self):
        self.assertAlmostEqual(pass_rate([59, 60, 80]), 2 / 3)

    def test_pass_rate_empty_list_returns_zero(self):
        self.assertEqual(pass_rate([]), 0.0)

    def test_letter_grade_boundaries(self):
        self.assertEqual(letter_grade(90), "A")
        self.assertEqual(letter_grade(80), "B")
        self.assertEqual(letter_grade(70), "C")
        self.assertEqual(letter_grade(60), "D")
        self.assertEqual(letter_grade(59), "F")


if __name__ == "__main__":
    unittest.main()
