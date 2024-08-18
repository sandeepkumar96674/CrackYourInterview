import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        if n == m == 1:
            return grid[0][0]
        dist = max(grid[0][0], grid[-1][-1])
        h = [(dist, 0, 0)]
        in_progress = {(0, 0)}
        while h:
            current_dist, i, j = heapq.heappop(h)
            dist = max(dist, current_dist)
            if i == n - 1 and j == m - 1:
                return dist
            for x, y in ((i - 1, j), 
                         (i + 1, j),
                         (i, j - 1),
                         (i, j + 1)):
                if (
                    0 <= x < n 
                    and 0 <= y < m 
                    and (x, y) not in in_progress
                ):
                    heapq.heappush(h, (grid[x][y], x, y))
                    in_progress.add((x, y))