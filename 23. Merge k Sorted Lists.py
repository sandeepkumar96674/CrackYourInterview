class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        listNodes = []
        for currentNode in lists:
            while currentNode:
                listNodes.append(currentNode.val)
                currentNode = currentNode.next
        listNodes.sort()           
        dummy = ListNode()
        currentNode = dummy
        for node in listNodes:
            currentNode.next = ListNode(node)
            currentNode = currentNode.next
        return dummy.next