class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        perlength = total//k
        piles = [0] * k
        nums.sort(reverse=True)

        def dfs(i):
            if i == len(nums):
                return True

            for j in range(k):
                if piles[j]+nums[i] <= perlength:
                    piles[j] += nums[i]
                    if dfs(i+1):
                        return True

                    piles[j] -= nums[i]

                if piles[j] == 0:
                    break

            return False

        return dfs(0)