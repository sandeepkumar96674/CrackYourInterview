class Solution:
        def maximizeTheCuts(self,n,x,y,z):
        dp=[-1]*(n+1)
        dp[0]=0
        for i in range(n+1):
            if dp[i]==-1:
                continue
            if i+x<=n:
                dp[i+x]=max(dp[i]+1,dp[i+x])
            if i+y<=n:
                dp[i+y]=max(dp[i]+1,dp[i+y])
            if i+z<=n:
                dp[i+z]=max(dp[i]+1,dp[i+z])
        if dp[n]==-1:
            return 0
        return dp[n]