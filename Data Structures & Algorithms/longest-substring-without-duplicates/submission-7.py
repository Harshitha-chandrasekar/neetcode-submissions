class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        l = 0
        r = 1
        ans = 1
        while r<=len(s):
            substr = s[l:r]
            if substr[-1] in substr[:-1]:
                l = l+1
            else:
                ans = max(ans,len(substr))
                r = r +1

        return ans