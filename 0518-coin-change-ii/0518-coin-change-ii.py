class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        # return self.solveUsingRecursion(n - 1, amount, coins)
        dp = [[-1 for _ in range(amount + 1)] for _ in range(n)]
        return self.solveUsingMemoization(n - 1, amount, coins, dp)

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

    
        