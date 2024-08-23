from typing import List
from collections import deque
class Solution:
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visited = [False] * V
        def bfs(node):
            q = deque([(node,-1)])
            while q:
                curr,parent = q.popleft()
                visited[curr] = True
                for neighbour in adj[curr]:
                    if not visited[neighbour]:
                        q.append((neighbour,curr))
                    elif neighbour != parent:
                        return True
            return False
        for i in range(V):
            if not visited[i]:
                if bfs(i):
                    return True
        return False