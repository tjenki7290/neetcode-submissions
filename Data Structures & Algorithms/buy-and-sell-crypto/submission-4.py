class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0,0
        max_profit = 0
        while R < len(prices):
            if prices[R] == prices[L]:
                R += 1
            elif prices[R] < prices[L]:
                L = R
                R +=1
            else:
                max_profit = max(max_profit, (prices[R] - prices[L]))
                R += 1

        return max_profit




