"""
Lab 6 - Exercise 5: Count Character in Strings
==============================================
Counts the occurrences of a specified character within each string in a list.
"""

from typing import List


def count_char_in_strings(strings: List[str], target_char: str) -> List[int]:
    """Return a list containing the frequency count of target_char for each string."""
    return [s.count(target_char) for s in strings]


if __name__ == "__main__":
    assert count_char_in_strings(["abba", "babana", "ann"], "a") == [2, 3, 1]
    assert count_char_in_strings(["apple", "banana", "cherry"], "a") == [1, 3, 0]
    assert count_char_in_strings(["dog", "cat", "fish"], "z") == [0, 0, 0]
    assert count_char_in_strings(["@home", "#hash", "space "], "#") == [0, 1, 0]

    print("Count Character in Strings: All tests passed!")
