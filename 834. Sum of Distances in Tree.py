class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        to = [[] for _ in range(n)]
        for u, v in edges:
            to[u].append(v)
            to[v].append(u)
        ans = [0] * n
        size = [1] * n
        def dfs(u=0, par=-1):
            d = 0
            for v in to[u]:
                if v == par:
                    continue
                ret = dfs(v, u)
                d += ret + size[v]
                size[u] += size[v]
            return d
        ans[0] = dfs()
        def solve(u=0, par=-1):
            for v in to[u]:
                if v == par:
                    continue
                ans[v] = ans[u] + n - 2 * size[v]
                solve(v, u)
        solve()
        return ans