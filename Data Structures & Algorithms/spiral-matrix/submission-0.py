class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        up,left = 0,0
        down,right = len(matrix),len(matrix[0])

        while left<right and up<down:
            for i in range(left,right):
                ans.append(matrix[up][i])
            up = up+1
            for i in range(up,down):
                ans.append(matrix[i][right-1])
            right = right-1
            if not (left < right and up < down):
                break
            for i in range(right-1,left-1,-1):
                ans.append(matrix[down-1][i])
            down = down -1
            for i in range(down-1,up-1,-1):
                ans.append(matrix[i][left])
            left = left + 1
        
        return ans