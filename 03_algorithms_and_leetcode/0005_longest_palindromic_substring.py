"""
LeetCode 5: Longest Palindromic Substring
=========================================
Difficulty: Medium
Topics: Two Pointers, String, Dynamic Programming

Problem:
Given a string `s`, return the longest palindromic substring in `s`.

Complexity:
- Time Complexity: O(N^2) using expand around center technique.
- Space Complexity: O(1) auxiliary space (excluding output).
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """Find the longest palindromic substring by expanding around each center."""
        if not s or len(s) <= 1:
            return s

        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        longest = ""
        for i in range(len(s)):
            # Odd length center (e.g. "aba")
            odd = expand_around_center(i, i)
            # Even length center (e.g. "abba")
            even = expand_around_center(i, i + 1)

            if len(odd) > len(longest):
                longest = odd
            if len(even) > len(longest):
                longest = even

        return longest


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    assert solution.longestPalindrome("babad") in ("bab", "aba")
    assert solution.longestPalindrome("cbbd") == "bb"
    assert solution.longestPalindrome("a") == "a"
    assert solution.longestPalindrome("ac") in ("a", "c")

    print("Longest Palindromic Substring: All test cases passed!")
