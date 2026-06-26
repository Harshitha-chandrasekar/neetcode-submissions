class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowhash = defaultdict(list)
        colhash = defaultdict(list)
        square = defaultdict(list)
        for i in range(9):
            for j in range(9):
                n = board[i][j]
                if n!='.':
                    if n in rowhash[i]:
                        return False
                    else:
                        rowhash[i].append(n)
                    if n in colhash[j]:
                        return False
                    else:
                        colhash[j].append(n)
                    sq_ind = (i//3)*3 + (j//3)
                    if n in square[sq_ind]:
                        return False
                    else:
                        square[sq_ind].append(n)
        return True