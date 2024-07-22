# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         # TC: O(N)
#         #SC: O(N) Recursive Stack Space
#         res = [True]
#         prev = [None]
#         self.inorder(root, prev, res)
#         return res[0]

#     def inorder(self, root, prev, res):
#         if root == None:
#             return 

#         self.inorder(root.left, prev, res)

#         # Check if the current node's value is greater than the previous node's value
#         if prev[0] != None and prev[0] >= root.val:
#             res[0] = False
#             return
#         # Update the prev value to the current node's value
#         prev[0] = root.val

#         self.inorder(root.right, prev, res)

# Approach 2:
# TC: O(N)
# SC: O(N)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Use a helper function that can use early exit
        # 'prev' is used as a mutable container to track the last node value
        self.prev = None
        return self.inorder(root)

    def inorder(self, root):
        if root is None:
            return True
        
        # Traverse the left subtree
        if not self.inorder(root.left):
            return False

        # Check current node value with the previous node value
        if self.prev is not None and self.prev >= root.val:
            return False
        # Update the prev pointer
        self.prev = root.val

        # Traverse the right subtree
        return self.inorder(root.right)


        
        