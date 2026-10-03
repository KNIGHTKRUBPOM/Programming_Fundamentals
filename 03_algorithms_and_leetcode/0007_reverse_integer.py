"""
LeetCode 7: Reverse Integer
===========================
Difficulty: Medium
Topics: Math

Problem:
Given a signed 32-bit integer `x`, return `x` with its digits reversed.
If reversing `x` causes the value to go outside the signed 32-bit integer range
[-2^31, 2^31 - 1], then return 0.

Complexity:
- Time Complexity: O(log10(N)) proportional to the number of decimal digits.
- Space Complexity: O(1).
"""


class Solution:
    def reverse(self, x: int) -> int:
        """Reverse 32-bit signed integer digits with overflow guard."""
        sign = -1 if x < 0 else 1
        reversed_num = int(str(abs(x))[::-1]) * sign

        int_min = -(2**31)
        int_max = 2**31 - 1

        if reversed_num < int_min or reversed_num > int_max:
            return 0
        return reversed_num


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    assert solution.reverse(123) == 321
    assert solution.reverse(-123) == -321
    assert solution.reverse(120) == 21
    assert solution.reverse(0) == 0
    assert solution.reverse(1534236469) == 0  # 32-bit overflow boundary

    print("Reverse Integer: All test cases passed!")
