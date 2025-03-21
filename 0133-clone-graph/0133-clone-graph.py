"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# Approach 1: Brute Force:

#1. Use a hashmap to track originals to their clones. 
#2. Traverse the original graph, visiting each node once, for each node just clone it's value without the neighbors.
#3. Traverse the original graph again , visiting each node once, for each node find it''s clone and set the original's neighbors clones as the clone's neighbors.
#4. return oldToNew[node]

# Approach 2: Optimal:
# TC: O(V + E) (dfs or bfs traversal)
# SC: O(V) (dictionary and recursion call stack)


from typing import Optional
# class Solution:
#     def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
#         oldToNew = {} # Map which stores "Old node address: New Node address"

#         def dfs(node):
#             if node in oldToNew:
#                 return oldToNew[node]

#             copyNode = Node(node.val)
#             oldToNew[node] = copyNode

#             for neighbor in node.neighbors:
#                 copyNode.neighbors.append(dfs(neighbor))

#             return copyNode

#         if node:
#             return dfs(node)
#         else:
#             return None



class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # If give node is None
        if node == None:
            return None

        queue = deque()
        oldToNew = {} # Map which stores "Old node address: New Node address"
        
        # Putting given node in the queue
        queue.append(node)

        # Map the old node to the new(copy) node
        oldToNew[node] = Node(node.val)

        while queue:
            old_node = queue.popleft() # Current Node

            # Traverse the Neighbours of old_node (current node)
            for neighbor in old_node.neighbors:
                # If Neighbour is Not in Map
                if neighbor not in oldToNew:
                    oldToNew[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                # Linking
                oldToNew[old_node].neighbors.append(oldToNew[neighbor])

        return oldToNew[node]

        # Approach 3: Pythonic way
        # return copy.deepcopy(node)
