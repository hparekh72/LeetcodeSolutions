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
    def goodNodes(self, root: TreeNode) -> int: # Preorder Traversal (DFS)
        # TC: O(N)
        # SC: O(N)

        def countGoodNodes(node, max_value):
            if not node:
                return 0

            res = 1 if node.val >= max_value else 0
            max_value = max(max_value, node.val)

            res += countGoodNodes(node.left, max_value)
            res += countGoodNodes(node.right, max_value)

            return res

        return countGoodNodes(root, root.val)

        


            
            
 

    
