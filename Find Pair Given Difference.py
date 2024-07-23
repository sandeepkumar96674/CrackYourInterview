from typing import List
class Solution:
    def findPair(self, n : int, x : int, arr : List[int]) -> int:
        for i in range(n):
            for j in range(i+1,n):
                if(abs(arr[i]-arr[j])==x):
                    return 1
        return 2