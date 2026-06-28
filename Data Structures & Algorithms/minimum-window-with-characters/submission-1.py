class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        count_t = {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1
        need = len(count_t)
        have = 0
        window_counts = {}
        res = (float("inf"), -1, -1)
        l = 0
        for r in range(len(s)):
            c = s[r]
            window_counts[c] = window_counts.get(c, 0) + 1
            if c in count_t and window_counts[c] == count_t[c]:
                have += 1
            while have == need:
                if (r - l + 1) < res[0]:
                    res = (r - l + 1, l, r)
                left_char = s[l]
                window_counts[left_char] -= 1
                if left_char in count_t and window_counts[left_char] < count_t[left_char]:
                    have -= 1
                l += 1
        window_len, start, end = res
        return s[start : end + 1] if window_len != float("inf") else ""