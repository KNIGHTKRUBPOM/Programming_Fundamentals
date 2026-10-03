"""
Element Frequency Counter
=========================
Topics: Hash Table, Dictionary, Counting

Problem:
Count the frequency of each unique element within an input collection,
returning a key-value mapping of element to occurrence count.

Complexity:
- Time Complexity: O(N) single pass over input list.
- Space Complexity: O(K) where K is the number of distinct elements.
"""

from typing import Any, Dict, List


def count_frequencies(elements: List[Any]) -> Dict[Any, int]:
    """Map unique elements to their corresponding occurrence count."""
    frequencies: Dict[Any, int] = {}
    for item in elements:
        frequencies[item] = frequencies.get(item, 0) + 1
    return frequencies


if __name__ == "__main__":
    test_list = [0, 80, 1, 2, 2, 3, 4, 5, 5, 7]
    result = count_frequencies(test_list)

    print(f"Input: {test_list}")
    print(f"Frequencies: {result}")

    assert result[0] == 1
    assert result[80] == 1
    assert result[2] == 2
    assert result[5] == 2

    print("Element Frequency Counter: All test cases passed!")
