# Using Dijkstra (Greedy + BFS using priority queue)

# TC: O(4 * N * M) * log(N * M) 
# N * M are the total cells, for each of which we also check 4 adjacent nodes for the minimum effort and additional log(N * M) for insertion-deletion operations in a priority queue 

# SC: O(N * M) 
# Distance matrix containing N * M cells + priority queue in the worst case containing all the nodes (N * M)

# Note: We are using Priority Queue as we require Path with Minimum Effort

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])

        minHeap = []
        heapq.heappush(minHeap, [0, 0, 0]) # maximum difference, row, col

        # Note: Can also use a visited array here istead of distance (Mark the position as visite when we pop the node out of the heap in case of visited array)
        distance = [[float('inf') for _ in range(COLS)] for _ in range(ROWS)]
        distance[0][0] = 0

        # 4 directions(up, down, left, right)
        dRow = [-1, 1, 0, 0]
        dCol = [0, 0, -1, 1]
        while minHeap:
            diff, r, c = heapq.heappop(minHeap)
            
            if r == ROWS - 1 and c == COLS - 1:
                return diff

            for i in range(4):
                newR = r + dRow[i]
                newC = c + dCol[i]

                if newR >= 0 and newR < ROWS and newC >= 0 and newC < COLS:
                    newDiff = max(diff, abs(heights[r][c] - heights[newR][newC]))

                    if newDiff < distance[newR][newC]:
                        distance[newR][newC] = newDiff
                        heapq.heappush(minHeap, [newDiff, newR, newC])

                



            




