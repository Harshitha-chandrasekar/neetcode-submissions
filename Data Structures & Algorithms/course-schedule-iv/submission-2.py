class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ans = []
        dicti = defaultdict(list)
        for pre,crs in prerequisites:
            dicti[pre].append(crs)
        for start,target in queries:
            q = deque([start])
            seen = set()
            visit = set()
            seen.add(start)
            while q:
                crs = q.popleft()
                for req in dicti[crs]:
                    if req not in seen:
                        seen.add(req)
                        q.append(req)
                    visit.add(req)
            if target in visit:
                ans.append(True)
            else:
                ans.append(False)
        return ans
