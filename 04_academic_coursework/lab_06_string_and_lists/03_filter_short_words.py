"""
Lab 6 - Exercise 3: Filter Short Words
======================================
Filters a sentence and retains only words with length strictly less than 5 characters.
"""


def find_short_words(sentence: str) -> str:
    """Return space-joined string of words that have length strictly less than 5."""
    short_words = [word for word in sentence.split() if len(word) < 5]
    return " ".join(short_words)


if __name__ == "__main__":
    t1 = "A total of 16 playable characters!"
    t2 = "The quick brown fox jumps over the lazy dog"
    t3 = "Python is a great programming language"

    print(find_short_words(t1))
    print(find_short_words(t2))
    print(find_short_words(t3))

    assert find_short_words(t1) == "A of 16"
    assert find_short_words(t2) == "The fox over the lazy dog"
    print("Filter Short Words: All tests passed!")
