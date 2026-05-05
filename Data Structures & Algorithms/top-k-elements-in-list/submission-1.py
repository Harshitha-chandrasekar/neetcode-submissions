class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = defaultdict(int)
        for i in nums:
            l[i] +=1

        ans = sorted(l,key = l.get, reverse=True)
        return ans[:k]
