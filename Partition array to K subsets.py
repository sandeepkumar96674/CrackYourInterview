class Solution:
    def isKPartitionPossible(self, a, k):
        n = len(a)
        s = sum(a)
        if s%k != 0:
            return False
        t  = s//k
        memo = {}
        def solve(s,k,used):
            if k == 0:
                memo[(s,k,tuple(used))] = True
                return True
            if s == t:
                memo[(s,k,tuple(used))] = solve(0,k-1,used)
                return memo[(s,k,tuple(used))]
            
            if((s,k,tuple(used)) in memo):
                return memo[(s,k,tuple(used))]
            
            for j in range(n):
                if not used[j]:
                    used[j] = True
                    if solve(s+arr[j],k,used):
                        memo[(s,k,tuple(used))] = True
                        return True
                    used[j] = False
            memo[(s,k,tuple(used))] = False
            return False
        used = [False]*n
        return solve(0,k,used)