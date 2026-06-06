# Evaluate Reverse Polish Notation
# You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

# Return the integer that represents the evaluation of the expression.

# The operands may be integers or the results of other operations.
# The operators include '+', '-', '*', and '/'.
# Assume that division between integers always truncates toward zero.

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens: return 0
        stack = []

        for s in tokens:
            if s == "*":
                b,a = stack.pop(), stack.pop()  # evluated from left - to - right
                stack.append(a*b)
            elif s == "+":
                b,a = stack.pop(), stack.pop()
                stack.append(a+b)
            elif s == "-":
                b,a = stack.pop(), stack.pop()
                stack.append(a-b)
            elif s == "/":
                b,a = stack.pop(), stack.pop()
                stack.append(int(a/b)) # had to use for - division between integers always truncates toward zero.
            else:
                stack.append(int(s))

        return int(stack[0])

        