#User function Template for python3
class Solution:
    def productExceptSelf(self, nums, n):
        if n == 1: # when the number of Element is only 1.
            return [1] #return the element only
        i, temp = 1, 1
        prod = [1 for i in range(n)]
        for i in range(n):
            prod[i] = temp
            temp *= arr[i] 
        temp = 1
        for i in range(n - 1, -1, -1):
            prod[i] *= temp
            temp *= arr[i]
        return prod