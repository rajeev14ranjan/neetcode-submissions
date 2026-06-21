# Valid Parenthesis String
# You are given a string s which contains only three types of characters: '(', ')' and '*'.

# Return true if s is valid, otherwise return false.

# - A string is valid if it follows all of the following rules:
# - Every left parenthesis '(' must have a corresponding right parenthesis ')'.
# - Every right parenthesis ')' must have a corresponding left parenthesis '('.
# - Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# - A '*' could be treated as a right parenthesis ')' character or a left parenthesis '(' character, or as an empty string "".
# *********** Using Stack ***********

class Solution:
    def checkValidString(self, s: str) -> bool:
        stack, star = [], []

        for i, p in enumerate(s):
            if p == "(":
                stack.append(i)
            elif p == "*":
                star.append(i)
            else:
                # close bracket
                # both are empty and nothing 
                if not stack and not star: return False

                if stack:
                    stack.pop() # use once ( to complete
                elif star:
                    star.pop() # if not, then use * if available
        
        while stack and star:
            if stack.pop() > star.pop(): return False # * is before (, can't close it
        
        return len(stack) == 0 
         

