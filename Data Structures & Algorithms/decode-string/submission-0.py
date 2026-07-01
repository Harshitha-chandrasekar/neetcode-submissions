class Solution:
    def decodeString(self, s: str) -> str:
        num = 0
        st = ""
        stack = []

        for char in s:
            if char.isdigit():
                num = num*10 + int(char)
            elif char == '[':
                stack.append((num,st))
                st = ""
                num = 0
            elif char == ']':
                prev_num,prev_str = stack.pop()
                st = prev_str + (st*prev_num)
            else:
                st = st+char

        return st