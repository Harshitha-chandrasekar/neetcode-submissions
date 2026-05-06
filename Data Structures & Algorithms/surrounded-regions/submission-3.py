class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row = len(board)
        col = len(board[0])
        visited = set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(r,c):
            if(r<0 or c<0 or r>=row or c>=col or (r,c) in visited or board[r][c] == 'X'):
                return

            visited.add((r,c))
                

            for dr,dc in directions:
                nr,nc = dr+r,dc+c
                dfs(nr,nc)

            return




            

        for r in range(row):
            if board[r][0] == 'O':
                dfs(r,0)
            if board[r][col-1] == 'O':
                dfs(r,col-1)
        for c in range(col):
            if board[0][c] == 'O':
                dfs(0,c)
            if board[row-1][c] == 'O':
                dfs(row-1,c)

        for i in range(row):
            for j in range(col):
                if (i,j) not in visited and board[i][j] == 'O':
                    board[i][j] = 'X'

        return
                