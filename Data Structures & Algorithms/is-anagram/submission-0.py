class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h = {}
        for i in s:
            if i in h:
                h[i] = h[i] + 1
            else:
                h[i] = 1
        h2 = {}
        for i in t:
            if i in h2:
                h2[i] = h2[i] + 1
            else:
                h2[i] = 1
        if h == h2:
            return True
        return False
        