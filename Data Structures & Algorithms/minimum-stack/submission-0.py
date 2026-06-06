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

        
