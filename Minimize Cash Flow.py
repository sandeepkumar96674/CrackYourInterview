from typing import List
class Solution:
    def minCashFlow(self, transaction: List[List[int]], n: int) -> List[List[int]]:
        t = [0 for i in range(n)]
        for i in range(n):
            for j in range(n):
                t[i] -= transaction[i][j]
                t[j] += transaction[i][j]
        
        pos = [(-x,i) for i,x in enumerate(t) if x > 0]
        neg = [(x,i) for i,x in enumerate(t) if x < 0]
        
        heapify(pos) ; heapify(neg)
        t2 = [[0 for i in range(n)] for j in range(n)]
        t3 = 0
        while len(pos) > 0:
            p,i = heappop(pos)
            n,j = heappop(neg)
            p = -p
        
            if p > -n: heappush(pos, (-(p+n),i) )
            elif p < -n: heappush(neg, (p+n,j) )
            
            t2[j][i] = min(p,-n)
            t3 += 1
        return t2