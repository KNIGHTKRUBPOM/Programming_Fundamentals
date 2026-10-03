"""
Lab 6.1 - Exercise 8: Majority Element
======================================
Finds the majority element in a list (an element appearing more than n/2 times).
Returns "Not Found" if no majority element exists.
"""

from typing import Any, List, Union


def more_than_half(numbers: List[Any]) -> Union[Any, str]:
    """Find element appearing more than len(numbers) / 2 times."""
    threshold = len(numbers) / 2
    for item in set(numbers):
        if numbers.count(item) > threshold:
            return item
    return "Not Found"


if __name__ == "__main__":
    assert more_than_half([4, 5, 5]) == 5
    assert more_than_half([10, 5, 5, 3, 5]) == 5
    assert more_than_half([4, 5, 5, 10]) == "Not Found"
    assert more_than_half([2, 4, 2, 4, 2, 4]) == "Not Found"

    print("Majority Element: All tests passed!")
