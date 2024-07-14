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

        # pathP = []
        # pathQ = []
        # self.getPath(root, p, pathP)
        # self.getPath(root, q, pathQ)

        # prevCommom = TreeNode(-1)
        # length = min(len(pathP), len(pathQ))
        # for i in range(length):
        #     if pathP[i] == pathQ[i]:
        #         prevCommom = pathP[i]

        # return prevCommom

        # Approach 2
        # TC: O(N)
        # SC: O(N)

        # Base Case
        if root == None or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q) # Go left
        right = self.lowestCommonAncestor(root.right, p, q) # Go right

        # Result 
        if left == None:
            return right
        elif right == None:
            return left
        else: # Both left and right are not null, we found our result
            return root
            

    # def getPath(self, root, targetNode, res):
    #     if root == None:
    #         return False

    #     res.append(root)

    #     if root == targetNode:
    #         return True

    #     if self.getPath(root.left, targetNode, res) or self.getPath(root.right, targetNode, res):
    #         return True

    #     res.pop(-1)

    #     return False

        