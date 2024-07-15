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
        self.markParents(root, self.parentsMap)
        startNode = [0]
        self.getStartNode(root, start, startNode) # Get start node address

        # BFS traversal on all the nodes from the start node

        queue = [startNode[0]]
        
        visited = {startNode[0]: True}
        curr_level = 0 # minutes

        c = 4
        q = []

        while queue:
            
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.pop(0)

                if node.left and node.left not in visited:
                    queue.append(node.left)
                    visited[node.left] = True
                
                if node.right and node.right not in visited:
                    queue.append(node.right)
                    visited[node.right] = True

                parentNode = self.parentsMap[node]
                if parentNode and parentNode not in visited:
                    queue.append(parentNode)
                    visited[parentNode] = True

            if len(queue) > 0:
                curr_level += 1 

        return curr_level

    def getStartNode(self, root, start, startNode): # Preorder Traversal

        if root == None:
            return 
        
        if root.val == start:
            startNode[0] = root
            return 

        self.getStartNode(root.left, start, startNode)
        self.getStartNode(root.right, start, startNode)
            


    def markParents(self, root, parentsMap): # Level Order Traversal (BFS Traversal)
        parentsMap[root] = None # Root has no parent
        queue = [root]

        while queue:
            
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                    parentsMap[node.left] = node
                if node.right:
                    queue.append(node.right)
                    parentsMap[node.right] = node





        