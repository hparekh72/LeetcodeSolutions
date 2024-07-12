# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        self.verticalMap = defaultdict(list)
        
        self.levelOrder(root)

        res = []
        sorted_keys = sorted(self.verticalMap)
        for key in sorted_keys:
            res.append(self.verticalMap[key])

        return res


    def levelOrder(self, root):
        if root == None:
            return

        q = collections.deque([(root, 0)])

        while q:
            current_level_map = defaultdict(list)
            for _ in range(len(q)):
                node, pos = q.popleft()
                if node.left:
                    q.append((node.left, pos - 1))

                if node.right:
                    q.append((node.right, pos + 1))

                current_level_map[pos].append(node.val)

            for pos in current_level_map:
                self.verticalMap[pos].extend(sorted(current_level_map[pos])) 
                # Sorted since there may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

            



        



        


        