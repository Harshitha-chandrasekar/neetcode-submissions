class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        totalsum = sum(stones)
        dp = {}
        target = math.ceil(totalsum/2)

        def func(i,currtotal):
            if i == len(stones) or currtotal > target:
                return abs(currtotal - (totalsum - currtotal))
            if (i,currtotal) in dp:
                return dp[(i,currtotal)]
            dp[(i,currtotal)] = min(func(i+1,currtotal),func(i+1,currtotal+stones[i]))
            return dp[(i,currtotal)]

        return func(0,0)