class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        tar_times = len(nums)//3
        times = {}
        for n in nums:
            if n in times:
                times[n] = times[n]+1
            else:
                times[n] = 0
        ans = []
        for key,value in times.items():
            if value>=tar_times:
                ans.append(key)
        return ans