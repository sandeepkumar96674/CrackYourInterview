class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        res = [nums[0]]
        for num in nums[1:]:
            if num > res[-1]:
                res.append(num)
            else:
                left, right = 0, len(res) - 1
                while left < right:
                    mid = left + (right - left) // 2
                    if res[mid] < num:
                        left = mid + 1
                    else:
                        right = mid
                res[left] = num
        return len(res)