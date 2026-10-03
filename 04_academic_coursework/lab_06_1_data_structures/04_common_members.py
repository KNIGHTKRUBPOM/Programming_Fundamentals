"""
Lab 6.1 - Exercise 4: Common List Members
=========================================
Extracts members from the first list that are also present in the second list.
"""

from typing import Any, List


def common_member(list1: List[Any], list2: List[Any]) -> List[Any]:
    """Return elements in list1 that are also members of list2."""
    return [item for item in list1 if item in list2]


if __name__ == "__main__":
    l1 = [1, 2, 3, 4, 5]
    l2 = [3, 4, 5, 6, 7]
    assert common_member(l1, l2) == [3, 4, 5]
    assert common_member(["a", "b"], ["c", "d"]) == []

    print("Common List Members: All tests passed!")
