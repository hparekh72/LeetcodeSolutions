class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # return self.solveUsingRecursion(0, 1, prices)

        # dp = [[-1 for _ in range(2)] for _ in range(n)]
        # return self.solveUsingMemoization(0, 1, prices, dp)

        # return self.solveUsingTabulation(prices)
        return self.solveUsingSpaceOptimization(prices)


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


    # TC: O(n * 2)
    # SC: O(n * 2) 
    def solveUsingTabulation(self, prices):
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n + 1)]

        # Base Case
        dp[n][0] = dp[n][1] = 0

        for ind in range(n-1, -1, -1):
            for buy in range(2):
                # Buy
                profit = 0
                if buy: # Buy: 2 choices(Can buy, Cannot buy)
                    profit = max(-prices[ind] + dp[ind + 1][0], 0 + dp[ind + 1][1])
                else: # Sell: 2 choices (Can sell, Cannot sell)
                    profit = max(prices[ind] + dp[ind + 1][1], 0 + dp[ind + 1][0])

                dp[ind][buy] = profit
        return dp[0][1] 


    # TC: O(n * 2)
    # SC: O(2) 
    def solveUsingSpaceOptimization(self, prices):
        n = len(prices)
        front = [0 for _ in range(2)]

        # Base Case
        # front[0] = front[1] = 0  (Not required)

        for ind in range(n-1, -1, -1):
            curr = [0 for _ in range(2)]
            for buy in range(2):
                # Buy
                profit = 0
                if buy: # Buy: 2 choices(Can buy, Cannot buy)
                    profit = max(-prices[ind] + front[0], 0 + front[1])
                else: # Sell: 2 choices (Can sell, Cannot sell)
                    profit = max(prices[ind] + front[1], 0 + front[0])

                curr[buy] = profit
            front = curr
        return front[1]      



    




        
        

    
     
        
    

        
        