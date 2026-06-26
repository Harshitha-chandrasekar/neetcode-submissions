class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        prefix = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r>0 and c>0:
                    prefix[r][c] = prefix[r-1][c] + prefix[r][c-1] + matrix[r][c] - prefix[r-1][c-1]
                elif r>0:
                    prefix[r][c] = prefix[r-1][c] + matrix[r][c]
                elif c>0:
                    prefix[r][c] = prefix[r][c-1] + matrix[r][c]
                else:
                    prefix[r][c] = matrix[r][c]
        self.prefix = prefix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.prefix[row2][col2]
        if row1 > 0:
            ans -= self.prefix[row1-1][col2]
        if col1 > 0:
            ans -= self.prefix[row2][col1-1]
        if row1 > 0 and col1 > 0:
            ans += self.prefix[row1-1][col1-1]
            
        return ans

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)