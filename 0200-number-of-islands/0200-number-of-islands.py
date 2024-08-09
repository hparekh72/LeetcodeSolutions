# TC: O(N^2) + (4 * N * M) 
# SC: O(N^2)(visited) + O(N^2)(queue in bfs) O(N + M) (recursive call stack in dfs)

class Solution:

    def dfs(self, grid, r, c, row, col, visited):
        # Base Case
        if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] == "0" or visited[r][c] == 1:
            return
        
        visited[r][c] = 1 # Mark as visited

        # Travel horizontally or vertically
        self.dfs(grid, r - 1, c, row, col, visited) # Up
        self.dfs(grid, r, c + 1, row, col, visited) # Right
        self.dfs(grid, r + 1, c, row, col, visited) # Down
        self.dfs(grid, r, c - 1, row, col, visited) # Left

    def bfs(self, grid, row_index, column_index, row, col, visited):
        queue = deque([(row_index, column_index)])
        visited[row_index][column_index] = 1

        # Up, Down, Left, Right
        dRow = [-1, 1, 0, 0] 
        dColumn = [0, 0, -1, 1]


        while queue:
            r, c = queue.popleft()

            for i in range(4):
                row_index = r + dRow[i]
                column_index = c + dColumn[i]

                if row_index < 0 or column_index < 0 or row_index >= row or column_index >= col or grid[row_index][column_index] == '0' or visited[row_index][column_index] == 1:
                    continue
                else:
                    queue.append((row_index, column_index))
                    visited[row_index][column_index] = 1

            


    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = [[0 for _ in range(col)] for _ in range(row)]
        res = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and visited[r][c] == 0:
                    # self.dfs(grid, r, c, row, col, visited)
                    self.bfs(grid, r, c, row, col, visited)
                    res += 1

        return res

        