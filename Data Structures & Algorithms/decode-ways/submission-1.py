class Solution:
    def numDecodings(self, s: str) -> int:
        # add 64 to the number and then do chr(number) to get alphabet

        cache = [-1]*len(s)

        def dp(s,i):
            if i== len(s):
                return 1
            if s[i] == '0':
                return  0
            if cache[i] != -1:
                return cache[i]
            res = dp(s,i+1)
            if i+1<len(s) and(s[i]=='1' or (s[i] == '2' and s[i+1]<='6')):
                res = res + dp(s,i+2)

            cache[i] = res
            return res

        ans = dp(s,0)
        return ans
