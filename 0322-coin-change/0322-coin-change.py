class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        # ans = self.solveUsingRecursion(n - 1, coins, amount)

        # dp = [[-1 for _ in range(amount + 1)] for _ in range(n)]
        # ans = self.solveUsingMemoization(n - 1, coins, amount, dp)

        # ans = self.solveUsingTabulation(coins, amount)

        ans = self.solveUsingSpaceOptimization(coins, amount)

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

    def solveUsingTabulation(self, coins, amount):
        n = len(coins)
        dp = [[float('inf') for _ in range(amount + 1)] for _ in range(n)]

        # Base Case
        for num in range(amount + 1):
            if num % coins[0] == 0:
                dp[0][num] = num // coins[0]

        for ind in range(1, n):
            for num in range(amount + 1):
                notPick = 0 + dp[ind - 1][num]

                pick = float('inf')
                if coins[ind] <= num: 
                    pick = 1 + dp[ind][num - coins[ind]] 
                
                dp[ind][num] = min(pick, notPick)
        return dp[n - 1][amount]  

    def solveUsingSpaceOptimization(self, coins, amount):
        n = len(coins)
        prev = [float('inf') for _ in range(amount + 1)] 

        # Base Case
        for num in range(amount + 1):
            if num % coins[0] == 0:
                prev[num] = num // coins[0]

        for ind in range(1, n):
            curr = [float('inf') for _ in range(amount + 1)] 
            for num in range(amount + 1):
                notPick = 0 + prev[num]

                pick = float('inf')
                if coins[ind] <= num: 
                    pick = 1 + curr[num - coins[ind]] 
                
                curr[num] = min(pick, notPick)
            prev = curr
        return prev[amount]                   



        

    


