# Valid Parentheses
# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

# The input string s is valid if and only if:
# 1. Every open bracket is closed by the same type of close bracket.
# 2. Open brackets are closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.

class Solution:
    def isValid(self, s: str) -> bool:
        if not s or len(s) & 1 > 0: return False

        pair = {")": "(", "}": "{", "]": "["}
        stack = []

        for b in s:
            if b in pair: # is closing braces
                if stack and stack[-1] == pair[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)

        return not stack

        