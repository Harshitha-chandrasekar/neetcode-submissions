class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        def bt(i,res,scentence):
            if i == len(s):
                res.append(" ".join(scentence))
                return

            for j in range(i,len(s)):
                if s[i:j+1] not in wordDict:
                    continue
                word = s[i:j+1]
                scentence.append(word)
                bt(j+1,res,scentence)
                scentence.pop()

        res = []
        bt(0,res,[])
        return res