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


        # if not inorder or not postorder:
        #     return None

        # root = TreeNode(postorder[-1])
        # mid = inorder.index(root.val)
        # root.left = self.buildTree(inorder[ : mid], postorder[ : mid])
        # root.right = self.buildTree(inorder[mid+1 : ], postorder[mid : len(postorder) - 1])

        # return root

        # Optimal
        # TC: O(N)
        # SC: O(N) + O(N) = O(N)

        inorder_map = {}
        for index, value in enumerate(inorder):
            inorder_map[value] = index

        return self.createTree(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1, inorder_map)

    def createTree(self, inorder, inStart, inEnd, postorder, postStart, postEnd, inorder_map):

        # Base case: If the start indices exceed the end indices, return None
        if inStart > inEnd or postStart > postEnd:
            return None

        # Create a new TreeNode with value at the current preorder index
        root = TreeNode(postorder[postEnd])

        # Find the index of the current root value in the inorder traversal
        mid = inorder_map[root.val]

        # Calculate the number of elements in the left subtree
        numsLeft = mid - inStart

        # Recursively build the left subtree
        root.left = self.createTree(inorder, inStart, mid - 1, postorder, postStart, postStart + numsLeft - 1, inorder_map)

        # Recursively build the right subtree
        root.right = self.createTree(inorder, mid + 1, inEnd, postorder, postStart + numsLeft, postEnd - 1, inorder_map)

        return root








