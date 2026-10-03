"""
Lab 6.1 - Exercise 5: Remove Vowels
===================================
Filters out English vowels (a, e, i, o, u) from a given string.
"""


def remove_vowels(text: str) -> str:
    """Return a string with all uppercase and lowercase vowels removed."""
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    return "".join(char for char in text if char not in vowels)


if __name__ == "__main__":
    assert remove_vowels("Hello World") == "Hll Wrld"
    assert remove_vowels("Python") == "Pythn"
    assert remove_vowels("AEIOU") == ""

    print("Remove Vowels: All tests passed!")
