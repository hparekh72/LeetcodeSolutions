# Brute Force
# 1) Generate all the subsequences. (Using Recursion or Power Set {TC: O(2^n)})
# 2) Check for increase
# 3) Store the longest among them

# Subsequence -> So think in the direction of pick and not-pick

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # return self.solveUsingRecursion(0, -1, nums)

        n = len(nums)

        # dp = [[-1 for _ in range(n + 1)] for _ in range(n)]
        # return self.solveUsingMemoization(0, -1, nums, dp)

        # return self.solveUsingTabulation(nums)

        return self.solveUsingSpaceOptimization(nums)

    def solveUsingRecursion(self, ind, prev_ind, nums):
        if ind == len(nums):
            return 0

        notPick = 0 + self.solveUsingRecursion(ind + 1, prev_ind, nums)

        pick = 0
        if prev_ind == -1 or nums[ind] > nums[prev_ind]:
            pick = 1 + self.solveUsingRecursion(ind + 1, ind, nums)

        return max(pick, notPick)

    def solveUsingMemoization(self, ind, prev_ind, nums, dp):
        if ind == len(nums):
            return 0

        if dp[ind][prev_ind] != -1:
            return dp[ind][prev_ind]

        notPick = 0 + self.solveUsingMemoization(ind + 1, prev_ind, nums, dp)

        pick = 0
        if prev_ind == -1 or nums[ind] > nums[prev_ind]:
            pick = 1 + self.solveUsingMemoization(ind + 1, ind, nums, dp)

        dp[ind][prev_ind] = max(pick, notPick)
        return dp[ind][prev_ind]
    

    # Note as the name suggest prev_ind(previous index), it will be ind(current index) - 1
    def solveUsingTabulation(self, nums):
        n = len(nums)

        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        # Base case is done as the dp matrix is initialized with 0

        for ind in range(n - 1, -1, -1):
            # Since, prev_ind ranges from (-1 to n-1) in recursion. And do cordinate change(reason is mentioned above).
            for prev_ind in range(ind - 1, -2, -1):
                notPick = 0 + dp[ind + 1][prev_ind + 1] 

                pick = 0
                if prev_ind == -1 or nums[ind] > nums[prev_ind]:
                    pick = 1 + dp[ind + 1][ind + 1] 

                dp[ind][prev_ind + 1] = max(pick, notPick)

        return dp[0][-1 + 1]

    # Note as the name suggest prev_ind(previous index), it will be ind(current index) - 1
    def solveUsingSpaceOptimization(self, nums):
        n = len(nums)

        front = [0 for _ in range(n + 1)] 

        # Base case is done as the dp matrix is initialized with 0

        for ind in range(n - 1, -1, -1):
            # Since, prev_ind ranges from (-1 to n-1) in recursion. And do cordinate change(reason is mentioned above).
            curr = [0 for _ in range(n + 1)]  
            for prev_ind in range(ind - 1, -2, -1):
                notPick = 0 + front[prev_ind + 1] 

                pick = 0
                if prev_ind == -1 or nums[ind] > nums[prev_ind]:
                    pick = 1 + front[ind + 1] 

                curr[prev_ind + 1] = max(pick, notPick)
            
            front = curr

        return front[-1 + 1]

    
        

    



        





            




        
        
 

        






        