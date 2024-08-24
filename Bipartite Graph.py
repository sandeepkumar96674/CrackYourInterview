from collections import deque
class Solution:
    
    def bfs(self, V, start, adj, color):
        q = deque()
        
        q.append(start)
        color[start] = 0
        
        while q:
            v = q.popleft()
            for adjac in adj[v]:
                if color[adjac]==-1: 
                    q.append(adjac)
                    if color[v]==0:  
                        color[adjac]=1
                    else:
                        color[adjac]=0
                elif color[adjac]==color[v]:   
                    return False
        return True
    def isBipartite(self, V, adj):
        color = [-1]*V
        
        for i in range(V):
            if color[i]==-1:
                if self.bfs(V, i, adj, color)==False:
                    return False
        return True