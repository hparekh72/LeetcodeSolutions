# TC: O(4 * m * n) (dfs) + O(m * n)
# SC: O(m * n) (visited array) + O(m * n) (recursive stack space)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = len(board)
        cols = len(board[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        
        # Traverse first row and last row
        for i in range(cols):
            # First row
            if board[0][i] == "O" and visited[0][i] == 0:
                self.dfs(0, i, board, visited)
            
            # Last row
            if board[rows - 1][i] == "O" and visited[rows - 1][i] == 0:
                self.dfs(rows - 1, i, board, visited)

        # Traverse first column and last column
        for i in range(rows):
            # First Column
            if board[i][0] == "O" and visited[i][0] == 0:
                self.dfs(i, 0, board, visited)

            # Last Column
            if board[i][cols - 1] == "O" and visited[i][cols - 1] == 0:
                self.dfs(i, cols - 1, board, visited)

        # Traversing the board except the boundaries
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if board[r][c] == "O" and visited[r][c] == 0:
                    board[r][c] = "X"
        
    def dfs(self, r, c, board, visited): # TC: O(4 * m * n)
        # Base Case
        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] == "X" or visited[r][c] == 1:
            return 

        visited[r][c] = 1

        self.dfs(r - 1, c, board, visited) # Down
        self.dfs(r + 1, c, board, visited) # Up
        self.dfs(r, c - 1, board, visited) # Left
        self.dfs(r, c + 1, board, visited) # Right











        