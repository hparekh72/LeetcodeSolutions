# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Approach: Level Order Traversal (BFS)
        # TC: O(N)
        # SC: O(N)

        res = []

        if not root:
            return res

        queue = deque([root])

        while queue:
            level_size = len(queue)
            for pos in range(level_size):
                node = queue.popleft()

                if pos == level_size - 1: # Last node of each level
                    res.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return res


        