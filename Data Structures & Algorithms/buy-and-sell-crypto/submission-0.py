class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        buy = prices[0]
        sell = prices[0]
        for i in prices:
            buy = min(i,buy)
            prof = max(prof,i - buy)

        return prof