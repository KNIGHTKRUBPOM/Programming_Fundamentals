"""
LeetCode 14: Longest Common Prefix
==================================
Difficulty: Easy
Topics: String, Trie

Problem:
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Complexity:
- Time Complexity: O(S) where S is the sum of characters in all strings.
- Space Complexity: O(1) auxiliary memory.
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """Find the longest common prefix using vertical character scanning."""
        if not strs:
            return ""

        pivot = strs[0]
        for i, char in enumerate(pivot):
            for other_word in strs[1:]:
                # If length boundary reached or characters mismatch
                if i == len(other_word) or other_word[i] != char:
                    return pivot[:i]

        return pivot


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    assert solution.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert solution.longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert solution.longestCommonPrefix(["interspecies", "interstellar", "interstate"]) == "inters"
    assert solution.longestCommonPrefix(["throne", "throne"]) == "throne"

    print("Longest Common Prefix: All test cases passed!")
