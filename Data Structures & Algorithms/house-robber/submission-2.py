class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = [-1]*n

        def df(val):
            if val>=n:
                return 0
            if cache[val] != -1:
                return cache[val]
            cache[val] = max(df(val+1),nums[val]+df(val+2))
            return cache[val]

        return df(0)