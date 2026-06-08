class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n ==0:
            return 0
        if n == 1:
            return nums[0]

        def solve(houses):
            size = len(houses)
            cache = [-1]*size

            def dp(val):
                if val >= size:
                    return 0
                if cache[val]!=-1:
                    return cache[val]

                rob = houses[val] + dp(val+2)
                skip = dp(val+1)
                cache[val] = max(rob,skip)
                return cache[val]


            return dp(0)

        soln1 = solve(nums[:-1])
        soln2 = solve(nums[1:])
        return max(soln1,soln2)
