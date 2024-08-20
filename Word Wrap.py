class Solution:
    def solveWordWrap(self, nums, k):
        #Code here
        def solve(cur,spaces,dp):
            if cur==len(nums):
                return 0
            if dp[cur][spaces]!=-1:
                return dp[cur][spaces]
            newSp=spaces+1+nums[cur]
            a=float('inf')
            if newSp<=k:
                a=solve(cur+1,newSp,dp)
            b=solve(cur+1,nums[cur],dp)+((k-spaces)*(k-spaces))
            dp[cur][spaces]=min(a,b)
            return dp[cur][spaces]
        n=len(nums)
        dp=[[-1]*(k+1) for _ in range(n+1)]
        return solve(1,nums[0],dp)