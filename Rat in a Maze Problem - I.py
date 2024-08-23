from typing import List

class Solution:
    def findPath(self, mat: List[List[int]]) -> List[str]:
        def solve(i,j,temp):
            if i<0 or j<0 or i>=n or j>=m or mat[i][j]==0:
                return
            if i==n-1 and j==n-1:
                ans.append(''.join(temp))
                return
            mat[i][j]=0
            temp.append('D')
            solve(i+1,j,temp)
            temp.pop()
            temp.append('U')
            solve(i-1,j,temp)
            temp.pop()
            temp.append('L')
            solve(i,j-1,temp)
            temp.pop()
            temp.append('R')
            solve(i,j+1,temp)
            temp.pop()
            mat[i][j]=1
            
        n = len(mat)
        m = len(mat[0])
        ans = []
        solve(0,0,[])
        return ans