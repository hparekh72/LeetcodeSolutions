# BFS and minHeap
# TC: O(4 * m * n) ~ O(m * n)
# SC: O(m * n) (visited and minHeap)

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        visited.add((0, 0)) # Mark this position as visited

        minHeap = []
        heapq.heappush(minHeap, (0, 0, 0)) # Distance, r, c

        leastTime = 0
        while minHeap:
            dist, r, c = heapq.heappop(minHeap)
            visited.add((r, c))
        
            leastTime = max(leastTime, grid[r][c])

            if r == rows - 1 and c == cols - 1:
                return leastTime

            dRow = [-1, 1, 0, 0]
            dCol = [0, 0, -1, 1]
            for i in range(4):
                row = r + dRow[i]
                col = c + dCol[i]
                if row >= 0 and row < rows and col >= 0 and col < cols and (row, col) not in visited:
                    heapq.heappush(minHeap, (grid[row][col], row, col))


                    












        