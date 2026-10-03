"""
Lab 6 - Exercise 4: Recursive List Sum
======================================
Calculates the sum of elements in a list using recursion.
"""

from typing import List


def find_sum(numbers: List[int], n: int) -> int:
    """Calculate the sum of the first n elements in numbers using recursion."""
    if n <= 0:
        return 0
    if n == 1:
        return numbers[0]
    return numbers[n - 1] + find_sum(numbers, n - 1)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = find_sum(nums, len(nums))
    print(f"Sum of {nums} = {result}")
    assert result == 55
    print("Recursive List Sum: All tests passed!")
