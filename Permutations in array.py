#User function Template for python3
class Solution:
    def isPossible(self,a, b, n, k):
    # Your code goes here
        a.sort(reverse=True)
        b.sort()
        for i in range(n):
            if a[i] + b[i] < k:
                return False
        return True