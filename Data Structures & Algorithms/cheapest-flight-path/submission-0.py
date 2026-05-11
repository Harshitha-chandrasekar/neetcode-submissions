class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        adj = [[]for _ in range(n)]
        for u,v,cost in flights:
            adj[u].append([v,cost])

        q = deque([(0,src,0)])
        while q:
            cost, node, stops = q.popleft()
            if stops>k:
                continue
            
            for nei, w in adj[node]:
                nextcost = cost+w
                if nextcost < prices[nei]:
                    prices[nei] = nextcost
                    q.append((nextcost, nei, stops+1))

        return prices[dst] if prices[dst] != float("inf") else -1

                    