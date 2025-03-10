# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

#         # Brute Force:
#         # Do any traversal and store all the elements in a array.
#         # Sort the array in ascending order
#         # Get the kthSmallest element from the start
#         # TC: O(N) + O(NlogN) + O(k) = O(NlogN)
#         # SC: O(N) (Recursive Stack space) + O(N) = O(N)


#         # Optimal
#         # Note: The Inorder of a BST will always be sorted
#         # TC: O(N)
#         # SC: O(N) (Recursive stack space)
#         count = [0]
#         k_smallest = [float('inf')]
#         self.inorder(root, k, count, k_smallest)
#         return k_smallest[0]

#     def inorder(self, root, k, count, k_smallest):
        
#         if root == None or count[0] >= k:
#             return 

#         self.inorder(root.left, k, count, k_smallest)

#         # Increment counter after visiting left subtree
#         count[0] += 1

#         # Check if current node is the Kth smallest
#         if count[0] == k:
#             k_smallest[0] = root.val 
#             return 
            
#         self.inorder(root.right, k, count, k_smallest)


#         # Optimal
#         # Note: The Inorder of a BST will always be sorted
#         # TC: O(N)
#         # SC: O(N) (Recursive stack space)

class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int: # Recursive Solution
#         self.count = 0
#         self.res = 0

#         def inorder(node, k):
#             if not node:
#                 return 

#             inorder(node.left, k)

#             # Increment the counter after visiting left subtree
#             self.count += 1

#             if self.count == k:
#                 self.res = node.val
#                 return 
            
#             inorder(node.right, k)

#         inorder(root, k)
#         return self.res


#         # TC: O(N)
#         # SC: O(N) 
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int: # Iterative Solution
        stack = []
        count = 0

        node = root
        while True:
            if node:
                stack.append(node)
                node = node.left
            else:
                if not stack:
                    break
                node = stack.pop()
                count += 1

                if count == k:
                    return node.val
                
                node = node.right
                


            


            
        
