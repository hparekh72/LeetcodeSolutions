class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # return self.solveUsingRecursion(0, 1, 2, prices)

        n = len(prices)
        # dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)]
        # return self.solveUsingMemoization(0, 1, 2, prices, dp)

        # return self.solveUsingTabulation(prices)
        # return self.solveUsingSpaceOptimization(prices)

        # Approach 2
        # return self.solveUsingRecursion2(0, 0, prices)

        dp = [[-1 for _ in range(4)] for _ in range(n)]
        return self.solveUsingMemoization2(0, 0, prices, dp)



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
        dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n + 1)]

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


    # TC: O(n * 2 * 3)
    # SC: O(2 * 3) 

    def solveUsingSpaceOptimization(self, prices):
        n = len(prices)
        capacity = 2
        front = [[0 for _ in range(3)] for _ in range(2)]

        # The base case is already covered as the DP array is initialized to 0

        for ind in range(n - 1, -1, -1):
            curr = [[0 for _ in range(3)] for _ in range(2)]
            for buy in range(2):
                for capacity in range(1, 3):
                    profit = 0
                    if buy:
                        # Buy: (2 choices: Can buy, Cannot buy)
                        profit = max(-prices[ind] + front[0][capacity], 0 + front[1][capacity])
                    else:
                        # Sell: (2 choices: Can sell, Cannot sell)
                        profit = max(prices[ind] + front[1][capacity - 1], 0 + front[0][capacity])
                    curr[buy][capacity] = profit
                    
            front = curr
        return front[1][2]  

    # Approach 2:
    # Transactions: 0, 1, 2, 3 (0 and 2 represents "buy", 1 and 3 repreents "sell")
    # TC: O(2^n) (exponential)
    # SC: O(n) (recursion stack space)
    def solveUsingRecursion2(self, ind, transaction, prices):
        if ind == len(prices) or transaction == 4:
            return 0

        profit = 0
        if transaction % 2 == 0: # Buy (2 choices: Can buy, Cannot buy)
            profit = max(-prices[ind] + self.solveUsingRecursion2(ind + 1, transaction + 1, prices), 0 + self.solveUsingRecursion2(ind + 1, transaction, prices))
        else: # Sell (2 choices: Can Sell, Cannot Sell)
            profit = max(prices[ind] + self.solveUsingRecursion2(ind + 1, transaction + 1, prices), self.solveUsingRecursion2(ind + 1, transaction, prices))

        return profit

    # TC: O(n * 4)
    # SC: O(n * 4) + O(n) (recursion stack space)
    def solveUsingMemoization2(self, ind, transaction, prices, dp):
        if ind == len(prices) or transaction == 4:
            return 0

        if dp[ind][transaction] != -1:
            return dp[ind][transaction]

        profit = 0
        if transaction % 2 == 0: # Buy (2 choices: Can buy, Cannot buy)
            profit = max(-prices[ind] + self.solveUsingMemoization2(ind + 1, transaction + 1, prices, dp), 0 + self.solveUsingMemoization2(ind + 1, transaction, prices, dp))
        else: # Sell (2 choices: Can Sell, Cannot Sell)
            profit = max(prices[ind] + self.solveUsingMemoization2(ind + 1, transaction + 1, prices, dp), self.solveUsingMemoization2(ind + 1, transaction, prices, dp))

        dp[ind][transaction] = profit
        return dp[ind][transaction]


        








        