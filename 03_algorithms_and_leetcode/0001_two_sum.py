"""
LeetCode 1: Two Sum
===================
Difficulty: Easy
Topics: Array, Hash Table

Problem:
Given an array of integers `nums` and an integer `target`, return indices
of the two numbers such that they add up to `target`.
You may assume that each input would have exactly one solution, and you
may not use the same element twice.

Complexity:
- Time Complexity: O(N) single pass through the array.
- Space Complexity: O(N) hash map to store seen values.
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Find indices of two numbers that add up to target using a hash map."""
        seen = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], index]
            seen[num] = index
        return []


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]
    assert solution.twoSum([3, 3], 6) == [0, 1]

    print("Two Sum: All test cases passed successfully!")
