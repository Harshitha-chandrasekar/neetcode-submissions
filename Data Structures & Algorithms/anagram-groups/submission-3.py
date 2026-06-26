class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alph = defaultdict(list)
        for word in strs:
            sorteds = ''.join(sorted(word))
            alph[sorteds].append(word)
        return list(alph.values())