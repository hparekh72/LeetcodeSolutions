class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # return self.solveUsingRecursion(0, 1, prices, fee)

        # n = len(prices)
        # dp = [[-1 for _ in range(2)] for _ in range(n)]
        # return self.solveUsingMemoization(0, 1, prices, fee, dp)

        # return self.solveUsingTabulation(prices, fee)
        return self.solveUsingSpaceOptimization(prices, fee)

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



    # TC: O(n * 2)
    # SC: O(n * 2) 
    def solveUsingTabulation(self, prices, fee):
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n + 1)]

        # Base Case
        dp[n][0] = dp[n][1] = 0

        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                profit = 0 
                if buy:
                    # Buy: 2 choices (Can Buy, Cannot Buy)
                    profit = max(-prices[ind] + dp[ind + 1][0],  dp[ind + 1][1])
                else:
                    # Sell: 2 choices (Can Sell, Cannot Sell)
                    profit = max(prices[ind] - fee + dp[ind + 1][1], dp[ind + 1][0])
                
                dp[ind][buy] = profit 

        return dp[0][1] 


    # TC: O(n * 2)
    # SC: O(2) 
    def solveUsingSpaceOptimization(self, prices, fee):
        n = len(prices)
        front = [0 for _ in range(2)] 

        # Base Case
        # front[0] = front[1] = 0  (Not required)

        for ind in range(n - 1, -1, -1):
            curr = [-1 for _ in range(2)] 
            for buy in range(2):
                profit = 0 
                if buy:
                    # Buy: 2 choices (Can Buy, Cannot Buy)
                    profit = max(-prices[ind] + front[0],  front[1])
                else:
                    # Sell: 2 choices (Can Sell, Cannot Sell)
                    profit = max(prices[ind] - fee + front[1], front[0])
                
                curr[buy] = profit 
            front = curr

        return front[1]       


        