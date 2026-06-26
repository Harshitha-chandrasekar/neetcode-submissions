class Solution:
    def isPalindrome(self, s: str) -> bool:
        pals = ""
        for c in s:
            if c.isalnum():
                pals = pals + c.lower()

        return pals == pals[::-1]