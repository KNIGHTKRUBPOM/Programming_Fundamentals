"""
Lab 7 - Exercise 1: Subject Score Management
============================================
Dictionary management for student subjects, scores, and grade point average calculation.
"""

from typing import Dict


def add_score(subject_scores: Dict[str, float], subject: str, score: float) -> Dict[str, float]:
    """Add or update subject score in dictionary."""
    subject_scores[subject] = score
    return subject_scores


def calc_average_score(subject_scores: Dict[str, float]) -> str:
    """Calculate and return average score formatted to 2 decimal places."""
    if not subject_scores:
        return "0.00"
    avg = sum(subject_scores.values()) / len(subject_scores)
    return f"{avg:.2f}"


if __name__ == "__main__":
    scores = {}
    add_score(scores, "python", 50)
    add_score(scores, "calculus", 60)

    print(f"Subject scores: {scores}")
    avg = calc_average_score(scores)
    print(f"Average: {avg}")

    assert scores == {"python": 50, "calculus": 60}
    assert avg == "55.00"
    print("Subject Score Management: All tests passed!")
