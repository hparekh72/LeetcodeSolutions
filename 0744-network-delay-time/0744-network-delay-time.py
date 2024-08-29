# Dijkstra Algorithm
# TC: O(V + E) (adjacency list creation) + O(ElogV) (minHeap) ~ O(V + E). Here V -> n, E -> len(times)
# SC: O(V + E) (adjacency list creation) + O(V) (minHeap) ~ O(V + E)

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # Create adjacency list
        adjList = {i:[] for i in range(n + 1)} # 1 based indexing
        for u, v, w in times:
            adjList[u].append([v, w])

        distance = [float('inf')] * (n + 1) # 1 based indexing
        distance[k] = 0 # Travel time(distance) is 0 for source node

        minHeap = []
        heapq.heappush(minHeap, (0, k))

        while minHeap:
            time, node = heapq.heappop(minHeap)

            for neighbor, neighborTime in adjList[node]:
                if neighborTime + time < distance[neighbor]:
                    distance[neighbor] = neighborTime + time
                    heapq.heappush(minHeap, (distance[neighbor], neighbor))

        print(distance)
        minTime = -1
        for i in range(1, n + 1):
            if distance[i] == float('inf'):
                return -1
            
            if distance[i] > minTime:
                minTime = distance[i]

        return minTime

