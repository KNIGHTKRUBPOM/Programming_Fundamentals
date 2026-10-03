"""
LeetCode 56: Merge Intervals
============================
Difficulty: Medium
Topics: Array, Sorting

Problem:
Given an array of `intervals` where intervals[i] = [start_i, end_i],
merge all overlapping intervals, and return an array of the non-overlapping
intervals that cover all the intervals in the input.

Complexity:
- Time Complexity: O(N log N) sorting the intervals by start time.
- Space Complexity: O(N) to store merged output intervals.
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """Sort intervals by start coordinate and merge contiguous overlaps."""
        if not intervals:
            return []

        # Sort intervals by their start point
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for current in intervals[1:]:
            previous = merged[-1]
            if current[0] <= previous[1]:
                # Overlap: extend the end of the previous interval
                previous[1] = max(previous[1], current[1])
            else:
                # No overlap: append current interval
                merged.append(current)

        return merged


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    assert solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [
        [1, 6],
        [8, 10],
        [15, 18],
    ]
    assert solution.merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert solution.merge([[1, 6], [3, 7], [10, 11]]) == [[1, 7], [10, 11]]
    assert solution.merge([[1, 4], [2, 3]]) == [[1, 4]]

    print("Merge Intervals: All test cases passed!")
