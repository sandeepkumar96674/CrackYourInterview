class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return set(permutations(nums)) 