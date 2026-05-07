class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n
        count = 0

        def dfs(edge):
            for ne in adj[edge]:
                if not visited[ne]:
                    visited[ne] = True
                    dfs(ne)

        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                count = count + 1

        return count