class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        # return self.solveUsingRecursion(n - 1, amount, coins)

        dp = [[-1 for _ in range(amount + 1)] for _ in range(n)]
        # return self.solveUsingMemoization(n - 1, amount, coins, dp)

        # return self.solveUsingTabulation(amount, coins, n)
        return self.solveUsingSpaceOptimization(amount, coins, n)


    # TC: O(2^n) (exponential)
    # SC: O(n) (recursion stack space)

    def solveUsingRecursion(self, ind, amount, coins):
        # Base Case
        if ind == 0:
            if amount % coins[0] == 0:
                return 1
            else:
                return 0

        # Not Pick
        notPick = self.solveUsingRecursion(ind - 1, amount, coins)

        # Pick
        pick = 0
        if coins[ind] <= amount:
            pick = self.solveUsingRecursion(ind, amount - coins[ind], coins)

        return pick + notPick

    # TC: O(n * amount)
    # SC: O(n * amount) + O(amount) (recursion stack space)

    def solveUsingMemoization(self, ind, amount, coins, dp):
        # Base Case
        if ind == 0:
            if amount % coins[0] == 0:
                return 1
            else:
                return 0

        if dp[ind][amount] != -1:
            return dp[ind][amount]

        # Not Pick
        notPick = self.solveUsingMemoization(ind - 1, amount, coins, dp)

        # Pick
        pick = 0
        if coins[ind] <= amount:
            pick = self.solveUsingMemoization(ind, amount - coins[ind], coins, dp)

        dp[ind][amount] = pick + notPick
        return dp[ind][amount]


    # TC: O(n * amount)
    # SC: O(n * amount) 

    def solveUsingTabulation(self, amount, coins, n):
        dp = [[0 for _ in range(amount + 1)] for _ in range(n)]

        # Base Case
        for num in range(amount + 1):
            if num % coins[0] == 0:
                dp[0][num] = 1
        
        for ind in range(1, n):
            for num in range(amount + 1):
                # Not Pick
                notPick = dp[ind - 1][num] 

                # Pick
                pick = 0
                if coins[ind] <= num:
                    pick = dp[ind][num - coins[ind]] 

                dp[ind][num] = pick + notPick
        
        return dp[n - 1][amount]


    # TC: O(n * amount)
    # SC: O(amount) 

    def solveUsingSpaceOptimization(self, amount, coins, n):
        prev = [0 for _ in range(amount + 1)] 
        
        # Base Case
        for num in range(amount + 1):
            if num % coins[0] == 0:
                prev[num] = 1
        
        for ind in range(1, n):
            curr = [0 for _ in range(amount + 1)] 
            for num in range(amount + 1):
                # Not Pick
                notPick = prev[num] 

                # Pick
                pick = 0
                if coins[ind] <= num:
                    pick = curr[num - coins[ind]] 

                curr[num] = pick + notPick

            prev = curr

        return prev[amount]

         



    
        