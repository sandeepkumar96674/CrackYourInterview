class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        l =[]
        while curr:
            l.append(curr.val)
            curr = curr.next
        l.sort()
        curr = head
        for i in l:
            curr.val = i
            curr = curr.next
        return head