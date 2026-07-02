from collections import Counter
class FreqStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> int:
        c = dict(Counter(self.stack))
        max_freq = max(c.values())
        for i in range(len(self.stack)-1,-1,-1):
            if c[self.stack[i]] == max_freq:
                return self.stack.pop(i)

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()