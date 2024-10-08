class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = [] #initialize the blank stack
        for i, n in enumerate(nums):
            while stack and stack[-1] > n and len(nums) - i > k - len(stack):
                stack.pop()
            stack.append(n)
        return stack[:k]