from collections import deque
class Solution:
    def topoSort(self, V, adj):
        indegree =[0] * V
        topo = []
        for u in range(V):
            for v in adj[u]:
                indegree[v]+=1
        q = deque([i for i in range(V) if indegree[i]==0])
        while q:
            u = q.popleft()
            topo.append(u)
            for v in adj[u]:
                indegree[v]-=1
                if indegree[v]==0:
                    q.append(v)
        return topo if len(topo)==V else []