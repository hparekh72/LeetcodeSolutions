# Prims Algorithm (Intution: Greedy approach)
# TC: O(ElogE). Here E represents no. of edges which is n^2 in worst case. ie. O(n^2(logn))
# SC: O(n^2) (For adjacency list and minHeap) + O(n) (visited array) ~ O(n^2)


class Solution:

    def manhattanDistance(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        # Create Adjacency List
        adjList = {i:[] for i in range(n)} # i: list of [cost, node]
        for i in range(n):
            x1, y1, = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = self.manhattanDistance(x1, y1, x2, y2)
                adjList[i].append([dist, j])
                adjList[j].append([dist, i])

        # Prim's Algorithm
        visited = set()

        minHeap = []
        heapq.heappush(minHeap, [0, 0])

        minCost = 0
        while minHeap:
            cost, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            
            visited.add(node)
            minCost += cost

            for neighborCost, neighbor in adjList[node]:
                if neighbor not in visited:
                    heapq.heappush(minHeap, [neighborCost, neighbor])
        
        return minCost




        
        

        

        

            

