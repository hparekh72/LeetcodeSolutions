# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Note: We can use any traversal (Preorder, Inorder, Postorder, Level Order) to solve this problem

# class Codec:
    # TC: O(N)
    # SC: O(N)
    # def serialize(self, root):
    #     """Encodes a tree to a single string.
        
    #     :type root: TreeNode
    #     :rtype: str
    #     """

    #     # Preorder Traversal
    #     res = []
    #     self.preorder(root, res)
    #     return ",".join(res)

    # def preorder(self, root, res):
    #     if root == None:
    #         res.append("N")
    #         return

    #     res.append(str(root.val))
    #     self.preorder(root.left, res)
    #     self.preorder(root.right, res)
                
    # TC: O(N)
    # SC: O(N)
    # def deserialize(self, data):
    #     """Decodes your encoded data to tree.
        
    #     :type data: str
    #     :rtype: TreeNode
    #     """
    #     arr = data.split(",")
    #     pos = [0]
    #     return self.buildTree(arr, pos)

    
    # def buildTree(self, arr, pos): # DFS traversal
    #     if arr[pos[0]] == "N":
    #         pos[0] += 1
    #         return None

    #     node = TreeNode(int(arr[pos[0]]))
    #     pos[0] += 1
    #     node.left = self.buildTree(arr, pos)
    #     node.right = self.buildTree(arr, pos)
    #     return node
    
    
class Codec:
    # TC: O(N)
    # SC: O(N)
    def serialize(self, root):
        # Level Order Traversal (BFS)
        if root == None:
            return ""

        s = ""
        queue = [root]
        while queue:
            node = queue.pop(0)

            # If node is None, append "N" to the string
            if node == None: 
                s += "N,"
            else:
                s += str(node.val) + ","

                # Push the left and right children to the queue for further traversal
                queue.append(node.left)
                queue.append(node.right)
        return s

    # TC: O(N)
    # SC: O(N)
    def deserialize(self, data):
        # Level Order Traversal

        if not data:
            return None

        arr = data.split(",")

        # Read the root value from the serialized data
        root = TreeNode(int(arr.pop(0)))
        queue = [root]

        # Perform level-order traversal to reconstruct the tree
        while queue:
            node = queue.pop(0)

            # Read the value of the left child from the serialized data
            left_val = arr.pop(0)
            # If the value is not "N", create a new left child and push it to the queue
            if left_val != "N":
                node.left = TreeNode(int(left_val))
                queue.append(node.left)

            # Read the value of the right child from the serialized data
            right_val = arr.pop(0)
            # If the value is not "N", create a new right child and push it to the queue
            if right_val != "N":
                node.right = TreeNode(int(right_val))
                queue.append(node.right)

        return root

        

            

        
        



    







        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))