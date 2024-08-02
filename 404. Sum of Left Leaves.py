class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def is_leaf(node):
            return not node.left and not node.right
        
        def sum_left_leaves(node):
            if not node:
                return 0
            if node.left and is_leaf(node.left):
                return node.left.val + sum_left_leaves(node.right)
            return sum_left_leaves(node.left) + sum_left_leaves(node.right)
        
        return sum_left_leaves(root)