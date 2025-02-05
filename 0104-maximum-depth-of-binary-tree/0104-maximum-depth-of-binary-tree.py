# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # TC: O(n)
    # SC: O(n)

    # def maxDepth(self, root: Optional[TreeNode]) -> int: # Recursive DFS approach
    #     if not root:
    #         return 0

    #     leftTree = self.maxDepth(root.left)
    #     rightTree = self.maxDepth(root.right)

    #     return 1 + max(leftTree, rightTree)

    # Iterative Approaches

    # TC: O(n)
    # SC: O(n)
    def maxDepth(self, root: Optional[TreeNode]) -> int: # BFS (Level Order Traversal)
        if not root:
            return 0

        queue = deque([root])
        level = 0

        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1

        return level


    # TC: O(n)
    # SC: O(n)
    # def maxDepth(self, root: Optional[TreeNode]) -> int: # Iterative DFS (Stack)
    #     stack = [[root, 1]] # [node, depth]
    #     res = 0

    #     while stack:
    #         node, depth = stack.pop()

    #         if node:
    #             res = max(res, depth)
    #             stack.append([node.left, depth + 1])
    #             stack.append([node.right, depth + 1])
        
    #     return res







        