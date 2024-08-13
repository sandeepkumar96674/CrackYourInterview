class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def Inorder(root):
            if(root==None):
                return
            Inorder(root.left)
            res.append(root)
            values.append(root.val)
            Inorder(root.right)
        
        res=[]
        values=[]
        Inorder(root)
        values.sort()
        for i in range(len(values)):
            res[i].val=values[i]