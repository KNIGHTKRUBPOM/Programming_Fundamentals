"""
LeetCode 20: Valid Parentheses
==============================
Difficulty: Easy
Topics: String, Stack

Problem:
Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Complexity:
- Time Complexity: O(N) single pass through the string.
- Space Complexity: O(N) stack for tracking open brackets.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        """Validate bracket ordering using a Last-In-First-Out (LIFO) stack."""
        stack = []
        matching = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in matching.values():
                stack.append(char)
            elif char in matching:
                if not stack or stack.pop() != matching[char]:
                    return False
            else:
                return False

        return len(stack) == 0


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    assert solution.isValid("()") is True
    assert solution.isValid("()[]{}") is True
    assert solution.isValid("(]") is False
    assert solution.isValid("([)]") is False
    assert solution.isValid("{[]}") is True
    assert solution.isValid("]") is False

    print("Valid Parentheses: All test cases passed!")
