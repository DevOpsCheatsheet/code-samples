
""" bestTimeBuySellStockII
Say you have an array for which the ith element is the price of a given 
stock on day i.

Design an algorithm to find the maximum profit. You may complete as many 
transactions as you like (ie, buy one and sell one share of the stock 
multiple times). However, you may not engage in multiple transactions at 
the same time (ie, you must sell the stock before you buy again).
"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(len(prices)-1):
            profit += max(0, prices[i+1] - prices[i])     
        return profit



