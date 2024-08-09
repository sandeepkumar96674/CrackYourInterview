from collections import deque
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = deque()
        start_index = 0
        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        for _ in range(k):
            stack.pop()
        while start_index < len(stack) and stack[start_index] == '0':
            start_index += 1
        
        result = ''.join(stack)[start_index:]
        return result if result else '0'
