# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        # Brute Force:
        # TC: O(NlogN)
        # SC: O(1)

        self.root = None
        for i in range(len(preorder)):
            self.insertIntoBST(preorder[i]) # TC: O(logN)

        return self.root

    def insertIntoBST(self, val):
        if self.root == None:
            self.root = TreeNode(val)
            return
        
        curr = self.root
        while curr != None:
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
        