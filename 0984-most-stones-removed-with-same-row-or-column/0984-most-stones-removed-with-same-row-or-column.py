# Approach 1: Using DFS
# Intution: The core idea of this solution is to treat each stone as a node in a graph, with edges connecting nodes if they share the same row or column. The goal is to identify and count the connected components (clusters of stones directly or indirectly connected). Each connected component can have all but one of its stones removed, such that there's still a way to trace from any stone in the component to any other without crossing a removed stone. Thus, the number of stones that can be removed is the total number of stones minus the number of these connected components.


# TC: O(n ^ 2) + (V + E)
# SC: O(n ^ 2) + O(n) (visited array)

class Solution:

    def dfs(self, src, adjList, visited):
        visited.add(src)

        for neighbor in adjList[src]:
            if neighbor not in visited:
                self.dfs(neighbor, adjList, visited)

    def removeStones(self, stones: List[List[int]]) -> int:

        # Create adjacency list
        n = len(stones)
        adjList = defaultdict(list)

        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    adjList[i].append(j)
                    adjList[j].append(i)

        visited = set()
        numOfComponents = 0
        for i in range(n):
            if i not in visited:
                numOfComponents += 1
                self.dfs(i, adjList, visited)

        return n - numOfComponents

