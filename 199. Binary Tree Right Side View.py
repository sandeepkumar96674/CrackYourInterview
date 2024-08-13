class Solution:
    def rightSideView(self, root: TreeNode | None) -> List[int]:
        if not root:
            return []
        ans = []        
        q = [root]
        while q:            
            ans.append(q[-1].val)
            q = [child for node in q for child in (node.left, node.right) if child]
        return ans