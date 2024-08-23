from collections import defaultdict
class Solution:
    
    def helper(self, root, k, d, currSum):
        if root == None:
            return 
        currSum += root.data
        if currSum == k:
            self.res += 1
        self.res += d[currSum - k]
        d[currSum] += 1
        self.helper(root.left, k, d, currSum)
        self.helper(root.right, k, d, currSum)
        d[currSum] -= 1
    
    def sumK(self,root,k):
        self.res = 0
        d = defaultdict(int)
        self.helper(root, k, d, 0)
        return self.res