# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Approach: Level Order Traversal
        # TC: O(N)
        # SC: O(N)

        res = []

        if root == None:
            return            

        queue = [root]

        while queue:
            level_size = len(queue)
            for pos in range(level_size):

                node = queue.pop(0)

                if pos == level_size - 1: # Last node of each level
                    res.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return res

            
        