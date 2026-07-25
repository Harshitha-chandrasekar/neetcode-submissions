class Solution:
    def totalNQueens(self, n: int) -> int:
        def placeQ(i,cols,rightdiag,leftdiag,cur,count):
            n = len(cols)
            if i == n:
                count = count+1
                return count

            for j in range(n):
                if cols[j] or rightdiag[i+j] or leftdiag[i-j+n-1]:
                    continue

                cols[j] = 1
                rightdiag[i+j] = 1
                leftdiag[i-j+n-1] = 1
                cur[i][j] = 'Q'
                count = placeQ(i+1,cols,rightdiag,leftdiag,cur,count)
                cols[j] = 0
                rightdiag[i+j] = 0
                leftdiag[i-j+n-1] = 0
                cur[i][j] = '.'
            return count

        cols = [0]*n
        leftd = [0]*(n*2)
        rightd = [0]*(n*2)
        cur = [['.']*n for _ in range(n)]            
        count = 0
        return placeQ(0,cols,rightd,leftd,cur,count)