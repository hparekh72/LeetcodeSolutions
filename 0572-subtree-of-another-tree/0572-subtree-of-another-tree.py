# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# TC: O(N*M) N -> mainTree, M -> subTree
# SC: O(N)

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # An empty subtree can always be considered a subtree of any tree.
        if subRoot == None:
            return True
        # An empty tree cannot contain any subtrees except another empty tree.
        if not root:
            return False

        return self.sameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, newRoot, subRoot):

        if newRoot == None or subRoot == None:
            return newRoot == subRoot

        return newRoot.val == subRoot.val and self.sameTree(newRoot.left, subRoot.left) and self.sameTree(newRoot.right, subRoot.right)

        
        