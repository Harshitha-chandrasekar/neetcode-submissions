class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False
        
        c1 = {}
        c2 = {}

        for i in range(len(s1)):
            c1[s1[i]] = c1.get(s1[i], 0) + 1
            c2[s2[i]] = c2.get(s2[i], 0) + 1

        if c1 == c2:
            return True

        for i in range(len(s1),len(s2)):

            c2[s2[i]] = c2.get(s2[i], 0) + 1

            left_char = s2[i - len(s1)]
            c2[left_char] -= 1
            if c2[left_char] == 0:
                del c2[left_char]

            if c1 == c2:
                return True

        return False
