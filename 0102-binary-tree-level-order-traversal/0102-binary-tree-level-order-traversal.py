# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # TC: O(N) # N -> Number of Nodes
        # SC: O(N)

        res = []

        if root == None:
            return res

        queue = [root]
        

        while queue:
            size = len(queue)
            sublist = []
            for _ in range(size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                sublist.append(node.val)
            res.append(sublist)

        return res


        