class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        Mask=1<<n
        powerSet=[[] for _ in range(Mask)]
        for m in range(Mask):
            for i, x in enumerate(nums):
                if m& 1<<i:
                    powerSet[m].append(x)
        return powerSet    