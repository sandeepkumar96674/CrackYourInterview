class Solution:
    def countSquares(self, li: List[List[int]]) -> int:
        ans = 0
        for i in range(len(li)):
            for j in range(len(li[0])):
                if li[i][j] == 0:
                    continue
                elif i == 0 or j == 0:
                    ans += li[i][j]
                else:
                    li[i][j] = 1 + min(li[i-1][j],li[i-1][j-1],li[i][j-1])
                    ans += li[i][j]
        return ans