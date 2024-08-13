class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPathSum = float('-inf')
        self.dfs(root)
        return self.maxPathSum

    def dfs(self, root):
        if not root: return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.maxPathSum = max(left+right+root.val, left+root.val, right+root.val, root.val, self.maxPathSum)
        maxLeftRight = max(left, right)
        if maxLeftRight < 0:
            return root.val
        else:
            return root.val + max(left, right)