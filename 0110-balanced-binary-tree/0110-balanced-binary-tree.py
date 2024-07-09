# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # TC: O(N)
    # SC: O(N) # Recursive call stack

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.heightBalanced(root) == -1:
            return False
        else:
            return True

    def heightBalanced(self, root):
        if root == None:
            return 0

        leftHeight = self.heightBalanced(root.left)
        rightHeight = self.heightBalanced(root.right)

        if leftHeight == -1 or rightHeight == -1:
            return -1

        if abs(leftHeight - rightHeight) > 1:
            return -1


        return 1 + max(leftHeight, rightHeight)
        