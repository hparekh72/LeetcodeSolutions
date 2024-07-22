# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Brute Force:
Do inorder traversal and store the result in an array. Inorder traversal gives a sorted array. Then use a index variable to traverse the array for next and hasNext operations.
Time Complexity of next() and hasNext(): O(1)
SC: O(N)

Optimal: Iterative Inorder Traversal using stack
TC: O(1)
    __init__(): O(h)
    next(): Amortized O(1) per call over n calls. Considering that each node is dealt with exactly once across all calls to next(), the average cost per operation levels out to O(1).
    hasNext(): O(1) for checking the state of the stack.

SC: O(Height Of the tree)
"""

class BSTIterator:

    stack = []

    def __init__(self, root: Optional[TreeNode]):
        # Start by pushing all left children of the root into the stack
        self.pushAll(root)
        

    def next(self) -> int:
        node = self.stack.pop(-1) # Pop the top node 
        self.pushAll(node.right)  # If the node has a right child, push its left children to stack
        return node.val
        
    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def pushAll(self, root): 
        while root != None:
            self.stack.append(root) # Add the node to the stack
            root = root.left  # Move to the left child
         
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()