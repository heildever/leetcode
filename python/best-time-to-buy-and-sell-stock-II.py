# question can be found on leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Greedy
        profit = 0
        for idx, price in enumerate(prices)[:-1]:
            if price[idx + 1] > price:
                profit += price[idx + 1] - price

        return profit

        # Dynamic with local maxima
        profit, sell_price = 0, float("-inf")
        for price in prices:
            sell_price = max(sell_price, profit - price)
            profit = max(profit, sell_price + price)

        return profit
