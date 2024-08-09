# TC: O(N * M) + O(4 * N * M) + O(N * M) ~ O(N * M)
# SC: O(N * M) (queue) + O(N * M) (visited) ~ O(N * M)

from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        queue = deque()
        for r in range(rows):       # TC: O(N * M)
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append([[r, c], 0])
                    visited[r][c] = 2

        time = 0
        # Up, Down, Left, Right
        dRow = [-1, 1, 0, 0]
        dCol = [0, 0, -1, 1]
        while queue:
            node = queue.popleft()
            position, t = node[0], node[1]
            r, c = position[0], position[1]

            time = t
            for i in range(4):    # TC: O(4 * N * M)
                row = r + dRow[i]
                col = c + dCol[i]

                if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] in [0, 2] or visited[row][col] == 2:
                    continue
                else:
                    queue.append([[row, col], t + 1])
                    visited[row][col] = 2

        
        for r in range(rows):  # TC: O(N * M)
            for c in range(cols):
                if grid[r][c] == 1 and visited[r][c] != 2:
                    return -1
        
        return time


    



        



        