class Solution:
    def maxProfit(self, prices: list[int]) -> int:  
        mn = prices[0]
        mx = prices[0]
        res = 0

        for i in range(len(prices)):
            if (mx > prices[i]): 
                res += (mx - mn)
                mn = mx = prices[i]
                
            else:
                mn = min(mn, prices[i])
                mx = max(mx, prices[i])
        
        res += (mx - mn)

        return res
