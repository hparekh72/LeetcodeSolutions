class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        # ans = self.solveUsingRecursion(n - 1, amount, coins)
        # if ans == float('inf'):
        #     return -1
        # else:
        #     return ans      

        dp = [[-1 for _ in range(amount + 1)] for _ in range(n)]

        ans = self.solveUsingMemoization(n - 1, amount, coins, dp)
        if ans == float('inf'):
            return -1
        else:
            return ans

    # TC: O(2^n)
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

        pick = float('inf')
        if coins[ind] <= amount:
            pick = 1 + self.solveUsingMemoization(ind, amount - coins[ind], coins, dp)

        dp[ind][amount] = min(notPick, pick)
        return dp[ind][amount]


