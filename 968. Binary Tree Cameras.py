class Solution(object):
    def minCameraCover(self, root):
        self.ans = 0
        def dfs(node):
            if not node:
                return 1
            left = dfs(node.left)
            right = dfs(node.right)
            if left == 0 or right == 0:
                self.ans += 1
                return 2
            if left == 2 or right == 2:
                return 1
            return 0
        if dfs(root) == 0:
            self.ans += 1 
        return self.ans