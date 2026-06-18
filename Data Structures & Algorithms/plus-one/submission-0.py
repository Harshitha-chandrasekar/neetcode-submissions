class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        carry = 1
        for i in range(len(digits)):
            n = digits[i]+carry
            if n<10:
                digits[i] = n
                carry = 0
                break
            else:
                digits[i] = n%10
                carry = n//10

        if carry!=0:
            digits.append(carry)

        digits.reverse()
        return digits