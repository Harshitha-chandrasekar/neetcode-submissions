class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        for i in range(len(equations)):
            numer,demon = equations[i]
            value = values[i]
            graph[numer][demon] = value
            graph[demon][numer] = 1.0/value

        def bfs(start,target):
            if start not in graph or target not in graph:
                return -1.0

            q = deque([(start,1.0)])
            visited = set([start])
            while q:
                currnode, currprod = q.popleft()
                if currnode == target:
                    return currprod

                for neighbor, weight in graph[currnode].items():
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append((neighbor, currprod * weight))
            return -1.0

        ans = []
        for a,b in queries:
            ans.append(bfs(a,b))
        return ans