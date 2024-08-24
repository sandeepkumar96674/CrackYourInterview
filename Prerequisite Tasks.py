class Solution:
    def isPossible(self,N,P,prerequisites):
        adj = [[] for i in range(N)]
        for i in range(P):
            adj[prerequisites[i][1]].append(prerequisites[i][0])
        ind = [0 for i in range(N)]
        for a in adj:
            for i in a:
                ind[i] += 1
        s = [i for i in range(N) if ind[i] == 0]
        c = 0
        while len(s) > 0:
            node = s.pop(0)
            for i in adj[node]:
                ind[i] -= 1
                if ind[i] == 0:
                    s.append(i)
            c += 1
        return True if c == N else False