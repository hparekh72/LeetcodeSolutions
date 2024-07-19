# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # TC: O(logN) N -> Number of nodes
        # SC: O(logN)
        # Intution: Find where(always a leaf node) it can be and insert


        # Recursive Approach

        # if root == None: # If empty tree, create root node
        #     root = TreeNode(val)
        #     return root

        # if val < root.val: 
        #     if root.left == None:
        #         root.left = TreeNode(val)
        #     else:
        #         self.insertIntoBST(root.left, val)
        # else:
        #     if root.right == None:
        #         root.right = TreeNode(val)
        #     else:
        #         self.insertIntoBST(root.right, val)

        # return root

        #Iterative Approach
        # TC: O(logN) N -> Number of nodes
        # SC: O(1)
        if root == None: # If empty tree, create root node
            root = TreeNode(val)
            return root

        curr = root
        while True:
            if val < curr.val: 
                if curr.left == None:
                    curr.left = TreeNode(val)
                    break
                else:
                    curr = curr.left
            else:
                if curr.right == None:
                    curr.right = TreeNode(val)
                    break
                else:
                    curr = curr.right

        return root



        