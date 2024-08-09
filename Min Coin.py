class Solution:
    def MinCoin(self, arr, amount):        
        N = len(arr)
        arr.sort()
        dp = {}
        def solve(amt):
            if amt==0:
                return 0
            elif amt in dp:
                return dp[amt]
            else:
                ans = float('INF')
                for coin in arr:
                    if coin<=amt:
                        ans = min(ans,1+solve(amt-coin))
                    else:
                        break 
                dp[amt] = ans 
                return ans
                
        val =  solve(amount)
        if val>=10**9+7:
            return -1 
        else:
            return val