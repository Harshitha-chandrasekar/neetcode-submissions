class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {
            2:'abc',
            3:'def',
            4:'ghi',
            5:'jkl',
            6:'mno',
            7:'pqrs',
            8:'tuv',
            9:'wxyz'
        }

        res = []
        def bt(i,current_path):
            if i == len(digits):
                res.append(current_path)
                return

            for ch in mapping[int(digits[i])]:
                bt(i + 1, current_path + ch)

        bt(0,"")
        return res