class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []
        def backtrack(opencount, closedcount,string):
            if len(string) == 2*n:
                result.append(string)
                return

            if opencount < n:
                backtrack(opencount + 1, closedcount, string + "(")

            if closedcount < opencount:
                backtrack(opencount, closedcount + 1, string + ")")
            

        backtrack(0,0,"")
        return result