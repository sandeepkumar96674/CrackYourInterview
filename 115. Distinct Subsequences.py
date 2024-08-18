class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memory = {}
        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in memory:
                return memory[(i, j)]
            if s[i] == t[j]:
                memory[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                memory[(i, j)] = dfs(i + 1, j)
            return memory[(i, j)]
        return dfs(0, 0)