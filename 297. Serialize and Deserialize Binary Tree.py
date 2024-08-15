# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:
    def serialize(self, root):
        if not root: return "#"
        return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)

    def deserialize(self, data):
        def deserialize_helper(queue):
            val = queue.popleft()
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = deserialize_helper(queue)
            node.right = deserialize_helper(queue)
            return node
        
        queue = deque(data.split(","))
        return deserialize_helper(queue)   