class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i == '+':
                x = stack[-1]
                y = stack[-2]
                stack.append(int(x)+int(y))
            elif i == 'D':
                x = stack[-1]
                stack.append(2*int(x))
            elif i == 'C':
                stack.pop()
            else:
                stack.append(int(i))

        return sum(stack)