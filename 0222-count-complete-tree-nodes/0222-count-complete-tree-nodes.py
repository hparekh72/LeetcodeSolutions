# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


        # Brute Force: Any Tree Traversal (PreOrder, InOrder, PostOrder, LevelOrder)
        # TC: O(N)
        # SC: O(N)

        # Optimal Approach
        # TC: O(logN^2)
        # SC: O(logN)

#  Self Notes:
#  Formula is (2^TreeLevel - 1). Only works for perfect tree.
#  To determine if its a perfect tree, go all the way down and count the nodes on left and right side, If they match, its a perfect tree and our formula applies.
#  If its not a perfect tree, we go on left and right subtree and again determine if they are perfect tree.
#  When we have our left and right heights, we do (1 + left + right)
#  If we reach null, return 0


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # Optimal Approach
        # TC: O(logN^2)
        # SC: O(logN)

        if root == None:
            return 0
        
        leftHeight = self.getLeftHeight(root) # TC: O(logN)
        rightHeight = self.getRightHeight(root) # TC: O(logN)

        if leftHeight == rightHeight:
            return pow(2, leftHeight) - 1 # Formula is (2^TreeLevel - 1). Only works for perfect tree.

        return 1 + self.countNodes(root.left) + self.countNodes(root.right) # TC: O(logN)

    def getLeftHeight(self, root): # TC: O(logN)
        count = 0

        while root != None:
            root = root.left
            count += 1
        
        return count

    def getRightHeight(self, root): # TC: O(logN)
        count = 0

        while root != None:
            root = root.right
            count += 1

        return count 






        