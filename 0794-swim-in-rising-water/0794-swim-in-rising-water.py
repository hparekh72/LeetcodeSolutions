# Brute Force: Try out all possible ways, and return the least time possible to reach the bottom right square
# TC: O(4 ^ (n * n))
# SC: O(m * n) (maximum depth of the recursion tree) 

# Optimal: Modified Dijkstra Algorithm (Greedy Approach) (BFS and MinHeap)
# TC: O(4 * n * n * log n) ~ O(n^2 logn)
# SC: O(n * n) (visited and minHeap)

# class Solution:
#     def swimInWater(self, grid: List[List[int]]) -> int:
#         rows = len(grid)
  
#         visited = set()
#         visited.add((0, 0)) # Mark this position as visited

#         minHeap = []
#         heapq.heappush(minHeap, (0, 0, 0)) # Distance, r, c

#         leastTime = 0
#         while minHeap:
#             dist, r, c = heapq.heappop(minHeap)
#             visited.add((r, c))
        
#             leastTime = max(leastTime, grid[r][c])

#             if r == rows - 1 and c == cols - 1:
#                 return leastTime

#             dRow = [-1, 1, 0, 0]
#             dCol = [0, 0, -1, 1]
#             for i in range(4):
#                 row = r + dRow[i]
#                 col = c + dCol[i]
#                 if row >= 0 and row < rows and col >= 0 and col < cols and (row, col) not in visited:
#                     heapq.heappush(minHeap, (grid[row][col], row, col))


                    
# Optimal: Modified Dijkstra Algorithm (Greedy Approach) (BFS and MinHeap)
# TC: O(4 * n * n * log n) ~ O(n^2 logn)
# SC: O(n * n) (visited and minHeap)

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
  
        visited = set()
        visited.add((0, 0)) # Mark this position as visited

        minHeap = []
        heapq.heappush(minHeap, (grid[0][0], 0, 0)) # time/max-height, r, c

        while minHeap:
            time, r, c = heapq.heappop(minHeap)
        
            if r == n - 1 and c == n - 1:
                return time

            dRow = [-1, 1, 0, 0]
            dCol = [0, 0, -1, 1]
            for i in range(4):
                row = r + dRow[i]
                col = c + dCol[i]
                if row >= 0 and row < n and col >= 0 and col < n and (row, col) not in visited:
                    visited.add((row, col))
                    heapq.heappush(minHeap, (max(time, grid[row][col]), row, col))









        