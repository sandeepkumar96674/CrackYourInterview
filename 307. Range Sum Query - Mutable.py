class NumArray:
    def __init__(self, nums):
        self.nums = nums
        self.sum = sum(nums)
    def update(self, index, val):
        self.sum += val-self.nums[index]
        self.nums[index] = val
    def sumRange(self, left, right):
        return self.sum - sum(self.nums[0:left]) - sum(self.nums[right+1:])