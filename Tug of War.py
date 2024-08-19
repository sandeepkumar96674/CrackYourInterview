from typing import List
from itertools import islice

class Solution:
    def minDifference(self, n : int, a : List[int]) -> List[List[int]]:
        def f(i, j, s1, s2):
            if j == i:
                j, s1 = 0, s1 + sum(a[:i])
            if j == 0:
                return (s1, s2)[abs(s1 - sh) > abs(s2 - sh)]
            return f(i-1, j - 1, s1 + a[i-1], f(i-1, j, s1, s2))
    
        s = sum(a)
        sh = s / 2
        s1 = f(len(a), (len(a) + 1) // 2, 0, sum(map(abs, a)))
        ss = (s1, s - s1)
        return [[min(ss)], [max(ss)]]