class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adjlist = defaultdict(list)
        for a,b in edges:
            adjlist[a].append(b)
            adjlist[b].append(a)

        ans = []
        min_overall_h = float('inf')

        def minfromn(n,h,seen):
            mini = h
            for neighbour in adjlist[n]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    mini = max(mini,minfromn(neighbour,h+1,seen))
                    seen.remove(neighbour)
            return mini
            

        for i in range(n):
            seen = set([i])
            currh = minfromn(i,0,seen)

            if currh < min_overall_h:
                min_overall_h = currh
                ans = [i]
            
            elif currh == min_overall_h:
                ans.append(i)

        return ans