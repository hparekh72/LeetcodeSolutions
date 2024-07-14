# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Level Order Traversal

        # TC: O(N)
        # SC: O(N)

        if root == None:
            return 0

        queue = deque([(root, 0)])
        max_width = 0

        while queue:
            level_size = len(queue)
            _, level_start = queue[0]

            for _ in range(level_size):

                node, index = queue.popleft()

                if node.left:
                    queue.append((node.left, 2 * index))

                if node.right:
                    queue.append((node.right, 2 * index + 1))

            max_width = max(max_width, index - level_start + 1)

        return max_width

        