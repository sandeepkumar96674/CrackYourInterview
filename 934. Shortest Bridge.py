class Solution:
    def __init__(self):
        self.found_first_island = False
        self.first_island_grid = set()
    def dfs(self, grid, visited, x, y, n):
        if visited[x][y] or grid[x][y] == 0:
            return
        if not self.found_first_island:
            self.found_first_island = True
        visited[x][y] = True
        self.first_island_grid.add((x,y))
        for new_x, new_y in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
            if 0<= new_x < n and 0 <= new_y < n:
                self.dfs(grid, visited, new_x, new_y, n)
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False for _ in range(n)] for _ in range(n)]
        water_grids = []
        for i in range(n):
            for j in range(n):
                if self.found_first_island:
                    break
                self.dfs(grid, visited, i, j, n)
        count = 0
        queue = collections.deque(self.first_island_grid)
        while queue:
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()
                for new_i, new_j in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if (new_i, new_j) not in self.first_island_grid and (0 <= new_i < n and 0 <= new_j < n):
                        if grid[new_i][new_j] == 1:
                            return count
                        else:
                            self.first_island_grid.add((new_i, new_j))
                            queue.append((new_i, new_j))
            count += 1