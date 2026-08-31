class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp =  {}

        def func(i,buying):
            if i >= len(prices):
                return 0 
            if (i,buying) in dp:
                return dp[(i,buying)]

            skip_today = func(i+1,buying)
            if buying:
                buy = func(i+1,not buying) - prices[i]
                dp[(i,buying)] = max(buy, skip_today)
            else:
                sell = func(i+2,not buying) + prices[i]
                dp[(i,buying)] = max(sell,skip_today)

            return dp[(i,buying)]

        return func(0,True)
 
        