class Solution:
    def build(self, preorder, postorder, preStart, preEnd, postStart, postEnd, indices):
        if preStart > preEnd or postStart > postEnd: return None
        root = TreeNode(preorder[preStart])
        leftCount = 0
        if preStart + 1 <= preEnd: leftCount = indices[preorder[preStart + 1]] - postStart + 1
        if leftCount == 0: root.left = None
        else: root.left = self.build(preorder, postorder, preStart + 1, preStart + leftCount, postStart, indices[preorder[preStart + 1]], indices)
            
        root.right = self.build(preorder, postorder, preStart + leftCount + 1, preEnd, postStart + leftCount, postEnd - 1, indices)
        return root
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(postorder)
        indices = {}
        for i in range(n): indices[postorder[i]] = i
        preStart, preEnd = 0, n - 1
        postStart, postEnd = 0, n - 1
        return self.build(preorder, postorder, preStart, preEnd, postStart, postEnd, indices)