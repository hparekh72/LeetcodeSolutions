# TC: O(N) + O(V + 2E) ~ O(N)
# SC: O(N) + O(N) (recursive stack space) ~ O(N)


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        numOfProvinces = 0
        for start_vertex in range(len(isConnected)):
            if start_vertex not in visited:
                numOfProvinces += 1
                self.dfs(start_vertex, isConnected, visited)
        
        return numOfProvinces
                


    def dfs(self, start_vertex, isConnected, visited):
        visited.add(start_vertex)

        for adjacent_vertex in range(len(isConnected)):
            if isConnected[start_vertex][adjacent_vertex] == 1 and adjacent_vertex not in visited:
                self.dfs(adjacent_vertex, isConnected, visited)
        