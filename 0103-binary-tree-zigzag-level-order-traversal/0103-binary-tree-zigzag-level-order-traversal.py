# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Level order Travesal
        

        # Brute Force:

        # if root == None:
        #     return 

        # queue = [root]
        # res = []
        # flag = True

        # while queue:
        #     current_level = []
            
        #     for _ in range(len(queue)):
        #         node = queue.pop(0)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #         current_level.append(node.val)
        #     flag = not flag

        #     if flag:
        #         current_level.reverse()

        #     res.append(current_level)

        # return res

        # Optimal:
        # TC: O(N)
        # SC: O(N)

        if root == None:
            return 

        queue = [root]
        res = []
        flag = True

        while queue:
            current_level = []
            
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                if flag:
                    current_level.append(node.val)
                else:
                    current_level.insert(0, node.val)                

            flag = not flag

            res.append(current_level)

        return res




            

            


        