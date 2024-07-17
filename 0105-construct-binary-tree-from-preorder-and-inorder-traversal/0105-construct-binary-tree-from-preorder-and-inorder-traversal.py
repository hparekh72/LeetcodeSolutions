# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # Brute Force:
        # TC: O(N^2)
        # SC: O(N) (recursive call stack) + O(N) (new preorder and inorder arrays in each call) = O(N)

        if len(preorder) == 0 or len(inorder) == 0:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0]) # TC: O(N)

        root.left = self.buildTree(preorder[1 : mid+1], inorder[ : mid]) # Skipping 0-index in preorder, as we already just created a node 
        root.right = self.buildTree(preorder[mid+1 : ], inorder[mid+1 : ])

        return root


        