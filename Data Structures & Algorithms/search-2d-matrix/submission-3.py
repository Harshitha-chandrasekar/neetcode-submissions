class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix) -1
        cols = len(matrix[0]) -1

        x = 0
        y = rows
        m = 0
        while x<= y :
            m =(x+y)//2
            if matrix[m][0]<= target <= matrix[m][-1]:
                break
            elif matrix[m][0] > target:
                y = m-1
            else:
                x = m+1

        r = m

        x = 0
        y = cols
        while x<=y:
            m = (x+y)//2
            if matrix[r][m] == target:
                return True
            elif matrix[r][m]> target:
                y = m -1 
            else:
                x = m+1

        return False
