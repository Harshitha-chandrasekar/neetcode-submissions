class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1set = {}
        s2set = {}
        window_len = len(s1)
        
        for i in range(window_len):
            s1set[s1[i]] = s1set.get(s1[i], 0) + 1
            s2set[s2[i]] = s2set.get(s2[i], 0) + 1
            
        if s1set == s2set:
            return True
            
        l = 0
        for r in range(window_len, len(s2)):
            s2set[s2[r]] = s2set.get(s2[r], 0) + 1
            s2set[s2[l]] -= 1
            if s2set[s2[l]] == 0:
                del s2set[s2[l]]
            l += 1
            if s1set == s2set:
                return True
                
        return False