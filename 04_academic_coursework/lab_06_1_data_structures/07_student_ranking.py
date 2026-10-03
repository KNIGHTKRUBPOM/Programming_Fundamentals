"""
Lab 6.1 - Exercise 7: Student Ranking
=====================================
Calculates a student's leaderboard rank based on scores in descending order.
"""

from typing import List, Tuple, Union


def find_rank(student_scores: List[List[Union[str, float]]], target_student_id: str) -> int:
    """Return 1-indexed rank of student based on score sorted in descending order."""
    sorted_scores = sorted(student_scores, key=lambda x: x[1], reverse=True)

    for index, (student_id, score) in enumerate(sorted_scores):
        if student_id == target_student_id:
            return index + 1
    return -1


if __name__ == "__main__":
    scores = [
        ["65015001", 87.25],
        ["65015002", 77.00],
        ["65015003", 82.50],
        ["65015004", 69.75],
        ["65015005", 66.00],
    ]
    assert find_rank(scores, "65015001") == 1
    assert find_rank(scores, "65015003") == 2
    assert find_rank(scores, "65015004") == 4
    assert find_rank(scores, "99999999") == -1

    print("Student Ranking: All tests passed!")
