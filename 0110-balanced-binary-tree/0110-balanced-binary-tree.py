# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# TC: O(n)
# SC: O(n) (Recursive Call Stack)

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.res = True

        def height(node):
            if not node:
                return 0

            leftHeight = height(node.left)
            rightHeight = height(node.right)

            if abs(rightHeight - leftHeight) > 1:
                self.res = False

            return 1 + max(leftHeight, rightHeight)

        height(root)
        return self.res

            

        