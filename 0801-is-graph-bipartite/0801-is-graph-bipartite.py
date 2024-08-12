# TC: O(N) + O(N + 2E)
# SC: O(N) (queue in bfs or recursive stack space in dfs) + O(N) (color array) ~ O(N)


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1] * len(graph)
        for i in range(len(graph)):
            if color[i] == -1:
                # if self.bfs(i, graph, color) == False:
                #     return False

                if self.dfs(i, 0, graph, color) == False:
                    return False
        return True

    def bfs(self, start, graph, color): # TC: O(N + 2E)
        queue = deque()
        queue.append(start)
        color[start] = 0

        while queue:
            node = queue.popleft()

            for neighbor in graph[node]:
                # If the neighbor(adjacent) node is not yet colored, we will give the opposite color of the node
                if color[neighbor] == -1:
                    queue.append(neighbor)
                    color[neighbor] = not color[node]
                # If the neighbor(adjacent) node is having the same color as the node, then someone did color it on some other path
                elif color[neighbor] == color[node]:
                    return False

        return True

    def dfs(self, node, color, graph, colorArr):
        colorArr[node] = color

        for neighbor in graph[node]:
            if colorArr[neighbor] == -1:
                if self.dfs(neighbor, not color, graph, colorArr) == False:
                    return False
            elif colorArr[neighbor] == color:
                return False
            
        return True


        