class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def cal_num(node):
            num = 0
            while node:
                num = num*10 +(node.val)
                node = node.next
            return int(num)
            
        int_1 = cal_num(l1)
        int_2 = cal_num(l2)
        int_ret = str(int_1+int_2)

        node_list = []
        for dig in int_ret:
            new_node = ListNode(int(dig))
            node_list.append(new_node)
        
        head = node_list[0]
        for j in range(len(node_list)-1):
            node_list[j].next = node_list[j+1]
        
        return head