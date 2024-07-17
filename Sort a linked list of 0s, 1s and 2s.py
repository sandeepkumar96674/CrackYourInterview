#User function Template for python3
'''
    Your task is to segregate the list of 
    0s,1s and 2s.
    
    Function Arguments: head of the original list.
    Return Type: head of the new list formed.

    {
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    }

'''
class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        #code here
        stack = []
        curr = head 
        while curr!=None:
            stack.append(curr.data)
            curr = curr.next 
        stack = sorted(stack)
        curr = head 
        # print(stack)
        while curr:
            curr.data = stack[-1]
            stack.pop()
            curr = curr.next
        stack = []
        curr  = head 
        while curr!=None:
            stack.append(curr.data)
            curr = curr.next 
        curr = head 
        while curr:
            curr.data = stack[-1]
            stack.pop()
            curr = curr.next 
        return head


    
