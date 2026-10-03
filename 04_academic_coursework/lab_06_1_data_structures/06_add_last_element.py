"""
Lab 6.1 - Exercise 6: Append Last Element Sum
=============================================
Adds the last element of the list to each preceding element in the list.
"""

from typing import List


def add_last_element(lst: List[int]) -> List[int]:
    """Return each preceding element added with the last element."""
    if len(lst) <= 1:
        return []
    return [item + lst[-1] for item in lst[:-1]]


if __name__ == "__main__":
    assert add_last_element([1, 2, 3, 4]) == [5, 6, 7]
    assert add_last_element([10, 20, 5]) == [15, 25]

    print("Append Last Element Sum: All tests passed!")
