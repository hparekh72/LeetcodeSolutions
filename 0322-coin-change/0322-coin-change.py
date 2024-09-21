class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[-1 for _ in range(amount+1)] for _ in range(n)]

        # ans =  self.solve(n-1, amount, coins, dp)
        # if ans >= 10001:
        #     return -1
        # else:
        #     return ans

        ans =  self.solve(coins, amount)
        if ans >= 10001:
            return -1
        else:
            return ans


#    def solve(self, ind, amount, coins, dp): # ME
#         # Base Case

#         if amount == 0: 
#             return 0

#         if ind < 0:
#             return 10001

#         if dp[ind][amount] != -1:
#             return dp[ind][amount]

#         notPick = 0 + self.solve(ind - 1, amount, coins, dp)
#         pick = 10001
#         if amount >= coins[ind]:
#             pick = 1 + self.solve(ind, amount - coins[ind], coins, dp)

#         dp[ind][amount] = min(pick, notPick)
#         return dp[ind][amount] 

    # def solve(self, ind, amount, coins, dp): # Memoization
    #     # Base Case

    #     if ind == 0:
    #         if amount % coins[0] == 0:
    #             return amount//coins[0]
    #         else:
    #             return int(1e9)

    #     if dp[ind][amount] != -1:
    #         return dp[ind][amount]

    #     notPick = 0 + self.solve(ind - 1, amount, coins, dp)
    #     pick = int(1e9)
    #     if amount >= coins[ind]:
    #         pick = 1 + self.solve(ind, amount - coins[ind], coins, dp)

    #     dp[ind][amount] = min(pick, notPick)
    #     return dp[ind][amount]


    # def solve(self, coins, amount): # Tabulation
    #     # Base Case

    #     n = len(coins)
    #     dp = [[int(1e9) for _ in range(amount + 1)] for _ in range(n)]

    #     for j in range(amount + 1):
    #         if j % coins[0] == 0:
    #             dp[0][j] = j//coins[0]
        
    #     for ind in range(1, n):
    #         for j in range(amount+1):
    #             notPick = 0 + dp[ind - 1][j]
    #             pick = int(1e9)
    #             if j >= coins[ind]:
    #                 pick = 1 + dp[ind][j - coins[ind]]

    #             dp[ind][j] = min(pick, notPick)
    #     return dp[n-1][amount]

    def solve(self, coins, amount): # Space Optimized
        # Base Case
            n = len(coins)
            prev = [int(1e9) for _ in range(amount + 1)]

            for j in range(amount + 1):
                if j % coins[0] == 0:
                    prev[j] = j//coins[0]
            
            for ind in range(1, n):
                curr = [int(1e9) for _ in range(amount + 1)]
                for j in range(amount+1):
                    notPick = 0 + prev[j]
                    pick = int(1e9)
                    if j >= coins[ind]:
                        pick = 1 + curr[j - coins[ind]]

                    curr[j] = min(pick, notPick)
                prev = curr
            return prev[amount]


        