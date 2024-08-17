class Solution:
  def maxCoins(self, nums: List[int]) -> int:
    nums = [1] + [x for x in nums if x] + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]
    for i in range(n-3, -1, -1):
      for j in range(i+2, n):
        temp = nums[i] * nums[j]
        dp[i][j] = max(temp * nums[k] + dp[i][k] + dp[k][j] for k in range(i+1, j))
    return dp[0][-1]