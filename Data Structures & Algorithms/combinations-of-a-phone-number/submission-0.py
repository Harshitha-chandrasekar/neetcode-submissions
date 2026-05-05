class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dictionary = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res = []

        def backtracking(index,temp):
            if len(temp) == len(digits):
                res.append(temp)
                return

            for x in dictionary[digits[index]]:
                backtracking(index+1,temp + x)

        if digits:
            backtracking(0,"")

        return res