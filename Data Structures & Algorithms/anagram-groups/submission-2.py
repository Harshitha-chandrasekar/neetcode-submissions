class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            s = "".join(sorted(i))
            res[s].append(i)
        return list(res.values())
        
        