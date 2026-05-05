class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        pivot = 0
        while(l<r):
            pivot = l + ((r-l)//2)
            if nums[pivot] > nums[r]:
                l = pivot + 1
            else:
                r = pivot

        pivot = l

        if target >= nums[pivot] and target <= nums[-1]:
            l, r = pivot, len(nums) - 1
        else:
            l, r = 0, pivot - 1

        while(l<=r):
            mid = l + ((r-l)//2)
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

        return -1