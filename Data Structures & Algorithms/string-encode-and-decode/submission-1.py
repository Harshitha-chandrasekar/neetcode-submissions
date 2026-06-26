class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            l = len(s)
            encoded = encoded + "#"+str(l)+"#"+s
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        ans = []
        while i<len(s):
            j = i+1
            while s[j]!='#':
                j = j+1
            l = int(s[i+1:j])
            ans.append(s[j+1:j+1+l])
            i = j+1+l
        return ans
