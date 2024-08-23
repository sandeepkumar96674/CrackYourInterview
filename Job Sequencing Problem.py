class Solution:
    def JobScheduling(self,Jobs,n):
        
        Jobs.sort(reverse=True,key = lambda x:x.profit)
        flag=[False]*n
        count,maxprofit=0,0
        for i in range(n):
            for j in range(Jobs[i].deadline -1,-1,-1):
                if flag[j] == False:
                    count +=1
                    maxprofit += Jobs[i].profit
                    flag[j] = True
                    break
        return [count,maxprofit]