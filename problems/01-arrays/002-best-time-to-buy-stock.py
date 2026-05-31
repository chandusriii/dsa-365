"""
Problem: Best Time to Buy and Sell Stock
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Difficulty: Easy

You are given an array prices where prices[i] is the price of a stock on day i.
Choose one day to buy and a later day to sell to maximize profit.
Return the maximum profit. If no profit is possible, return 0.

Approach: Single Pass
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            potential_profit = price - min_price
            max_profit = max(max_profit, potential_profit)
            min_price = min(min_price, price)

        return max_profit


def test():
    sol = Solution()
    assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert sol.maxProfit([7, 6, 4, 3, 1]) == 0
    assert sol.maxProfit([1, 2, 3, 4, 5]) == 4
    assert sol.maxProfit([]) == 0
    print("All tests passed!")


if __name__ == "__main__":
    test()
