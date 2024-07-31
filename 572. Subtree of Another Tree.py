class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helpr(n1, n2, checking=False):
            if n1 is None or n2 is None:
                return n1 is n2  
            if n1.val == n2.val: 
                if helpr(n1.left, n2.left, True) and helpr(n1.right, n2.right, True):
                    return True
            return not checking and helpr(n1.left, n2) or helpr(n1.right, n2)
        return helpr(root, subRoot)