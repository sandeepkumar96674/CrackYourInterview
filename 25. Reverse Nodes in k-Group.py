class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return
        start = end = head
        for _ in range(k):
            if not end: return head 
            end = end.next
        newHead = self.reverse(start, end)
        start.next = self.reverseKGroup(end, k)
        return newHead
    def reverse(self, start, end):
        prev = None
        while start != end:
            start.next, start, prev = prev, start.next, start
        return prev 