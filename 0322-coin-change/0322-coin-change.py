class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        # ans = self.solveUsingRecursion(n - 1, coins, amount)

        dp = [[-1 for _ in range(amount + 1)] for _ in range(n)]
        ans = self.solveUsingMemoization(n - 1, coins, amount, dp)

        if ans == float('inf'):
            return -1
        else:
            return ans

    def solveUsingRecursion(self, ind, coins, amount):
        if ind == 0:
            if amount % coins[ind] == 0:
                return amount // coins[ind]
            else:
                return float('inf')
            

        notPick = 0 + self.solveUsingRecursion(ind - 1, coins, amount)

        pick = float('inf')
        if amount >= coins[ind]: 
            pick = 1 + self.solveUsingRecursion(ind, coins, amount - coins[ind])
        
        return min(pick, notPick)


    # TC: O(amount * n) 
    # SC: O(amount * n) + O(amount) (recursion stack space)
    def solveUsingMemoization(self, ind, coins, amount, dp):
        if ind == 0:
            if amount % coins[ind] == 0:
                return amount // coins[ind]
            else:
                return float('inf')
        
        if dp[ind][amount] != -1:
            return dp[ind][amount]
            
        notPick = 0 + self.solveUsingMemoization(ind - 1, coins, amount, dp)

        pick = float('inf')
        if amount >= coins[ind]: 
            pick = 1 + self.solveUsingMemoization(ind, coins, amount - coins[ind], dp)
        
        dp[ind][amount] = min(pick, notPick)
        return dp[ind][amount]

        

    


