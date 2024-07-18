# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    # TC: O(N)
    # SC: O(N)
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        # Preorder Traversal
        res = []
        self.preorder(root, res)
        return ",".join(res)

    def preorder(self, root, res):
        if root == None:
            res.append("N")
            return

        res.append(str(root.val))
        self.preorder(root.left, res)
        self.preorder(root.right, res)
                
    # TC: O(N)
    # SC: O(N)
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        arr = data.split(",")
        pos = [0]
        return self.buildTree(arr, pos)

    
    def buildTree(self, arr, pos): # DFS traversal
        if arr[pos[0]] == "N":
            pos[0] += 1
            return None

        node = TreeNode(int(arr[pos[0]]))
        pos[0] += 1
        node.left = self.buildTree(arr, pos)
        node.right = self.buildTree(arr, pos)
        return node






        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))