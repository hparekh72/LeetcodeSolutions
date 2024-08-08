from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        queue = deque()
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        for i in range(len(grid)):      
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append([[i, j], 0])
                    visited[i][j] = 2

        time = 0
        dRow = [-1, 1, 0, 0]
        dCol = [0, 0, -1, 1]
        while queue:
            node = queue.popleft()
            position = node[0]
            t = node[1]
            r, c = position[0], position[1]
            time = max(time, t)
            for i in range(4):
                row = r + dRow[i]
                column = c + dCol[i]

                if row >= 0 and row < len(grid) and column >= 0 and column < len(grid[0]) and grid[row][column] == 1 and visited[row][column] != 2:
                    queue.append([[row, column], t+1])
                    visited[row][column] = 2

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and visited[i][j] != 2:
                    return -1

        return time



        