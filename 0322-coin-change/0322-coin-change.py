class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        # ans = self.solveUsingRecursion(n - 1, amount, coins)
        # if ans == float('inf'):
        #     return -1
        # else:
        #     return ans      

        # dp = [[-1 for _ in range(amount + 1)] for _ in range(n)]

        # ans = self.solveUsingMemoization(n - 1, amount, coins, dp)
        # if ans == float('inf'):
        #     return -1
        # else:
        #     return ans


        # ans = self.solveUsingTabulation(amount, coins, n)
        # if ans == float('inf'):
        #     return -1
        # else:
        #     return ans

        ans = self.solveUsingSpaceOptimization(amount, coins, n)
        if ans == float('inf'):
            return -1
        else:
            return ans

    # TC: O(2^n) (exponential)
    # SC: O(amount) (recursion stack space)
    def solveUsingRecursion(self, ind, amount, coins):
        # Base Case
        if ind == 0:
            if amount % coins[ind] == 0:
                return amount // coins[ind]
            else:
                return float('inf')

        # Not Pick
        notPick = 0 + self.solveUsingRecursion(ind - 1, amount, coins)

        # Pick
        pick = float('inf')
        if coins[ind] <= amount:
            pick = 1 + self.solveUsingRecursion(ind, amount - coins[ind], coins)

        return min(notPick, pick)

    # TC: O(amount * n)
    # SC: O(amount * n) + O(amount) (recursion stack space)
    def solveUsingMemoization(self, ind, amount, coins, dp):
        # Base Case
        if ind == 0:
            if amount % coins[ind] == 0:
                return amount // coins[ind]
            else:
                return float('inf')

        if dp[ind][amount] != -1:
            return dp[ind][amount]

        # Not Pick
        notPick = 0 + self.solveUsingMemoization(ind - 1, amount, coins, dp)

        # Pick
        pick = float('inf')
        if coins[ind] <= amount:
            pick = 1 + self.solveUsingMemoization(ind, amount - coins[ind], coins, dp)

        dp[ind][amount] = min(notPick, pick)
        return dp[ind][amount]


    # TC: O(amount * n)
    # SC: O(amount * n) 

    def solveUsingTabulation(self, amount, coins, n):
        dp = [[float('inf') for _ in range(amount + 1)] for _ in range(n)]

        # Base Case
        for num in range(amount + 1):
            if num % coins[0] == 0: 
                dp[0][num] = num // coins[0]

        for ind in range(1, n):
            for num in range(amount + 1):
                # Not Pick
                notPick = 0 + dp[ind - 1][num] 

                # Pick
                pick = float('inf')
                if coins[ind] <= num:
                    pick = 1 + dp[ind][num - coins[ind]]

                dp[ind][num] = min(notPick, pick)

        return dp[n - 1][amount]


    # TC: O(amount * n)
    # SC: O(amount) 

    def solveUsingSpaceOptimization(self, amount, coins, n): # Two Array (Space Optimized)
        prev = [float('inf') for _ in range(amount + 1)]

        # Base Case
        for num in range(amount + 1):
            if num % coins[0] == 0: 
                prev[num] = num // coins[0]

        for ind in range(1, n):
            curr = [float('inf') for _ in range(amount + 1)]
            for num in range(amount + 1):
                # Not Pick
                notPick = 0 + prev[num] 

                # Pick
                pick = float('inf')
                if coins[ind] <= num:
                    pick = 1 + curr[num - coins[ind]]

                curr[num] = min(notPick, pick)
            
            prev = curr

        return prev[amount]
