from collections import defaultdict

class Solution:
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
        
    #     def checkValidity(x, y, board):  # Checks the x-axis 
    #         hashSet = set()
    #         for i in range(len(board[0])):
    #             if board[x][i] == ".":
    #                 continue
                
    #             if board[x][i] not in hashSet:
    #                 hashSet.add(board[x][i])
    #             else:
    #                 return False


    #         hashSet = set()
    #         for i in range(len(board)): # Checks the y-axis 
    #             if board[i][y] == ".":
    #                 continue
                
    #             if board[i][y] not in hashSet:
    #                 hashSet.add(board[i][y])
    #             else:
    #                 return False


    #         m = (x // 3) * 3 
    #         n = (y // 3) * 3
    #         hashSet = set()
    #         for i in range(m, m+3): # Checks the sub-box
    #             for j in range(n, n+3):
    #                 if board[i][j] == ".":
    #                     continue
                
    #                 if board[i][j] not in hashSet:
    #                     hashSet.add(board[i][j])
    #                 else:
    #                     return False

    #         return True


    #     for i in range(len(board)):
    #         for j in range(len(board[0])):
    #             if board[i][j] != ".":
    #                 continue

    #             if checkValidity(i, j, board) == False:
    #                 return False
    #     return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r // 3, c // 3)]:
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c]) 

        return True