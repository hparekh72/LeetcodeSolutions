# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Level Order traversal
        # TC: O(N)
        # SC: O(N)

        count = 0

        if root == None:
            return count

        queue = [root]

        while queue:

            count += 1

            for _ in range(len(queue)):
            
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return count

        # Recursion
        # Space: Auxilary space of O(n) - Skew tree
        # Time: O(n)

        # if root == None:
        #     return 0

        # leftTree = self.maxDepth(root.left)
        # rightTree = self.maxDepth(root.right)

        # return 1 + max(leftTree, rightTree)

            


                

            


        

        
        