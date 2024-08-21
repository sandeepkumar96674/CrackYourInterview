class Solution:
    def tour(self, lis, n):
        sum_pet = 0
        sum_dist = 0
        for x, y in lis:
            sum_pet += x
            sum_dist += y
        if sum_pet < sum_dist:
            return -1
        total = 0
        res = 0
        for i in range(n):
            x, y = lis[i]
            total += x - y
            if total < 0:
                total = 0  
                res = i + 1  
        return res