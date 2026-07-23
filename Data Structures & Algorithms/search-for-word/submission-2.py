class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        x = 0

        def bt(i,j,x):
            if x == len(word):
                return True
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j]!=word[x]:
                return False

            temp = board[i][j]
            board[i][j] = '#'
            found = (bt(i+1,j,x+1) or
                    bt(i-1,j,x+1) or 
                    bt(i,j+1,x+1) or
                    bt(i,j-1,x+1))

            board[i][j] = temp
            return found

        for i in range(len(board)):
            for j in range(len(board[0])):
                if bt(i,j,0):
                    return True

        return False
            

