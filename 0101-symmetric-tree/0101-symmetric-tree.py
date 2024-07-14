# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #  Self Notes: 
        #  Mirror property is    left == right and right == left
        #  pre-order traversal on root->left subtree, (root, left, right)
        #  modified pre-order traversal on root->right subtree, (root, right, left) 
        #  compare the node val's if they are the same 
        #  Do both traversals at the same time
        #  if left is null or right is null, then both sides must match and return true (base case)     

        # TC: O(N)
        # SC: O(N)

        if root == None:
            return

        return self.checkSymmetry(root.left, root.right)

    def checkSymmetry(self, leftTree, rightTree):
        if leftTree == None or rightTree == None:
            return leftTree == rightTree

        if leftTree.val != rightTree.val:
            return False

        return self.checkSymmetry(leftTree.left, rightTree.right) and self.checkSymmetry(leftTree.right, rightTree.left)
        

        

        