"""
Lab 7 - Exercise 3: Character Frequency Counter
===============================================
Maps each character in a given string to its occurrence frequency.
"""

from typing import Dict


def char_count(text: str) -> Dict[str, int]:
    """Return dictionary with characters as keys and occurrence counts as values."""
    counts: Dict[str, int] = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return counts


if __name__ == "__main__":
    assert char_count("language") == {"l": 1, "a": 2, "n": 1, "g": 2, "u": 1, "e": 1}
    assert char_count("awesome") == {"a": 1, "w": 1, "e": 2, "s": 1, "o": 1, "m": 1}
    assert char_count("me") == {"m": 1, "e": 1}

    print("Character Frequency Counter: All tests passed!")
