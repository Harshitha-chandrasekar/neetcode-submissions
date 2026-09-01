class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n+1)]
        dp[0][0] = 1

        for i in range(n):
            for s,c in dp[i].items():
                dp[i+1][s + nums[i]] +=c
                dp[i+1][s - nums[i]] +=c
            
        return dp[n][target]