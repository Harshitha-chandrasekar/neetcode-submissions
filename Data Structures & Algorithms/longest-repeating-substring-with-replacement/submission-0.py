class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxl = 1
        l = 0
        r = 0
        count = {}

        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(count.values())
            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            maxl = max(maxl, r - l + 1)
            r += 1

        return maxl