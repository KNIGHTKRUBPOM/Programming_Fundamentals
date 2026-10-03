"""
Lab 6.1 - Exercise 3: Flatten Nested 2D List
============================================
Flattens a 2-dimensional list into a single flat list using list comprehension.
"""

from typing import Any, List


def flatten_list(matrix: List[List[Any]]) -> List[Any]:
    """Flatten 2D list into 1D list."""
    return [item for sublist in matrix for item in sublist]


if __name__ == "__main__":
    test_nested = [[1, 2], [3, 4, 5], [6]]
    flattened = flatten_list(test_nested)
    print(f"Flattened: {flattened}")
    assert flattened == [1, 2, 3, 4, 5, 6]
    print("Flatten Nested List: All tests passed!")
