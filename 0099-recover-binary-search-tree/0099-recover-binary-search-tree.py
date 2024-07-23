# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    



    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

    # Brute Force:
        # 1) Do any traversal and then sort the array.
        # 2) Compare the sorted array with the BST by doing inorder tree traversal
        # 3) Update the node which are different 

        # TC: O(N) + O(NlogN) + O(N)
        # SC: O(N) + O(N) (Recursive Stack Space)
 

    # Optimal: Swap can have two possibilities
        # 1) Swapped nodes are not adjacent
        # 2) Swapped nodes are adjacent

        # TC: O(N)
        # SC: O(N) (Recursive Stack Space)
        self.prev = None
        self.first = None
        self.middle = None
        self.last = None

        self.inorder(root)

        if self.first != None and self.last != None:
            self.swap(self.first, self.last)

        elif self.first != None and self.middle != None:
            self.swap(self.first, self.middle)

    def swap(self, node1, node2):
        temp = node1.val
        node1.val = node2.val
        node2.val = temp
        


    def inorder(self, root):

        if root == None:
            return None
        
        self.inorder(root.left) # Move Left


        if self.prev != None and root.val < self.prev.val:
            # If this is first violation, mark these two nodes as first and middle
            if self.first == None:
                self.first = self.prev
                self.middle = root
            else:
            # If this is second violation, mark this node as last
                self.last = root

        self.prev = root # Mark current node as previous

        self.inorder(root.right) # Move Right

    
    

    

      