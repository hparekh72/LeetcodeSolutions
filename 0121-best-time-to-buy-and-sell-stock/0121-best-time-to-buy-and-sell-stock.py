class Solution:
    # Brute Force
    # TC: O(n ^ 2)
    # def maxProfit(self, prices: List[int]) -> int:
    #     days = len(prices)
    #     maxProfit = 0
    #     for buy in range(days):
    #         for sell in range(buy + 1, days):
    #             profit = prices[sell] - prices[buy]
    #             maxProfit = max(maxProfit, profit)

    #     return maxProfit

    # Optimal
    # TC: O(n)
    # def maxProfit(self, prices: List[int]) -> int:
    #     n = len(prices) # days
    #     maxProfit = 0       
    #     buyPrice = prices[0]
    #     for i in range(1, n):
    #         if prices[i] <= buyPrice:
    #             buyPrice = prices[i]
    #         else:
    #             sellPrice = prices[i]
    #             maxProfit = max(maxProfit, sellPrice - buyPrice)

    #     return maxProfit


    # Note: Why this is a DP problem ? Reason: As we are remembering the past(minPrice)
    # Optimal
    # TC: O(n)
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        minPrice, maxProfit = prices[0], 0

        for i in range(1, n):
            minPrice = min(minPrice, prices[i])
            maxProfit = max(maxProfit, prices[i] - minPrice)

        return maxProfit

        