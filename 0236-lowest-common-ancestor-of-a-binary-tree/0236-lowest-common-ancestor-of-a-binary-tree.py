# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Brute Force
        # TC: O(N) + O(N) + (N) = O(3N)
        # SC: O(N) + O(N) = O(2N)

        pathP = []
        pathQ = []
        self.getPath(root, p, pathP)
        self.getPath(root, q, pathQ)

        prevCommom = TreeNode(-1)
        length = min(len(pathP), len(pathQ))
        for i in range(length):
            if pathP[i] == pathQ[i]:
                prevCommom = pathP[i]

        return prevCommom
            

    def getPath(self, root, targetNode, res):
        if root == None:
            return False

        res.append(root)

        if root == targetNode:
            return True

        if self.getPath(root.left, targetNode, res) or self.getPath(root.right, targetNode, res):
            return True

        res.pop(-1)

        return False

        