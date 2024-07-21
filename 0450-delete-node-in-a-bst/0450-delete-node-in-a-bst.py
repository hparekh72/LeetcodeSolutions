# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # TC: O(Height of the tree)
        if root == None:
            return None

        if root.val == key:
            return self.helper(root)

        dummy = root

        while root != None:
            if key < root.val: # Move left 
                if root.left != None and root.left.val == key:
                    root.left = self.helper(root.left)
                    break
                else:
                    root = root.left
            else:
                if root.right != None and root.right.val == key:
                    root.right = self.helper(root.right)
                    break
                else:
                    root = root.right

        return dummy

    def helper(self, root): # root is the node to be deleted
        if root.left == None:
            return root.right
        elif root.right == None:
            return root.left
        else:
            rightChild = root.right
            lastRight = self.findLastRight(root.left)
            lastRight.right = rightChild
            return root.left


    def findLastRight(self, root):
        if root.right == None:
            return root
        return self.findLastRight(root.right)
        