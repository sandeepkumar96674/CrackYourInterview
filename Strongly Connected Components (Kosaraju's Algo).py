class Solution:
    def kosaraju(self, v, adj):
        stack = []
        vis = [0] * v
        
        def dfs(node, adj):
            vis[node] = 1
            for adjNode in adj[node]:
                if not vis[adjNode]:
                    dfs(adjNode, adj)
            stack.append(node)
            
        for i in range(v):
            if not vis[i]: dfs(i, adj)
            
        adjT = [[] for _ in range(v)]
        for i in range(v):
            vis[i] = 0
            for adjNode in adj[i]:
                adjT[adjNode].append(i)
        
        scc = 0
        while stack:
            node = stack.pop()
            if not vis[node]:
                scc += 1
                dfs(node, adjT)
        return scc