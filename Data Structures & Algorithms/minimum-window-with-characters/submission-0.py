class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tdict = {}
        for i in t:
            tdict[i] = tdict.get(i, 0) + 1
        smallest = ""
        sdict = {}
        l = 0
        r = 0
        
        while r < len(s):
            sdict[s[r]] = sdict.get(s[r], 0) + 1

            while all(sdict.get(c, 0) >= tdict[c] for c in tdict):
                if smallest == "" or (r - l + 1) < len(smallest):
                    smallest = s[l:r+1]

                sdict[s[l]] -= 1
                if sdict[s[l]] == 0:
                    del sdict[s[l]]
                l += 1
            
            r = r + 1


        
        return smallest
        