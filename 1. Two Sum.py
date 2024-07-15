class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_num = {}
        for key, val in enumerate(nums):
            if target-val in index_num:
                return [index_num[target-val], key]
            index_num[val]=key
        return []