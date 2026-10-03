"""
Lab 6 - Exercise 7: Count Negative Numbers
==========================================
Counts the number of negative integers present in a space-delimited string of numbers.
"""


def count_negative_numbers(numbers_str: str) -> int:
    """Return count of negative values in a space-separated number string."""
    return sum(1 for token in numbers_str.split() if int(token) < 0)


if __name__ == "__main__":
    assert count_negative_numbers("1 2 -3 4 -5") == 2
    assert count_negative_numbers("-1 -2 -3 -4 -5") == 5
    assert count_negative_numbers("1 2 3 4 5") == 0
    assert count_negative_numbers("0 0 0 0 0") == 0

    print("Count Negative Numbers: All tests passed!")
