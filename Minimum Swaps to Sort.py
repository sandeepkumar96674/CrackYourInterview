class Solution:
    def minSwaps(self, nums):
        n = len(nums)
        arrpos = [(num, i) for i, num in enumerate(nums)]
        arrpos.sort(key=lambda it: it[0])
        visited = [False] * n
        ans = 0
        for i in range(n):
            if visited[i] or arrpos[i][1] == i:
                continue
            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = arrpos[j][1]
                cycle_size += 1
            if cycle_size > 0:
                ans += (cycle_size - 1)
        return ans