# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # TC: O(N)
        # SC: O(N) # Recursive call stack
        maxSum = [float('-inf')]
        self.maximumSum(root, maxSum)
        return maxSum[0]

    def maximumSum(self, root, maxSum) :
        if root == None:
            return 0

        leftSum = max(0, self.maximumSum(root.left, maxSum)) # If path is negative, do not consider it 
        rightSum = max(0, self.maximumSum(root.right, maxSum))
        
        maxSum[0] = max(maxSum[0], root.val + leftSum + rightSum)

        return root.val + max(leftSum, rightSum)
            