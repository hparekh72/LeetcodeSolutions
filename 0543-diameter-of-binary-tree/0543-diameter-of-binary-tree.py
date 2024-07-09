# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maximum = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Brute Force:
        # TC: O(N^2)
        # SC: O(N) + O(N)

        # self.findDiameter(root)
        # return self.maximum

        # Optimal: Using the code of maximum depth of the binary tree
        # TC: O(N)
        # SC: O(N) 

        diameter = [0]
        self.height(root, diameter)
        return diameter[0]

    def height(self, root, diameter):
        if root == None:
            return 0

        leftTree = self.height(root.left, diameter)
        rightTree = self.height(root.right, diameter)

        diameter[0] = max(diameter[0], leftTree + rightTree)

        return 1 + max(leftTree, rightTree)


    # def findDiameter(self, root):

    #     if root == None:
    #         return 

    #     leftHeight = self.findHeight(root.left)
    #     rightHeight = self.findHeight(root.right)

    #     self.maximum = max(self.maximum, leftHeight + rightHeight)

    #     self.findDiameter(root.left)
    #     self.findDiameter(root.right)

    # def findHeight(self, root):
    #     if root == None:
    #         return 0

    #     leftTree = self.findHeight(root.left)
    #     rightTree = self.findHeight(root.right)

    #     return 1 + max(leftTree, rightTree)
        

    


        