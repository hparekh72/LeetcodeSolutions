# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # Brute Force:
        # TC: O(N)
        # SC: O(N)

        # Optimal: 
        # TC: O(N)
        # SC: O(1)

        # Intution: On the left sub-tree, whichever is the last node of preorder, just took that and connect with the right of the current node(root).

        #     Example: 
        #     1
        #    / \
        #   2   3

        #   connect 2 to 3
        #   connect 1 to only 2

        curr = root

        while curr != None:
            if curr.left:
                # If yes, find the rightmost node in the left subtree
                prev = curr.left
                while prev.right != None:
                    prev = prev.right

                # Connect the rightmost node in the left subtree to the current node's right child
                prev.right = curr.right

                # Move the entire left subtree to the right child of the current node
                curr.right = curr.left

                # Set the left child of the current node to None
                curr.left = None
            

            # Move to the next node on the right side
            curr = curr.right



