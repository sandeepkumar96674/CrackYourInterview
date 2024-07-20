class Solution:
    def maxArea(self, height: List[int]) -> int:
        temp = 0
        area = 0
        j = (len(height) - 1)
        i = 0
        if j == 1:
            area = 1 * min(height)
            return area
        while i < len(height) and j > i:
            if height[i] > height[j]:
                temp = height[j] * (j-i)
                if temp > area:
                    area = temp
                j -= 1
            else:
                temp = height[i] * (j-i)
                if temp > area:
                    area = temp
                i += 1
        return area #