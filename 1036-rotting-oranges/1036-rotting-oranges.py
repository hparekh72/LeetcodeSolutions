# TC: O(N * M) + O(4 * N * M) + O(N * M) ~ O(N * M)
# SC: O(N * M) (queue) + O(N * M) (visited) ~ O(N * M)

from collections import deque

# class Solution(object):
#     def orangesRotting(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """

#         rows = len(grid)
#         cols = len(grid[0])
#         visited = [[0 for _ in range(cols)] for _ in range(rows)]

#         queue = deque()
#         for r in range(rows):       # TC: O(N * M)
#             for c in range(cols):
#                 if grid[r][c] == 2:
#                     queue.append([[r, c], 0])
#                     visited[r][c] = 2

#         time = 0
#         # Up, Down, Left, Right
#         dRow = [-1, 1, 0, 0]
#         dCol = [0, 0, -1, 1]
#         while queue:
#             node = queue.popleft()
#             position, t = node[0], node[1]
#             r, c = position[0], position[1]

#             time = t
#             for i in range(4):    # TC: O(4 * N * M)
#                 row = r + dRow[i]
#                 col = c + dCol[i]

#                 if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] in [0, 2] or visited[row][col] == 2:
#                     continue
#                 else:
#                     queue.append([[row, col], t + 1])
#                     visited[row][col] = 2

        
#         for r in range(rows):  # TC: O(N * M)
#             for c in range(cols):
#                 if grid[r][c] == 1 and visited[r][c] != 2:
#                     return -1
        
#         return time


# TC: O(N * M) + O(4 * N * M) + O(N * M) ~ O(N * M)
# SC: O(N * M) (queue) + O(N * M) (visited) ~ O(N * M)

# Note: Here we are not using the visited array as we are updating within the grid. Hence, no need for a seperate visited array

class Solution(object): # BFS Traversal (Multi Source BFS )
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        ROWS, COLS = len(grid), len(grid[0])

        queue = deque()
        fresh = 0
        time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append([r, c])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]] # Right, Leftm Down, Up

        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    row = dr + r
                    col = dc + c

                    # If in bounds and fresh make rotten
                    if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] != 1:
                        continue
                    grid[row][col] = 2
                    queue.append([row, col])
                    fresh -= 1
                
            time += 1

        
        if fresh == 0:
            return time
        else:
            return -1

        

         


    



        



        