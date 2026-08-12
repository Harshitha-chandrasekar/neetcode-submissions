class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False

        dicti = defaultdict(list)
        for x,y in edges:
            dicti[x].append(y)
            dicti[y].append(x)

        seen = {0}
        q = deque([0])
        while q:
            node = q.popleft()
            for conn in dicti[node]:
                if conn not in seen:
                    seen.add(conn)
                    q.append(conn)


        return len(seen) == n

