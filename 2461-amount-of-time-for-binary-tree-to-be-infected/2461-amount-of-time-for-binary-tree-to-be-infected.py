# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # TC: O(N) + O(N) = O(N)
    # SC: O(N) + O(N) + O(N) = O(N)
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.parentsMap = {}
        startNode = [root]
        self.markParents(root, self.parentsMap, start, startNode) # Mark parent nodes and gets start node address

        # BFS traversal on all the nodes from the start node

        queue = [startNode[0]]
        
        visited = {startNode[0]: True}
        time = 0 # current level / minutes

        while queue:
            
            flag = False
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.pop(0)

                if node.left and node.left not in visited:
                    flag = True
                    queue.append(node.left)
                    visited[node.left] = True
                
                if node.right and node.right not in visited:
                    flag = True
                    queue.append(node.right)
                    visited[node.right] = True

                parentNode = self.parentsMap[node]
                if parentNode and parentNode not in visited:
                    flag = True
                    queue.append(parentNode)
                    visited[parentNode] = True

            if flag:
                time += 1 

        return time


    # Mark parent nodes and gets start node address
    def markParents(self, root, parentsMap, start,startNode): # Level Order Traversal (BFS Traversal)
        parentsMap[root] = None # Root has no parent
        queue = [root]

        while queue:
            
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.pop(0)

                if node.val == start:
                    startNode[0] = node

                if node.left:
                    queue.append(node.left)
                    parentsMap[node.left] = node
                if node.right:
                    queue.append(node.right)
                    parentsMap[node.right] = node





        