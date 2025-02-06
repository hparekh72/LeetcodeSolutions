# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Brute Force:
# TC: O(n^2)
# SC: O(n) (Recursive Call Stack)

# Optimal:
# TC: O(n)
# SC: O(n) (Recursive Call Stack)

# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:

#         self.res = True

#         def height(node):
#             if not node:
#                 return 0

#             leftHeight = height(node.left)
#             rightHeight = height(node.right)

#             if abs(rightHeight - leftHeight) > 1:
#                 self.res = False

#             return 1 + max(leftHeight, rightHeight)

#         height(root)
#         return self.res

            
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return [True, 0]

            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)

            balanced = leftHeight[0] and rightHeight[0] and abs(rightHeight[1] - leftHeight[1]) <= 1

            return [balanced, 1 + max(leftHeight[1], rightHeight[1])]

        return dfs(root)[0]
    



            