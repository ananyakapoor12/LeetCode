class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range (1, len(prices):
            if(price[i]>price[i-1]):
                max_profit += price[i]
        return max_profit
