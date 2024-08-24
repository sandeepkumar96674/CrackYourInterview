class Solution:
    def isNegativeWeightCycle(self, n, edges):
        dist=[None]*n
        for i in range(n-1):
            for u,v,w in edges:
                du = dist[u] if dist[u] is not None else 0
                if(dist[v] is None or du + w <dist[v]):
                    dist[v]=du + w
        for u,v,w in edges:
            du = dist[u] if dist[u] is not None else 0
            if(dist[v] is not None and du+w<dist[v]):
                return 1
        return 0