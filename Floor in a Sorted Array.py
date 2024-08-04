class Solution:
    def findFloor(self,A,N,X):
        #Your code here
        low=0
        high=N-1
        ans=-1
        while(low<=high):
            mid=(low+high)//2
            if(A[mid]==X):
                return mid
            elif(A[mid]<X):
                low=mid+1
                ans=mid
            else:
                high=mid-1
        
        return ans