"""
Lab 6 - Exercise 2: Remove Duplicates
=====================================
Given a list of integers, remove duplicates while preserving the order
using list comprehension without resorting to the built-in `set`.
"""

from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    """Sort a list of numbers using bubble sort without using built-in sorted()."""
    num = arr.copy()
    n = len(num)
    for i in range(n):
        for j in range(0, n - i - 1):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
    return num


def remove_duplicate(s: List[int]) -> List[int]:
    """Remove duplicate elements from list using list comprehension."""
    return [s[i] for i in range(len(s)) if s[i] not in s[:i]]


if __name__ == "__main__":
    sample = [5, 1, 3, 3, 2, 5, 1]
    unique_items = remove_duplicate(sample)
    sorted_unique = bubble_sort(unique_items)

    print(f"Original: {sample}")
    print(f"Deduplicated: {unique_items}")
    print(f"Sorted Unique: {sorted_unique}")

    assert unique_items == [5, 1, 3, 2]
    assert sorted_unique == [1, 2, 3, 5]
    print("Remove Duplicates: All tests passed!")
