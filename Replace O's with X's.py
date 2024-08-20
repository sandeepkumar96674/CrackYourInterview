class Solution:
    def fill(self, n, m, mat):
        if not n or not m:
            return None 
        paths = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        res = [['X'] * m for _ in range(n)]
        def valid(i , j):
            return i >= 0 and i < n and j >= 0 and j < m
        def border(i, j):
            return i == 0 or i == n - 1 or j == 0 or j == m - 1 
        def traverse(i, j):
            if not valid(i, j) or mat[i][j] != 'O':
                return
            if res[i][j] == "O":
                return
            res[i][j] = "O"
            for path_i, path_j in paths:
                traverse(path_i + i, path_j + j)
        for i in range(n):
            for j in range(m):
                if border(i, j) and mat[i][j] == "O" and res[i][j] == "X":
                    traverse(i, j)
        return res