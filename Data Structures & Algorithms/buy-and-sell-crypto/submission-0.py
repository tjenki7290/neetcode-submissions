class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0 #left is buying
        R = 1 #right is selling
        #maximum profit
        max_profit = 0
        while R < len(prices):
            if prices[R] > prices[L]: #that means that it's profitable so calc profit
                profit = prices[R] - prices[L]
                max_profit = max(max_profit,profit)
            else: #if the price at the right pointer is less than the left pointer then you've found a cheaper buy price so replace
                L = R
            R += 1

        return max_profit
                



