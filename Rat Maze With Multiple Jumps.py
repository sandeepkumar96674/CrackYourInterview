class Solution:
    def ShortestDistance(self, matrix):
        n = len(matrix)
        ans = [[0]*n for _ in range(n)]
        def helper(i,j):
            if i == n-1 and j == n-1:
                ans[i][j] = 1
                return True
            if i>= n or j>= n or matrix[i][j] == 0:
                return False
            val = matrix[i][j]
            for a in range(1,val+1):
                if helper(i,j+a):
                    ans[i][j] = 1
                    return True
                if helper(i+a,j):
                    ans[i][j] = 1
                    return True
            return False
        if helper(0,0):
            return ans
        return [[-1]]