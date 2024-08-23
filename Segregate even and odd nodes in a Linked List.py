class Solution:
    def divide(self, head):
        # code here
        ohead = None
        ehead = None
        oend = None
        eend = None
        curr = head
        while curr:
            if curr.data%2==0:
                if not ehead:
                    ehead = curr
                    eend = curr
                else:
                    eend.next = curr
                    eend = eend.next
            else:
                if not ohead:
                    ohead = curr
                    oend = curr
                else:
                    oend.next = curr
                    oend = oend.next
            curr = curr.next
        if not ohead or not ehead:
            return head
        eend.next = ohead
        oend.next = None
        return ehead