class Solution(object):
    def moveZeroes(self, nums):
        non_zero = 0 
        # Move all non-zero elements to the front in the array
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[non_zero] = nums[non_zero], nums[i]
                non_zero += 1
        