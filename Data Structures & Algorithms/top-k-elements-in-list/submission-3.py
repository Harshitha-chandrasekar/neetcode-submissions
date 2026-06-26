class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            if n in count:
                count[n] = count[n]+1
            else:
                count[n] = 1
        c = dict(sorted(count.items(),key=lambda item: item[1],reverse=True))
        return list(c.keys())[:k]