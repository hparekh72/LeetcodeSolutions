# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
    # def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # Brute Force:
        # TC: O(N^2)
        # SC: O(N) (recursive call stack) + O(N) (new preorder and inorder arrays in each call) = O(N)

        # if len(preorder) == 0 or len(inorder) == 0:
        #     return None

        # root = TreeNode(preorder[0])
        # mid = inorder.index(preorder[0]) # TC: O(N)

        # root.left = self.buildTree(preorder[1 : mid+1], inorder[ : mid]) # Skipping 0-index in preorder, as we already just created a node 
        # root.right = self.buildTree(preorder[mid+1 : ], inorder[mid+1 : ])

        # return root

        # Optimal:
        # TC: O(N)
        # SC: O(N) + O(N) = O(N)

    #     inorder_map = {} # SC: O(N)
    #     for index, value in enumerate(inorder):
    #         # Create a map to store indices of elements in the inorder traversal
    #         inorder_map[value] = index

    #     return self.createTree(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1, inorder_map)

    # def createTree(self, preorder, preStart, preEnd, inorder, inStart, inEnd, inorder_map):
    #     # Base case: If the start indices exceed the end indices, return None
    #     if preStart > preEnd or inStart > inEnd:
    #         return None

    #     # Create a new TreeNode with value at the current preorder index
    #     root = TreeNode(preorder[preStart])

    #     # Find the index of the current root value in the inorder traversal
    #     mid = inorder_map[root.val]

    #     # Calculate the number of elements in the left subtree
    #     numsLeft = mid - inStart

    #     # Recursively build the left subtree
    #     root.left = self.createTree(preorder, preStart + 1, preStart + numsLeft, inorder, inStart, mid - 1, inorder_map)

    #     # Recursively build the right subtree
    #     root.right = self.createTree(preorder, preStart + numsLeft + 1, preEnd, inorder, mid + 1, inEnd, inorder_map)

    #     return root

# Optimal:
# TC: O(N)
# SC: O(N) + O(N) = O(N)

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {}
        for ind, val in enumerate(inorder):
            inorder_map[val] = ind

        def createTable(preStart, preEnd, inStart, inEnd):
            if preStart > preEnd or inStart > inEnd:
                return None

            root = TreeNode(preorder[preStart])
            
            mid = inorder_map[root.val]
            numsLeft = mid - inStart

            root.left = createTable(preStart + 1, preStart + numsLeft, inStart, mid - 1)
            root.right = createTable(preStart + numsLeft + 1, preEnd, mid + 1, inEnd)

            return root

        return createTable(0, len(preorder) - 1, 0, len(inorder) - 1)
 

