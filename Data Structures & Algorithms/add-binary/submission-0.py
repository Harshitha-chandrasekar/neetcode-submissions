class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        a,b = a[::-1],b[::-1]# reverse
        for i in range(max(len(a),len(b))):
            dA = ord(a[i]) - ord('0') if i < len(a) else 0
            dB = ord(b[i]) - ord('0') if i < len(b) else 0

            total = dA+dB+carry
            char = str(total%2)
            res = char+res
            carry = total//2

        if carry:
            res = "1"+res

        return res