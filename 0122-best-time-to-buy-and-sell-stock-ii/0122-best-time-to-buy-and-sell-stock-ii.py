class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # return self.solveUsingRecursion(0, 1, prices)

        dp = [[-1 for _ in range(2)] for _ in range(n)]
        return self.solveUsingMemoization(0, 1, prices, dp)


    # Buy = 1 -> Can Buy,
    # Buy = 0 -> Cannot Buy

    # TC: O(2^n)
    # SC: O(n) (recursion stack space)
    def solveUsingRecursion(self, ind, buy, prices):
        # Base Case
        if ind == len(prices):
            return 0

        profit = 0
        if buy: # Buy: 2 choices(Can buy, Cannot buy)
            profit = max(-prices[ind] + self.solveUsingRecursion(ind + 1, 0, prices), 0 + self.solveUsingRecursion(ind + 1, 1, prices))
        else: # Sell: 2 choices (Can sell, Cannot sell)
            profit = max(prices[ind] + self.solveUsingRecursion(ind + 1, 1, prices), 0 + self.solveUsingRecursion(ind + 1, 0, prices))

        return profit


    # TC: O(n * 2)
    # SC: O(n * 2) + O(n) (recursion stack space)
    def solveUsingMemoization(self, ind, buy, prices, dp):
        # Base Case
        if ind == len(prices):
            return 0

        if dp[ind][buy] != -1:
            return dp[ind][buy]

        # Buy
        profit = 0
        if buy: # Buy: 2 choices(Can buy, Cannot buy)
            profit = max(-prices[ind] + self.solveUsingMemoization(ind + 1, 0, prices, dp), 0 + self.solveUsingMemoization(ind + 1, 1, prices, dp))
        else: # Sell: 2 choices (Can sell, Cannot sell)
            profit = max(prices[ind] + self.solveUsingMemoization(ind + 1, 1, prices, dp), 0 + self.solveUsingMemoization(ind + 1, 0, prices, dp))

        dp[ind][buy] = profit
        return dp[ind][buy]

    
     
        
    

        
        