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
        # Initialize a BST iterator.
        self.stack = []  # Stack to manage the controlled traversal of the BST
        self.reverse = isReverse  # Boolean flag to determine the direction of traversal
        self._pushAll(root)  # Push initial elements to the stack based on traversal order

    def _pushAll(self, root):
        # Private helper method to push nodes to the stack.
        # This method traverses to the leftmost or rightmost node (based on isReverse)
        while root is not None:
            self.stack.append(root)
            if self.reverse: 
                root = root.right  # Move to the right child if reverse is True
            else:
                root = root.left   # Move to the left child if reverse is False

    def next(self):
        # Return the next element in the traversal.
        node = self.stack.pop(-1)  # Pop the element from the top of the stack
        # Depending on the direction of traversal, push the children of the popped node
        if self.reverse:
            self._pushAll(node.left)  # For reverse, push left children to the stack
        else:
            self._pushAll(node.right) # For normal order, push right children to the stack
        return node.val  # Return the value of the current node

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # Check if the BST contains two elements that sum up to k
        if root.left is None and root.right is None:
            # If the tree has only one node, return False since no pair exists
            return False

        left = BSTIterator(root, False)  # Create an iterator for ascending order
        right = BSTIterator(root, True)  # Create an iterator for descending order

        i = left.next()  # Get the smallest element
        j = right.next() # Get the largest element

        while i < j:  # Continue until the two iterators cross each other
            if i + j == k:
                # If the sum of both elements equals k, return True
                return True
            elif i + j < k:
                # If the sum is less than k, increment the left iterator to get a larger number
                i = left.next()
            else:
                # If the sum is greater than k, decrement the right iterator to get a smaller number
                j = right.next()

        return False  # If no pair is found that sums to k, return False


        
        