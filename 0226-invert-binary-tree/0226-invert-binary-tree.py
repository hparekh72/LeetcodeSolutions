# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# TC: O(N)
# SC: O(N)

# Note: Both Pre-order or Post-order traversal can work
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]: # Recursive Approach
        # Preorder Traversal
        if root == None: # Base Case
            return  
        
        # Swap
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left) # Go Left
        self.invertTree(root.right) # Go right

        return root

        
        
        