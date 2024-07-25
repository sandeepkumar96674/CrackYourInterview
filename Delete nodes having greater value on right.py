
'''
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

'''
class Solution:
    def compute(self,head):
        #Your code here
        if not head or not head.next:
            return head
        
        prev = None
        cur= head
        dummy=Node(0)
        temp=dummy
        while cur:
            cur1=cur.next
            yes=True
            while cur1:
                if cur.data>=cur1.data:
                    yes=True
                else:
                    yes=False
                    break
                cur1=cur1.next
            if yes:
                temp.next=cur
                temp=temp.next
            cur=cur.next
        return dummy.next    
            
                    
                
            