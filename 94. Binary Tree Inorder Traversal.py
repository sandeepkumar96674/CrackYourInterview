# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(currentNode, res):

            if not currentNode:
                return 
            dfs(currentNode.left, res)
            res.append(currentNode.val)
            dfs(currentNode.right, res)

        dfs(root, res)
        return res