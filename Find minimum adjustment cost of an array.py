M = 100
class Solution:
    def minAdjustmentCost(self, arr, n, target):
        dp = [[float('inf') for _ in range(M+1)] for _ in range(n)]
        for j in range(M+1):
             dp[0][j] = abs(j - arr[0])
        for i in range(1, n):
            for j in range(M+1):
                for k in range(max(j-target,0), min(j+target,M)+1):
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + abs(arr[i]-j))
        res = min(dp[n-1])
        return res