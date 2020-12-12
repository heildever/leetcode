# question can be found on leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Dynamic Programming approach with global maxima
        max_profit = sell_price = 0
        for price in reversed(prices):
            sell_price = max(sell_price, price)
            max_profit = max(max_profit, sell_price - price)

        return max_profit
