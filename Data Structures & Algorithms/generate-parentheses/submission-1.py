class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def bt(s,opened,close):
            if opened == n and close == n:
                res.append(s)
                return

            if opened<n and opened>=close:
                bt(s+'(',opened+1,close)
            if close<n:
                bt(s+')',opened,close+1)

        bt('',0,0)
        return res