# Dijkstra (Graph BFS Implementation)
# TC: O(8 * n * n) ~ O(n^2)
# SC: O(n * n) (distance) + O(n * n) (queue) ~ O(n^2)


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # Check if the starting or ending cell is blocked.
        if grid[0][0] != 0 or grid[rows-1][cols-1] != 0:
            return -1


        queue = deque()

        queue.append([1, (0, 0)]) # Distance, Position
        distance = [[float('inf') for _ in range(rows)] for _ in range(cols)]

        # 8 directions
        dRow = [-1, 1, 0, 0, -1, 1, -1, 1]
        dCol = [0, 0, -1, 1, -1, 1, 1, -1]

        while queue:
            dist, position = queue.popleft()
            print(dist, position)
            r = position[0]
            c = position[1]

            # If we reach the bottom-right corner, return the distance.
            if r == rows - 1 and c == cols - 1:
                return dist

            for i in range(8):
                row = r + dRow[i]
                col = c + dCol[i]

                if row >= 0 and row < rows and col >= 0 and col < cols and grid[row][col] == 0:
                    if dist + 1 < distance[row][col]:
                        distance[row][col] = dist + 1
                        queue.append([distance[row][col], (row, col)])

        return -1

                







        
        