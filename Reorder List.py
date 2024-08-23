class node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

class Solution:
    
    def reorderList(self,head):
        stack=[]
        curr=head
        while curr:
            stack.append(curr.data)
            curr=curr.next
        i=0
        j=len(stack)-1
        curr=head
        while i<=j:
            curr.data=stack[i]
            curr=curr.next
            if i!=j:
                curr.data=stack[j]
                curr=curr.next
            i+=1
            j-=1