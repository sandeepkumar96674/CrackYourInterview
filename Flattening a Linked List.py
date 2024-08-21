class Solution:
    def mergeTwoLists(self, l1,l2):
        dummy=Node(0)
        s=dummy
        
        while l1 and l2:
            if l1.data<l2.data:
                s.bottom=l1
                s=l1
                l1=l1.bottom
            else:
                s.bottom=l2
                s=l2
                l2=l2.bottom
        if l1:
            s.bottom=l1
        if l2:
            s.bottom=l2
        return dummy.bottom
        
    def flatten(self, root):
        if not root:
            return None
        if not root.next:
            return root
        root.next=self.flatten(root.next)
        
        root = self.mergeTwoLists(root, root.next)
        
        return root