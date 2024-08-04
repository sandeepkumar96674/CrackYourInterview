from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        def bfs(node):
            q.append(node)
            vis[node]=1
            while q:
                nd=q.pop(0)
                res.append(nd)
                for it in adj[nd]:
                    if not vis[it]:
                        vis[it]=1
                        q.append(it)
        res=[]
        vis=[0]*V
        q=[]
        bfs(0)
        return res