"""
LeetCode 202: Happy Number
==========================
Difficulty: Easy
Topics: Hash Table, Math, Two Pointers

Problem:
A happy number is a number defined by the following process:
- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
- Those numbers for which this process ends in 1 are happy.
Return true if `n` is a happy number, and false if not.

Complexity:
- Time Complexity: O(log N) for digit square transitions.
- Space Complexity: O(log N) visited set to detect cycles.
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        """Determine if a number reaches 1 via sum of square digits cycle detection."""
        def sum_of_squared_digits(num: int) -> int:
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum_of_squared_digits(n)

        return n == 1


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    assert solution.isHappy(19) is True  # 1^2 + 9^2 = 82 -> ... -> 1
    assert solution.isHappy(2) is False   # Cycles endlessly
    assert solution.isHappy(7) is True
    assert solution.isHappy(1) is True

    print("Happy Number: All test cases passed!")
