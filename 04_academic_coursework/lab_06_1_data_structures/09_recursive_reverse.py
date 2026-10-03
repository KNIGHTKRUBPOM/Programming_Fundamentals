"""
Lab 6.1 - Exercise 9: Recursive String Reversal
===============================================
Reverses a string using recursive decomposition.
"""


def reverse_string_recursive(text: str) -> str:
    """Recursively reverse a string by taking the last character and recursing."""
    if not text:
        return ""
    return text[-1] + reverse_string_recursive(text[:-1])


if __name__ == "__main__":
    assert reverse_string_recursive("desserts") == "stressed"
    assert reverse_string_recursive("hello") == "olleh"
    assert reverse_string_recursive("") == ""
    assert reverse_string_recursive("a") == "a"

    print("Recursive String Reversal: All tests passed!")
