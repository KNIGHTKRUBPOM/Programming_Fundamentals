"""
Lab 6.1 - Exercise 1: Filter English Letters and Spaces
======================================================
Removes non-alphabetical characters (except spaces) from a string.
"""


def only_english(text: str) -> str:
    """Filter string to only retain English alphabetical characters and spaces."""
    return "".join(char for char in text if char.isalpha() or char.isspace())


if __name__ == "__main__":
    assert only_english("Hello, World!") == "Hello World"
    assert only_english("This is a test.") == "This is a test"
    assert only_english("12345") == ""
    assert only_english("abcABC123") == "abcABC"
    assert only_english("!@#$%^&*()") == ""

    print("Filter English Letters: All tests passed!")
