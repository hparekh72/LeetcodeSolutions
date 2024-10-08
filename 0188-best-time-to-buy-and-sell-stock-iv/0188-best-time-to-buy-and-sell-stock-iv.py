class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # return self.solveUsingRecursion(0, 1, k, prices)

        # n = len(prices)
        # dp = [[[-1 for _ in range(k+1)] for _ in range(2)] for _ in range(n)]
        # return self.solveUsingMemoization(0, 1, k, prices, dp)

        # return self.solveUsingTabulation(prices, k)
        return self.solveUsingSpaceOptimization(prices, k) 

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


    # TC: O(n * 2 * k)
    # SC: O(n * 2 * k) + O(n) (recursion stack space)

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

    # TC: O(n * 2 * k)
    # SC: O(n * 2 * k) 
    def solveUsingTabulation(self, prices, k):
        n = len(prices)
        capacity = k
        dp = [[[0 for _ in range(k + 1)] for _ in range(2)] for _ in range(n + 1)]

        # The base case is already covered as the DP array is initialized to 0

        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                for capacity in range(1, k + 1):
                    profit = 0
                    if buy:
                        # Buy: (2 choices: Can buy, Cannot buy)
                        profit = max(-prices[ind] + dp[ind + 1][0][capacity], 0 + dp[ind + 1][1][capacity])
                    else:
                        # Sell: (2 choices: Can sell, Cannot sell)
                        profit = max(prices[ind] + dp[ind + 1][1][capacity - 1], 0 + dp[ind + 1][0][capacity])

                    dp[ind][buy][capacity] = profit
        return dp[0][1][k]


    # TC: O(n * 2 * k)
    # SC: O(2 * k) 

    def solveUsingSpaceOptimization(self, prices, k):
        n = len(prices)
        capacity = k
        front = [[0 for _ in range(k + 1)] for _ in range(2)]

        # The base case is already covered as the DP array is initialized to 0

        for ind in range(n - 1, -1, -1):
            curr = [[0 for _ in range(k + 1)] for _ in range(2)]
            for buy in range(2):
                for capacity in range(1, k + 1):
                    profit = 0
                    if buy:
                        # Buy: (2 choices: Can buy, Cannot buy)
                        profit = max(-prices[ind] + front[0][capacity], 0 + front[1][capacity])
                    else:
                        # Sell: (2 choices: Can sell, Cannot sell)
                        profit = max(prices[ind] + front[1][capacity - 1], 0 + front[0][capacity])
                    curr[buy][capacity] = profit
                    
            front = curr
        return front[1][k]  




