# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        # Approach 1: Using Recursion

        # TC: O(logN) N -> Height of the tree
        # SC: O(logN)
        # if root == None:
        #     return None

        # if val == root.val:
        #     print(root)
        #     return root
        # elif val < root.val:
        #     return self.searchBST(root.left, val)
        # else:
        #     return self.searchBST(root.right, val)

        # Approach 2: Iterative
        # TC: O(logN) N -> Height of the tree

        while root != None and root.val != val:
            if val < root.val:
                root = root.left
            else:
                root = root.right
        
        return root



        