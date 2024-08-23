from math import inf
class Solution:
    def optimalSearchTree(self, keys, freq, n):
        dp = [[0] * n for _ in range(n)]
        for d in range(n):
            for i in range(n - d):
                j = i + d
                if (i == j):
                    dp[i][j] = freq[i]
                    continue
                mn = inf;
                for r in range(i, j + 1):
                    left = dp[i][r - 1] if (r - 1) >= i else 0
                    right = dp[r + 1][j] if r + 1 <= j else 0
                    cost = left + right + sum(freq[i:j+1])
                    mn = min([mn, cost])
                dp[i][j] = mn
        return dp[0][n - 1]