# Min Stack
# Design a stack class that supports the push, pop, top, and getMin operations.
# - MinStack() initializes the stack object.
# - void push(int val) pushes the element val onto the stack.
# - void pop() removes the element on the top of the stack.
# - int top() gets the top element of the stack.
# - int getMin() retrieves the minimum element in the stack.
# Each function should run in O(1) time.

class MinStack:
    def __init__(self):
        self.minstack = []
        self.minsofar = [] # monotonic increasing deque

    def push(self, val: int) -> None:
        self.minstack.append(val)

        minval = val if len(self.minsofar) == 0 else min(self.minsofar[-1], val)
        self.minsofar.append(minval)


    def pop(self) -> None:
        self.minsofar.pop()
        return self.minstack.pop()

    def top(self) -> int:
        return self.minstack[-1]

    def getMin(self) -> int:
        return self.minsofar[-1]

        
