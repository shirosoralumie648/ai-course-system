"""Small grade utilities with intentional bugs for Lab 01."""


def average_score(scores):
    """Return the average score.

    Lab 01 expects an empty score list to return 0.0.
    """
    return sum(scores) / len(scores)


def pass_rate(scores):
    """Return the fraction of scores that are passing.

    A score of 60 is passing in this course policy.
    """
    if not scores:
        return 0.0
    passing = [score for score in scores if score > 60]
    return len(passing) / len(scores)


def letter_grade(score):
    """Convert a numeric score into a letter grade."""
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"
