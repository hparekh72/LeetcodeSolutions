class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # return self.solveUsingRecursion(0, 1, 2, prices)

        # n = len(prices)
        # dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)]
        # return self.solveUsingMemoization(0, 1, 2, prices, dp)

        return self.solveUsingTabulation(prices)


    # Buy = 1 -> Can Buy,
    # Buy = 0 -> Cannot Buy


    # TC: O(2^n)
    # SC: O(n) (recursion stack space)
    def solveUsingRecursion(self, ind, buy, capacity, prices):
        # Base Case
        if ind == len(prices) or capacity == 0:
            return 0

        profit = 0
        if buy:
            # Buy: (2 choices: Can buy, Cannot buy)
            profit = max(
                -prices[ind] + self.solveUsingRecursion(ind + 1, 0, capacity, prices), 
            0 + self.solveUsingRecursion(ind + 1, 1, capacity, prices))
        else:
            # Sell: (2 choices: Can sell, Cannot sell)
            profit = max(
                prices[ind] + self.solveUsingRecursion(ind + 1, 1, capacity - 1, prices), 
                0 + self.solveUsingRecursion(ind + 1, 0, capacity, prices))

        return profit


    # TC: O(n * 2 * 3)
    # SC: O(n * 2 * 3) + O(n) (recursion stack space)

    def solveUsingMemoization(self, ind, buy, capacity, prices, dp):
        # Base Case
        if ind == len(prices) or capacity == 0:
            return 0

        if dp[ind][buy][capacity] != -1:
            return dp[ind][buy][capacity]

        profit = 0
        if buy:
            # Buy: (2 choices: Can buy, Cannot buy)
            profit = max(
                -prices[ind] + self.solveUsingMemoization(ind + 1, 0, capacity, prices, dp), 
            0 + self.solveUsingMemoization(ind + 1, 1, capacity, prices, dp))
        else:
            # Sell: (2 choices: Can sell, Cannot sell)
            profit = max(
                prices[ind] + self.solveUsingMemoization(ind + 1, 1, capacity - 1, prices, dp), 
                0 + self.solveUsingMemoization(ind + 1, 0, capacity, prices, dp))

        dp[ind][buy][capacity] = profit
        return dp[ind][buy][capacity]


    # TC: O(n * 2 * 3)
    # SC: O(n * 2 * 3) 
    def solveUsingTabulation(self, prices):
        n = len(prices)
        capacity = 2
        dp = dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n + 1)]

        # The base case is already covered as the DP array is initialized to 0

        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                for capacity in range(1, 3):
                    profit = 0
                    if buy:
                        # Buy: (2 choices: Can buy, Cannot buy)
                        profit = max(-prices[ind] + dp[ind + 1][0][capacity], 0 + dp[ind + 1][1][capacity])
                    else:
                        # Sell: (2 choices: Can sell, Cannot sell)
                        profit = max(prices[ind] + dp[ind + 1][1][capacity - 1], 0 + dp[ind + 1][0][capacity])

                    dp[ind][buy][capacity] = profit
        return dp[0][1][2]
        








        