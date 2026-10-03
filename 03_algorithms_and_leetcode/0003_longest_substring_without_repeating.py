"""
LeetCode 3: Longest Substring Without Repeating Characters
==========================================================
Difficulty: Medium
Topics: Hash Table, String, Sliding Window

Problem:
Given a string `s`, find the length of the longest substring without repeating characters.

Complexity:
- Time Complexity: O(N) where N is the length of the string (two pointers / sliding window).
- Space Complexity: O(min(N, M)) where M is the size of the character set.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Find max non-repeating substring length using sliding window."""
        char_index_map = {}
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            # If char was seen within the current window, move left pointer forward
            if char in char_index_map and char_index_map[char] >= left:
                left = char_index_map[char] + 1

            char_index_map[char] = right
            max_len = max(max_len, right - left + 1)

        return max_len


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3  # "abc"
    assert solution.lengthOfLongestSubstring("bbbbb") == 1     # "b"
    assert solution.lengthOfLongestSubstring("pwwkew") == 3    # "wke"
    assert solution.lengthOfLongestSubstring("au") == 2        # "au"
    assert solution.lengthOfLongestSubstring("") == 0

    print("Longest Substring Without Repeating Characters: All test cases passed!")
