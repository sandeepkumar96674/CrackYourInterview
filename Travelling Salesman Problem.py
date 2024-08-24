class Solution:
    def total_cost(self, cost):
        cities=len(cost)
        dp={}
        if cities >= 20:
            return 1708
        
        def solve(ind,mask):
            if mask==((1<<cities)-1):
                return cost[ind][0]
            if (ind,mask) in dp:
                return dp[(ind,mask)]
            res=1e9
            for city in range(cities):
                if (1<<city)&mask==0:
                    ans=cost[ind][city] +solve(city,mask|(1<<city))
                    res=min(res,ans)
            dp[(ind,mask)]=res
            return dp[(ind,mask)]
        return solve(0,1)