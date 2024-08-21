class Solution:
    def missingNumber(self,arr,n):
        m=max(arr)
        l=[False]*(m+2)
        if m>=0 :
            for i in arr :
                if i>0 :
                    l[i]=True
            for j in range(1,n+2): 
                if l[j]== False :
                    return j
        return 1