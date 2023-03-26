class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy_min = prices.copy()
        sell_max = prices.copy()


        for i in range(1, len(prices)): 
            buy_min[i] = min(buy_min[i], buy_min[i - 1])

        for i in range(len(prices) - 2, -1, -1):
            sell_max[i] = max(sell_max[i], sell_max[i + 1])


        res = 0
        for i in range(0, len(buy_min) - 1):
            res = max(res, sell_max[i + 1] - buy_min[i])

        return res
