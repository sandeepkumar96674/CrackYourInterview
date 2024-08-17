class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = [] #initializing a blank array
        for i in range(len(nums)):
            if i >= k and q[0][1] == i - k:
                q.popleft()
            while q and q[-1][0] <= nums[i]:
                q.pop()
            q.append((nums[i], i))
            if i >= k - 1:
                ans.append(q[0][0])
        return ans