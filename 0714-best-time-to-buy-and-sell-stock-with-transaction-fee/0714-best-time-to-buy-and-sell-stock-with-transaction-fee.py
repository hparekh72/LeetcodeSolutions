class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # return self.solveUsingRecursion(0, 1, prices, fee)

        n = len(prices)
        dp = [[-1 for _ in range(2)] for _ in range(n)]
        return self.solveUsingMemoization(0, 1, prices, fee, dp)

    # Buy -> 1
    # Cannot Buy -> 0

    # TC: O(2^n)
    # SC: O(n) (recursion stack space)
    def solveUsingRecursion(self, ind, buy, prices, fee):
        # Base Case
        if ind == len(prices):
            return 0

        profit = 0
        if buy:
            # Buy: 2 choices (Can Buy, Cannot Buy)
            profit = max(-prices[ind] + self.solveUsingRecursion(ind + 1, 0, prices, fee),  self.solveUsingRecursion(ind + 1, 1, prices, fee))
        else:
            # Sell: 2 choices (Can Sell, Cannot Sell)
            profit = max(prices[ind] - fee + self.solveUsingRecursion(ind + 1, 1, prices, fee), 
            self.solveUsingRecursion(ind + 1, 0, prices, fee))

        return profit
    
    # TC: O(n * 2)
    # SC: O(n * 2) + O(n) (recursion stack space)
    def solveUsingMemoization(self, ind, buy, prices, fee, dp):
        # Base Case
        if ind == len(prices):
            return 0

        if dp[ind][buy] != -1:
            return dp[ind][buy]

        profit = 0
        if buy:
            # Buy: 2 choices (Can Buy, Cannot Buy)
            profit = max(-prices[ind] + self.solveUsingMemoization(ind + 1, 0, prices, fee, dp),  self.solveUsingMemoization(ind + 1, 1, prices, fee, dp))
        else:
            # Sell: 2 choices (Can Sell, Cannot Sell)
            profit = max(prices[ind] - fee + self.solveUsingMemoization(ind + 1, 1, prices, fee, dp), 
            self.solveUsingMemoization(ind + 1, 0, prices, fee, dp))

        dp[ind][buy] = profit 
        return dp[ind][buy]

        