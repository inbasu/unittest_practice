URL = "https://leetcode.com/problems/valid-parentheses/"
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false


#'()[]{}'


class Solution:
    def isValid(self, s: str) -> bool:
        opened = [""]
        parantheses = {")": "(", "]": "[", "}": "{"}
        for chr in s:
            if chr in parantheses.values():
                opened.append(chr)
            elif chr in parantheses:
                if opened[-1] != parantheses[chr]:
                    return False
                else:
                    opened.pop(-1)

        return len(opened) == 1
