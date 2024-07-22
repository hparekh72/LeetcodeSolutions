# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # TC: O(N)
        #SC: O(N) Recursive Stack Space
        res = [True]
        prev = [None]
        self.inorder(root, prev, res)
        return res[0]

    def inorder(self, root, prev, res):
        if root == None:
            return 

        self.inorder(root.left, prev, res)

        # Check if the current node's value is greater than the previous node's value
        if prev[0] != None and prev[0] >= root.val:
            res[0] = False
            return
        # Update the prev value to the current node's value
        prev[0] = root.val

        self.inorder(root.right, prev, res)

        
        