# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        # Brute Force:
        # TC: O(N^2)
        # SC: O(N) (recursive call stack) + O(N) (new postorder and inorder arrays in each call) = O(N)


        if not inorder or not postorder:
            return None

        root = TreeNode(postorder[-1])
        mid = inorder.index(root.val)
        root.left = self.buildTree(inorder[ : mid], postorder[ : mid])
        root.right = self.buildTree(inorder[mid+1 : ], postorder[mid : len(postorder) - 1])

        return root
