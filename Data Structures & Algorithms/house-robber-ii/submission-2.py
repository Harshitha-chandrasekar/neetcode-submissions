class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        def solve(i,e):
            if i >e:
                return 0
            if cache[i]!=-1:
                return cache[i]

            cache[i] = max(solve(i+1,e),nums[i]+solve(i+2,e))
            return cache[i]

        cache = [-1]*n
        ans1 = solve(0,n-2)
        cache = [-1]*n
        ans2 = solve(1,n-1)
        return max(ans1,ans2)