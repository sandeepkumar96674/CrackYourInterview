class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        visited = {} 
        original = head
        while original:
            visited[original] = Node(original.val)
            original = original.next
        original = head
        while original:
            copied = visited[original]
            copied.next = visited.get(original.next)
            copied.random = visited.get(original.random)
            original = original.next
        return visited[head]