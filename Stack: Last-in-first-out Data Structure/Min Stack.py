class MinStack:

    def __init__(self):
        self.minima = None
        self.s = []

    def push(self, val: int) -> None:
        if self.minima == None:
            self.minima = val
        elif val < self.minima:
            self.minima = val
        self.s.insert(0, val)

    def pop(self) -> None:
        self.s.pop(0)
        if len(self.s) > 0:
            self.minima = min(self.s)
        else:
            self.minima = None

    def top(self) -> int:
        return self.s[0]

    def getMin(self) -> int:
        return self.minima