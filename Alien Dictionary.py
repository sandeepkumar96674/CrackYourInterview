from collections import deque
from typing import List
class Solution:
    def findOrder(self, dict: List[str], N: int, K: int) -> str:
        adj = {chr(97+i):[] for i in range(26)}
        for nodeIdx in range(N-1):
            s1 = dict[nodeIdx]
            s2 = dict[nodeIdx+1]
            
            minLen = min(len(s1), len(s2))
            for idx in range(minLen):
                if(s1[idx] != s2[idx]):
                    adj[s1[idx]].append(s2[idx])
                    break
        
        def topoSort(k, adj):
            
            indegree = [0 for _ in range(k)]
            
            for node in adj:
                for ad in adj[node]:
                    indegree[ord(ad) - ord('a')] += 1
        
            q = deque([])
            
            for i in range(k):
                if(indegree[i] == 0): q.append(chr(ord('a') + i))
            
            result = []
            
            while(len(q)>0):
                node = q[0]
                q.popleft()
                result.append(node)
                
                for n in adj[node]:
                    indegree[ord(n)-ord('a')] -= 1
                    
                    if(indegree[ord(n)-ord('a')] == 0): q.append(n)
            return result
        
        return topoSort(K, adj)