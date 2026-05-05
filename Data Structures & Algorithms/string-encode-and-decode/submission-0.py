class Solution:

    def encode(self, strs):
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + '#' + s
        return encoded

    def decode(self, s):
        strs = []
        i = 0
        
        while i < len(s):
            j = i
            
            while s[j] != '#':
                j += 1
            
            num = int(s[i:j])
            word = s[j+1 : j+1+num]
            strs.append(word)
            
            i = j + 1 + num
        
        return strs