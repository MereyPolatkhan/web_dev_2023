class Solution:
    def maxProfit(self, prices: list[int]) -> int:  
        mn = prices[0]
        mx = prices[0]
        res = 0

        for i in range(len(prices)):
            pass 