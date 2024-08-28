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
#3. Traverse the original graph again, visiting each node once, for each node find it''s clone and set the original's neighbors clones as the clone's neighbors.
#4. return oldToNew[node]

# Approach 2: Optimal:
# TC: O(V + E) (dfs traversal)
# SC: O(V) (dictionary and recursion call stack)


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copyNode = Node(node.val)
            oldToNew[node] = copyNode

            for neighbor in node.neighbors:
                copyNode.neighbors.append(dfs(neighbor))

            return copyNode

        if node:
            return dfs(node)
        else:
            return None

        # Approach 3: Pythonic way
        # return copy.deepcopy(node)
