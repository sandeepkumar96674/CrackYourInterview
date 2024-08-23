from typing import List

class Solution:
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        visited=set()
        pathVisited=set()
        def dfs(node):
            visited.add(node)
            pathVisited.add(node)
            for nei in adj[node]:
                if nei in pathVisited:
                        return True
                if nei not in visited:
                    if dfs(nei):
                        return True
            pathVisited.remove(node)
        for node in range(V):
            if node not in visited:
                if dfs(node):
                    return True
        return False