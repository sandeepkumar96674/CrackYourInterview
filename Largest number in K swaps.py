class Solution:
    def match(self, num, res):
        
        for i in range(len(num)):
            if res[i] > num[i]:
                return
            if res[i] < num[i]:
                
                for i in range(len(num)):
                    res[i] = num[i]
                return
    def setDigit(self, num, index, res, k):
        if k==0 or index==len(num)-1:
            self.match(num,res)
            return
        
        maxDigit = 0
        for i in range(index, len(num) ):
            maxDigit = max( maxDigit, num[i] )
        if num[index] == maxDigit:
            self.setDigit( num, index+1, res, k )
            return
        
        for i in range(index+1, len(num)):
            if num[i] == maxDigit:
                num[index] , num[i] = num[i] , num[index]
                self.setDigit(num, index+1, res, k-1);
                
                num[index] , num[i] = num[i] , num[index]
    def findMaximumNum(self, s,k):
        
        num = [ int(x) for x in s ]
        res = [ int(x) for x in s ]
        
        self.setDigit(num, 0, res, k)
        return ''.join( str(x) for x in res )