# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Brute Force: 
1) Do inorder traversal to get a sorted array.
2) Using two pointer approach(left = start, right = len(arr) - 1) we can solve two sum

TC: O(N) + O(N)
SC: O(N)

"""

"""
Optimal: 
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

1) BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.

2) boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.

3) int next() Moves the pointer to the right, then returns the number at the pointer.

Intution: 
1) Use Inorder(left, root, right) to get a sorted array in increasing order.
2) Use Inorder(right, root, left) to get a sorted array in decreasing order
3) Create 2 objects of class BSTIterator with reverse = True and reverse = False as the parameter
reverse = False --> next() in incresing order
reverse = False --> next() (also called as before()) is in decreasing order

3) Then compare similar to the two pointer approach 

TC: O(N)
SC: O(H) + O(H) (stack)

"""

class BSTIterator:

    def __init__(self, root, isReverse):
        self.stack = []
        self.reverse = isReverse
        self._pushAll(root)

    def _pushAll(self, root):
        while root != None:
            self.stack.append(root)
            if self.reverse: 
                root = root.right
            else:
                root = root.left

    def next(self):
        node = self.stack.pop(-1)
        if self.reverse:
            self._pushAll(node.left)
        else:
            self._pushAll(node.right)
        return node.val

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root.left == None and root.right == None:
            return False

        left = BSTIterator(root, False)
        right = BSTIterator(root, True)


        i = left.next()
        j = right.next() # before()

        while i < j:
            if i + j == k:
                return True
            elif i + j < k:
                i = left.next()
            else:
                j = right.next()

        return False

        
        