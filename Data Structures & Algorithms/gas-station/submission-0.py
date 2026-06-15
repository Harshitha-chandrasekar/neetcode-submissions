class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        i = 0
        if sum(cost)>sum(gas):
            return -1
        tank = 0
        for i in range(n):
            flag = True
            for j in range(i,i+n):
                tank = tank+gas[j%n]-cost[(j)%n]
                if tank<0:
                    flag = False
                    tank = 0
                    break
            if flag == True:
                return i
                break
        return -1