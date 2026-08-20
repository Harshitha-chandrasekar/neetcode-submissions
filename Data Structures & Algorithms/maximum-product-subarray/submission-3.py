class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maximum = [float('-inf')]*n
        minimum = [float('inf')]*n
        global_max = nums[0]

        maximum[0] = nums[0]
        minimum[0] = nums[0]

        for i in range(1,n):
            curr_max = max(maximum[i-1]*nums[i],minimum[i-1]*nums[i],nums[i])
            curr_min = min(maximum[i-1]*nums[i],minimum[i-1]*nums[i],nums[i])

            maximum[i] = max(curr_max,curr_min)
            minimum[i] = min(curr_max,curr_min)

            global_max = max(global_max,maximum[i],minimum[i])

        return global_max