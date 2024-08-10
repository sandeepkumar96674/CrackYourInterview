class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMaxValue, curMinValue = 1, 1
        maxProduct = nums[0]
        for num in nums:
            curMaxProduct = curMaxValue * num
            curMinProduct = curMinValue * num
            curMaxValue = max(curMaxProduct, curMinProduct, num)
            curMinValue = min(curMaxProduct, curMinProduct, num)
            maxProduct = max(maxProduct, curMaxValue)
        return maxProduct