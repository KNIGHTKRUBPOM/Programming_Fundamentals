"""
Lab 6 - Exercise 6: Filter Negative Numbers from 2D Lists
=========================================================
Removes all negative integers from each sublist within a 2D matrix.
"""

from typing import List


def filter_negative_numbers(matrix: List[List[int]]) -> List[List[int]]:
    """Return a new matrix containing only non-negative integers (>= 0)."""
    return [[val for val in row if val >= 0] for row in matrix]


if __name__ == "__main__":
    t1 = [[1, -3, 2], [-8, 5], [-1, -4, -3]]
    t2 = [[0, -1, -2], [3, 4, -5], [-6, 7]]
    t3 = [[-10, -20, -30], [-40, -50], [-60]]

    assert filter_negative_numbers(t1) == [[1, 2], [5], []]
    assert filter_negative_numbers(t2) == [[0], [3, 4], [7]]
    assert filter_negative_numbers(t3) == [[], [], []]

    print("Filter Negative Numbers: All tests passed!")
