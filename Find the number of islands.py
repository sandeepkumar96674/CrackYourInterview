import sys
sys.setrecursionlimit(10**8)
class Solution:
    def dfs(self, r, c, grid, vis):
        n = len(grid)
        m = len(grid[0])
        vis[r][c]= True
        
        for i in range(-1,2):
            for j in range(-1,2):
                if i==0 and j==0:
                    continue
                
                dr, dc = r+i, c+j
                if 0<=dr<n and 0<=dc<m and grid[dr][dc]==1 and not vis[dr][dc]:
                    self.dfs(dr, dc, grid, vis)
            
    def numIslands(self,grid):
        #code here
        n = len(grid)
        m = len(grid[0])
        vis = [[False for _ in range(m)] for _ in range(n)]
        cnt = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and not vis[i][j]:
                    cnt += 1
                    self.dfs(i, j, grid, vis)
        return cnt