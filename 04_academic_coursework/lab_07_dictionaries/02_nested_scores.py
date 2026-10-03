"""
Lab 7 - Exercise 2: Nested Student Gradebook
============================================
Nested dictionary structure storing multiple students and their respective course scores.
"""

from typing import Dict


def add_score(
    gradebook: Dict[str, Dict[str, float]],
    student_id: str,
    subject: str,
    score: float,
) -> Dict[str, Dict[str, float]]:
    """Insert or update course score for a student."""
    subject_norm = subject.lower()
    if student_id not in gradebook:
        gradebook[student_id] = {}
    gradebook[student_id][subject_norm] = score
    return gradebook


def calc_overall_average(gradebook: Dict[str, Dict[str, float]]) -> str:
    """Calculate overall average across all students and all subjects."""
    total_score = 0.0
    subject_count = 0

    for student_id, subjects in gradebook.items():
        for sub, score in subjects.items():
            total_score += score
            subject_count += 1

    if subject_count == 0:
        return "0.00"
    return f"{total_score / subject_count:.2f}"


if __name__ == "__main__":
    records = {}
    add_score(records, "65010001", "python", 50)
    add_score(records, "65010001", "calculus", 60)
    add_score(records, "65010001", "digi", 30)
    add_score(records, "65010002", "Digi", 40)

    overall_avg = calc_overall_average(records)
    print(f"Gradebook: {records}")
    print(f"Overall Average: {overall_avg}")

    # (50 + 60 + 30 + 40) / 4 = 180 / 4 = 45.00
    assert overall_avg == "45.00"
    print("Nested Gradebook: All tests passed!")
