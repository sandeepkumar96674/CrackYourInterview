class Solution:
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        vis= V*[0]
        res=[]
        def dfs(node):
           if vis[node]==1:
               return
           vis[node]=1
           res.append(node)
           
           for val in adj[node]:
               dfs(val)
        dfs(0)
        return res