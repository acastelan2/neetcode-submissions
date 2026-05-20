class MinStack:

    def __init__(self):
        self.stack = []
        self.min_elements = [float('inf')]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.min_elements[-1]:
            self.min_elements.append(val)
        
    def pop(self) -> None:
        if self.stack[-1] == self.min_elements[-1]:
            self.min_elements.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_elements[-1]
