# Intution: All possible paths starting from a node are going to end at some terminal node unless there exists a cycle and the paths return back to themselves. So, the intuition is to figure out the nodes which are neither a part of a cycle nor connected to the cycle.

# Note:
# We can eliminate the check array and just use if(pathVisited[i] == 0) to get the safe nodes and use the absolute same code as cycle detection in directed graph, just add this in end:

#     safeNodes = []
#     for i in range(V):
#         if path[i] == 0:
#                 safeNodes.append(i)

#         return safeNodes


# TC: O(N) + O(N + E)
# SC: O(3N) + O(N) (dfs recursive stack space) ~ O(N)

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        return self.topologicalSort(graph)     

    #     V = len(graph)
    #     visited, pathVisited, check = [0] * V, [0] * V, [0] * V

    #     for i in range(V):
    #         if visited[i] == 0:
    #             self.dfs(i, graph, visited, pathVisited, check)

    #     safeNodes = []
    #     for i in range(V):
    #         if check[i] == 1:
    #             safeNodes.append(i)

    #     return safeNodes
        
           
    # def dfs(self, node, graph, visited, pathVisited, check): # TC: O(N + E)
    #     visited[node] = 1
    #     pathVisited[node] = 1

    #     # Traverse for adjacent nodes
    #     for neighbor in graph[node]:
    #         # When the node is not visited
    #         if visited[neighbor] == 0:
    #             if self.dfs(neighbor, graph, visited, pathVisited, check) == True:
    #                 return True
            
    #         # If the node has been previously visited but it has to be visited on the same path
    #         elif pathVisited[neighbor]:
    #             return True

    #     # Ie the node is neither a part of a cycle nor connected to the cycle.
    #     check[node] = 1
    #     pathVisited[node] = 0
    #     return False

# Intution Of Topological Sort(BFS implementation):

# Initially, the terminal nodes are those with an outdegree of zero. However, after reversing the edges, the terminal nodes become those with an indegree of zero. Thus, we can apply Kahn's algorithm to identify all nodes connected to these terminal nodes, which have a linear dependency or are on a path leading to a terminal node. If a node is part of a cycle or leads to a cycle, that path cannot lead to a terminal node, as each node in that path will have a cyclic dependency.

# TC: O(V + E)
# SC: O(V)



    def topologicalSort(self, graph):

        reverseAdjList = defaultdict(list)

        # Reverse the edges of all nodes and calculate the indegree

        n = len(graph)
        reversed_graph = [[] for _ in range(n)]
        indegree = [0] * n

        for i in range(n):
            for neighbor in graph[i]:
                reversed_graph[neighbor].append(i)
                indegree[i] += 1

        # Topological Sort
        queue = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        res = []
        while queue:
            node = queue.popleft()
            res.append(node)

            for neighbor in reversed_graph[node]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return sorted(res)





        
                





        