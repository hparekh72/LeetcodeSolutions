# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Create a defaultdict with default value as an empty list.
        self.vertical_map = collections.defaultdict(list)
        # Perform a level order traversal of the binary tree.
        self.levelOrder(root)

        # Construct the result by sorting keys and retrieving values.
        result = []
        print(self.vertical_map)
        sorted_keys = sorted(self.vertical_map)

        for key in sorted_keys:
            result.append(self.vertical_map[key])

        return result


    def levelOrder(self, root):
        # Initialize a deque with the root and its horizontal position (0).
        q = collections.deque([(root, 0)])

        # Iterate while there are nodes in the queue.
        while q:
            # Get the number of nodes at the current level.
            levelSize = len(q)
            # Create a temporary defaultdict for the current level.
            temp_map = collections.defaultdict(list)

            # Process nodes at the current level.
            for _ in range(levelSize):
                # Dequeue a node and its horizontal position.
                node, x = q.popleft()
                # Add the node's value to the temporary map at its position.
                temp_map[x].append(node.val)


                # Enqueue left and right children if they exist.
                if node.left: q.append((node.left, x - 1))
                if node.right: q.append((node.right, x + 1))

            # Extend values from the temporary map to the vertical map.
            for k in temp_map:
                self.vertical_map[k].extend(sorted(temp_map[k]))
        