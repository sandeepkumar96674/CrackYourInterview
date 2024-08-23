class Solution:
    def maxOfMin(self, arr, n):
        left_smaller = [-1] * n
        right_smaller = [n] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            left_smaller[i] = stack[-1] if stack else -1
            stack.append(i)
        
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            right_smaller[i] = stack[-1] if stack else n
            stack.append(i)
        
        max_of_min = [0] * n
        
        for i in range(n):
            length = right_smaller[i] - left_smaller[i] - 1
            max_of_min[length - 1] = max(max_of_min[length - 1], arr[i])
        
        for i in range(n - 2, -1, -1):
            max_of_min[i] = max(max_of_min[i], max_of_min[i + 1])
        
        return max_of_min