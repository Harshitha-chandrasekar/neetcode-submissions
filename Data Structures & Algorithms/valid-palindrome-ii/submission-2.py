class Solution:
    def validPalindrome(self, s: str) -> bool:
        deleted = 0 
        
        def check(deleted,s,l,r):
            if l >= r:
                return True
            if s[l]!=s[r]:
                if deleted!=0:
                    return False
                deleted = deleted+1
                return check(deleted,s,l+1,r) or check(deleted,s,l,r-1)
            return check(deleted,s,l+1,r-1)

        return check(deleted,s,0,len(s)-1)    