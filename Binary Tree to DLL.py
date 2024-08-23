class Solution:
    def bToDLL(self,root):
        def inorder(node):
            if node is None: return
            inorder(node.left)
            if self.head is None: 
                self.head = node
            else:
                self.last.right = node
                node.left = self.last
            self.last = node
            inorder(node.right)
         
        if root is None: return None
        self.head = None
        self.last = None
        inorder(root)
        return self.head