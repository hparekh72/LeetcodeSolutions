# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def goodNodes(self, root: TreeNode) -> int:
#         # TC: O(N)
#         # SC: O(N)
#         if root == None:
#             return 

#         maximum = root.val
#         count = [0]
#         self.countGoodNodes(root, maximum, count)
#         return count[0]

#     # Preorder Traversal
#     def countGoodNodes(self, root, maximum, count):

#         if root == None:
#             return

#         if root.val >= maximum:
#             maximum = root.val
#             count[0] += 1

#         self.countGoodNodes(root.left, maximum, count)
#         self.countGoodNodes(root.right, maximum, count) 


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # TC: O(N)
        # SC: O(N)
        if root == None:
            return 

        return self.countGoodNodes(root, root.val)
 

    # Preorder Traversal (DFS)
    def countGoodNodes(self, root, maximum):

        if root == None:
            return 0

        if root.val >= maximum:
            maximum = root.val
            res = 1
        else:
            res = 0

        res += self.countGoodNodes(root.left, maximum)
        res += self.countGoodNodes(root.right, maximum)
        return res
        
