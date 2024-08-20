# Number of shortest paths to reach at the destination
# Using Dijkstra Algorithm

# TC: O(ElogV)
# SC: O(V + 2E) (graph) + O(V) (distance and ways array) Here, n = V

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
        MOD = 10**9 + 7

        # Create a adjacency list as only edges(roads array) is given
        graph = defaultdict(list)
        for edge in roads:
            graph[edge[0]].append([edge[1], edge[2]])
            graph[edge[1]].append([edge[0], edge[2]])


        minHeap = []
        heapq.heappush(minHeap, [0, 0]) # Distance, Node
        
        distance = [float('inf')] * n
        distance[0] = 0 # Mark the distance(time) to reach the start node as 0

        ways = [0] * n
        ways[0] = 1 # We can reach the start node in 1 way

        while minHeap:
            dist, node = heapq.heappop(minHeap)

            for neighbor in graph[node]:
                adjacentNode = neighbor[0]
                edgeWeight = neighbor[1]

                # This is the first time we are reaching with this short distance
                if dist + edgeWeight < distance[adjacentNode]:
                    distance[adjacentNode] = dist + edgeWeight
                    heapq.heappush(minHeap, [distance[adjacentNode], adjacentNode])
                    ways[adjacentNode] = ways[node]
                elif dist + edgeWeight == distance[adjacentNode]:
                    ways[adjacentNode] = (ways[adjacentNode] + ways[node]) % MOD
                
        return ways[n - 1]
