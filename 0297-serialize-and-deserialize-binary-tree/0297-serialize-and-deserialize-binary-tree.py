# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# DFS Approach (Pre-order Traversal)
# TC: O(n)
# SC: O(n)

# class Codec:

#     def serialize(self, root): # Pre-order Traversal # TC: O(n)
#         """Encodes a tree to a single string.
        
#         :type root: TreeNode
#         :rtype: str
#         """
#         res = []

#         def dfs(node):
#             if not node:
#                 res.append("N")
#                 return 
            
#             res.append(str(node.val))
#             dfs(node.left)
#             dfs(node.right)
#         dfs(root)
#         return ",".join(res)
        

#     def deserialize(self, data): # TC: O(n)
#         """Decodes your encoded data to tree.
        
#         :type data: str
#         :rtype: TreeNode
#         """
#         vals = data.split(",")
#         self.i = 0

#         def dfs():
#             if vals[self.i] == "N":
#                 self.i += 1
#                 return None

#             node = TreeNode(int(vals[self.i]))
#             self.i += 1
#             node.left = dfs()
#             node.right = dfs()
#             return node

#         return dfs()

# BFS Approach

# TC: O(n)
# SC: O(n)

class Codec:
    def serialize(self, root):
        if not root:
            return "N"

        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                res.append("N")
            else:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        return ",".join(res)
    
    def deserialize(self, data): 
        vals = data.split(",")
        if vals[0] == "N":
            return None
        
        root = TreeNode(vals[0])
        queue = deque([root])
        index = 1

        while queue:
            node = queue.popleft()
            if vals[index] != "N":
                node.left = TreeNode(vals[index])
                queue.append(node.left)
            index += 1

            if vals[index] != "N":
                node.right = TreeNode(vals[index])
                queue.append(node.right)
            index += 1

        return root

        




        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))