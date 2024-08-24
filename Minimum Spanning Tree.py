import heapq
class Solution:
    def spanningTree(self, V, adj):
        li=[]
        vis=[0 for i in range(V)]
        heapq.heapify(li)
        heapq.heappush(li,(0,0))
        sm=0
        while li:
            x=heapq.heappop(li)
            d,node=x[0],x[1]
            if vis[node]==1: continue
            sm+=d
            vis[node]=1
            for ngbr in adj[node]:
                if vis[ngbr[0]]==0:
                    heapq.heappush(li,(ngbr[1],ngbr[0]))
        return sm