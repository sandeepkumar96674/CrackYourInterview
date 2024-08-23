class Solution:
    def maxLen(self, n, arr):
        d={}
        ans=0
        s=0
        for i in range(n):
            s+=arr[i]
            if s==0:
                ans=max(ans,i+1)
            if s in d:
                ans=max(ans,i-d[s])
            else:
                d[s]=i
        return ans