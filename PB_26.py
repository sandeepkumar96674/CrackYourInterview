class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = 1 #initialize the count value
        for b in range(1, len(nums)):
            if nums[b] != nums[b - 1]: #if the current iteration value is not equals to the fisrt value then continue the loop without any change
                nums[a] = nums[b] 
                a += 1
        return a