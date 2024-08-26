# TC: O(V + 2E) (dfs) + O(V + 2E) (adjacency list) + O()
# SC: O(V + 2E) (adjacency list) + O(V) (visited, discoveryTime, low and dfs recursion stack space)

# Intuition:
# This approach uses a Depth-First Search (DFS) to identify "bridges" in an undirected graph.
# A bridge is an edge removing which increases the number of connected components.
# We apply Tarjan's algorithm to find these bridges:
# - Discovery Time records when a node is first visited.
# - Low-link Value is the smallest discovery time reachable from a node.
# The critical condition for an edge (u, v) to be a bridge is:
#   If the lowest point reachable from 'v' is still higher than the discovery time of 'u'.
# This means 'v' cannot reach 'u' or any ancestor of 'u' by any other path except through 'u'.


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # Create adjacency list
        graph = defaultdict(list)

        for edge in connections: # TC: O(V + 2E)
            u = edge[0]
            v = edge[1]
            graph[u].append(v)
            graph[v].append(u)

        # Initialize helper structures
        visited = set()
        timer = [0]
        discoveryTime = [0] * n # Discovery Time (Starting Time)
        low = [0] * n # Lowest possible discovery time (Earliest possible time)
        res = []  # Bridges

        self.dfs(0, -1, timer, graph, visited, discoveryTime, low, res)

        return res

    def dfs(self, node, parent, timer, graph, visited, discoveryTime, low, res): # TC: O(V + 2E)
        visited.add(node)
        discoveryTime[node] = low[node] = timer[0]
        timer[0] = timer[0] + 1 # Increment the timer for the next node


        for neighbor in graph[node]:
            if neighbor == parent:   # Skip the edge to parent to avoid cycle in undirected graph
                continue
            
            if neighbor not in visited:
                self.dfs(neighbor, node, timer, graph, visited, discoveryTime, low, res)

                # Update low value of node after DFS completion of neighbor
                low[node] = min(low[node], low[neighbor])

                # Check if the current edge is a critical connection
                if low[neighbor] > discoveryTime[node]: # Bridge condition
                    res.append([node, neighbor])

            else:
                # Back edge
                # Update low value if neighbor is already visited and not the parent
                low[node] = min(low[node], discoveryTime[neighbor])

