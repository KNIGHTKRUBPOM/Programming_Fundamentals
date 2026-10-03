"""
Lab 6.1 - Exercise 2: Element-wise List Addition
================================================
Adds corresponding elements of two lists with equal length.
"""

from typing import List


def add_two_lists(list1: List[int], list2: List[int]) -> List[int]:
    """Return element-wise addition of two lists if lengths match, else empty list."""
    if len(list1) == len(list2):
        return [list1[i] + list2[i] for i in range(len(list1))]
    return []


if __name__ == "__main__":
    assert add_two_lists([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
    assert add_two_lists([10, -5], [-10, 5]) == [0, 0]
    assert add_two_lists([1, 2], [3]) == []

    print("Element-wise List Addition: All tests passed!")
