# Can be solve using Floyd Warshall and Dijkstra Algorithm (since no negative weights) algorithm

# Floyd Warshall Algorithm
# TC: O(n ^ 2) + O(n ^ 2) + O(n ^ 3) + O(n ^ 2) ~ O(n ^ 3)
# SC: O(n ^ 2)

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Create distance matrix
        distance = [[float('inf') for _ in range(n)] for _ in range(n)] 

        for edge in edges:
            distance[edge[0]][edge[1]] = edge[2]
            distance[edge[1]][edge[0]] = edge[2]

        for i in range(n): # Distance to the node itself will be 0
            distance[i][i] = 0

        # Floyd Warshall Algorithm

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

        # Now the distance matrix stores the shortest paths between all pairs of nodes in a weighted graph

        cityNo = -1
        leastNeighbors = float('inf')

        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and distance[i][j] <= distanceThreshold:
                    count += 1

            if count <= leastNeighbors:
                leastNeighbors = count
                cityNo = i

        return cityNo




        


        