class Solution:
    def findPages(self,n ,arr ,m):
        if m>n:return -1
        def f(i):
            st=1
            s=0
            for j in arr:
                if s+j<=i:
                    s+=j
                else:
                    st+=1
                    if st>m or j>i:
                        return False
                    s=j
            return True
        l=max(arr)
        r=sum(arr)
        ans=-1
        while l<=r:
            mid=(l+r)//2
            if f(mid):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans