class Solution:
    def minSteps(self, m, n, d):
        if d>m and d>n:
            return -1
        def gcd(a, b):
            if b==0:
                return a
            return gcd(b, a%b)
        def function(a, b, tar):
            if a==tar or b==tar:
                return 1
            one = a
            two = 0
            step = 0
            while one!=tar and two!= tar:
                temp = min(one, b-two)
                one -= temp
                two += temp
                step += 1
                if one==0:
                    one = a
                    step+=1
                
                if two==b:
                    two = 0
                    step+=1
            return step
        if d%gcd(m, n)!=0:
            return -1
        return min(function(m, n, d), function(n, m ,d))