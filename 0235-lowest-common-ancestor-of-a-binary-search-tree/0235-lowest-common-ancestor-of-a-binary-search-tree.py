# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # Brute Force: LCA in Binary Tree
        # TC: O(N)
        # SC: O(N)

        # Optimal:
        # Approach: When we cannot determine if both the nodes are on the left or right subtree, then that node is the point of intersection

        # TC: O(Height of the Tree)
        # SC: O(Height of the Tree)
        if root == None:
            return root

        if p.val < root.val and q.val < root.val: # Move left
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q) # Move right
        else:
            return root





        
        