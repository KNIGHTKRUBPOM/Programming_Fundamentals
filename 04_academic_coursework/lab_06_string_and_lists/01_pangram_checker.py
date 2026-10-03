"""
Lab 6 - Exercise 1: Pangram Checker
===================================
A pangram is a sentence containing every single letter of the English alphabet
at least once (e.g. 'The quick brown fox jumps over the lazy dog').
"""

import string


def is_pangram(input_string: str) -> bool:
    """Return True if input_string contains all 26 English alphabet letters."""
    alphabet = set(string.ascii_lowercase)
    cleaned = set(input_string.lower())
    return alphabet.issubset(cleaned)


if __name__ == "__main__":
    test_1 = "The quick brown fox jumps over the lazy dog dog"
    test_2 = "Hello World"
    test_3 = "Pack my box with five dozen liquor jugs"

    assert is_pangram(test_1) is True
    assert is_pangram(test_2) is False
    assert is_pangram(test_3) is True

    print(f"'{test_1}' -> Pangram: {is_pangram(test_1)}")
    print(f"'{test_2}' -> Pangram: {is_pangram(test_2)}")
    print(f"'{test_3}' -> Pangram: {is_pangram(test_3)}")
    print("Pangram Checker: All tests passed!")
