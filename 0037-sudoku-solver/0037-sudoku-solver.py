# Time Complexity: O(9(n ^ 2)), in the worst case, for each cell in the n^2 board, we have 9 possible numbers.

# Space Complexity: O(1), since we are refilling the given board itself, there is no extra space required, so constant space complexity.



class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solveSudoku(board)

    def isValid(self, board, row, col, c):
        for i in range(9):
            if board[row][i] == c:
                return False

            if board[i][col] == c:
                return False

            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == c:
                return False

        return True


    def solveSudoku(self, board):

        for i in range(len(board)):
            for j in range(len(board[0])):

                if board[i][j] == ".":
                    for c in "123456789":
                        if self.isValid(board, i, j, c):
                            board[i][j] = c

                            if self.solveSudoku(board):
                                return True
                            else:
                                board[i][j] = "." # Backtrack

                    return False
        return True

    

        