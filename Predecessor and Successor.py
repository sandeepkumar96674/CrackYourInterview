class Solution:
    def findPreSuc(self, root, pre, suc, key):
        curr = root
        while curr:
            if curr.key > key:
                suc.key = curr.key
                curr = curr.left
                
            else:
                curr = curr.right
        curr = root
        while curr:
            if curr.key < key:
                
                pre.key = curr.key
                curr = curr.right
                
            else:
                curr = curr.left