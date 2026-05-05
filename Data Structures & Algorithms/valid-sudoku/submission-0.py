class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(0,9):
            # rows and columns
            l1 = []
            l2 = []


            for j in range(0,9):
                if board[i][j] !=".":
                    l1.append(board[i][j])
                if board[j][i] !=".":
                    l2.append(board[j][i])
            if sorted(l1) != sorted(list(set(l1))): 
                return False
            if sorted(l2) != sorted(list(set(l2))):
                return False

        check = [[] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                
                
                index = (int(j/3)) * 3 + int(i/3)
                if board[i][j] != '.':
                    check[index].append(board[i][j])
        
        for i in range(9):
            l = check[i]
            if sorted(l) != sorted(list(set(l))): 
                return False
            



        return True
