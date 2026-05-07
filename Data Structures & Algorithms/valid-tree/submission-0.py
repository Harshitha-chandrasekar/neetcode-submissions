class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n-1:
            return False

        adf = [[] for _ in range(n)]
        for u,v in edges:
            adf[u].append(v)
            adf[v].append(u)

        visit = set()
        def dfs(node, par):
            if node in visit:
                return False

            visit.add(node)
            for nex in adf[node]:
                if nex == par:
                    continue
                if not dfs(nex, node):
                    return False
            return True

        return dfs(0,-1) and len(visit) == n

        
