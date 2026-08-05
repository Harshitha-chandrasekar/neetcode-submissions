class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        delta = [0]*(n+1)
        for a,b in trust:
            delta[a]-=1
            delta[b]+=1

        for i in range(n+1):
            if delta[i] == n-1:
                return i

        return -1