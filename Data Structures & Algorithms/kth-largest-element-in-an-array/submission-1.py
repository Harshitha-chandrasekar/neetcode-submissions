class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        negn = [-1*n for n in nums]
        heapq.heapify(negn)
        while k-1>0:
            k -= 1
            heapq.heappop(negn)

        return -1*heapq.heappop(negn)
