# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Notes:
# When you have to traverse back use a map to store the parent node
# Basically turn a Binary Tree into an Undirected Graph

# Self Notes:
#  Mark each node to its parent to traverse upwards
#  We will do a BFS traversal starting from the target node
#  As long as we have not seen our node previously, Traverse up, left, right until reached Kth distance
#  when reached Kth distance, break out of BFS loop and remaining node's values in our queue is our result







class Solution:
    # TC: O(N) + O(N) = O(N)
    # SC: O(N) + O(N) + O(N) = O(N)
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.parentsMap = {} # SC: O(N)
        self.markParents(root, self.parentsMap) # TC: O(N)

        # We will do a BFS traversal starting from the target node
        # TC: O(N)
        queue = [target] # SC: O(N)
        visited = {target: True} # SC: O(N)
        curr_level = 0

        while queue:
            if curr_level == k:
                break

            curr_level += 1

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
        res = []
        while queue:
            node = queue.pop(0)
            res.append(node.val)

        return res
            

    def markParents(self, root, parentsMap): # Level Order Traversal (BFS traversal)
        queue = [root]
        parentsMap[root] = None  # Root has no parent
        while queue:
            for _ in range(len(queue)):
                node = queue.pop(0)

                if node.left:
                    queue.append(node.left)
                    parentsMap[node.left] = node
                
                if node.right:
                    queue.append(node.right)
                    parentsMap[node.right] = node