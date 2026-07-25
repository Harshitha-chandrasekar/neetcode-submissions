class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def placeQueens(i,cols,leftdiag,rightdiag,cur,res):
            n = len(cols)
            if i == n:
                res.append(["".join(row) for row in cur])
                return

            for j in range(n):
                if cols[j] or rightdiag[i+j] or leftdiag[i-j+n-1]:
                    continue
                
                cols[j] = 1
                rightdiag[i+j] = 1
                leftdiag[i-j+n-1] = 1
                cur[i][j]='Q'
                placeQueens(i+1,cols,leftdiag,rightdiag,cur,res)
                cols[j] = 0
                rightdiag[i+j] = 0
                leftdiag[i-j+n-1] = 0
                cur[i][j] = '.'

        cols = [0]*n
        leftdiag = [0]*(2*n)
        rightdiag = [0]*(2*n)
        cur = [['.'] * n for _ in range(n)]
        res = []

        placeQueens(0, cols, leftdiag, rightdiag, cur, res)
        return res