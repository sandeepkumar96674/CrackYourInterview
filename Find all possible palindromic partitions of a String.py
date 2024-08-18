class Solution:
    def allPalindromicPerms(self, S):
        n=len(S)
        
        def pal(i,j):
            while(i<=j):
                if(S[i]!=S[j]):
                    return False
                i+=1
                j-=1
            return True
        res = []
        dp = [] 
        def solver(ind):
            if(ind>=n):
                res.append(dp[:])
                return
            for i in range(ind,n):
                if(pal(ind,i)):
                    dp.append(S[ind:i+1])
                    solver(i+1)
                    dp.pop()
        solver(0)
        return res