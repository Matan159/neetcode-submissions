class MinStack:

    def __init__(self):
        self.stack = deque()
        self.minstack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minstack) == 0:
            self.minstack.append(val)
        else:
            self.minstack.append(min(self.minstack[-1], val))     

    def pop(self) -> None:
        if len(self.stack) == 0:
            return None
        self.minstack.pop()
        return self.stack.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.minstack) == 0:
            return None
        return self.minstack[-1]
