class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {'}':'{',
                        ']':'[',
                        ')':'('}

        for c in s:
            if c not in dictionary.keys():
                stack.append(c)
            else:
                if not stack:
                    return False
                if stack[-1] == dictionary[c]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False