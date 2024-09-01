class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1 for _ in range(n)]

        # return self.solveUsingRecursion(n - 1, nums)
        # return self.solveUsingMemoization(n - 1, nums, dp)
        # return self.solveUsingTabulation(nums, dp)
        return self.solveUsingSpaceOptimization(nums, dp)

    # TC: O(2 ^ n) (exponential)
    # SC: O(n) (recursion stack space)

    def solveUsingRecursion(self, ind, nums):
        # Base Case
        if ind == 0:
            return nums[ind]

        if ind < 0:
            return 0

        # Pick (If we pick this element, then we will skip its next element as to avoid adjacents)
        pick = nums[ind] + self.solveUsingRecursion(ind - 2, nums)

        # Not Pick
        notPick = 0 + self.solveUsingRecursion(ind - 1, nums)

        return max(pick, notPick)


    # TC: O(n)
    # SC: O(n) (dp array and recursion stack space)
    def solveUsingMemoization(self, ind, nums, dp):
        # Base Case
        if ind == 0:
            return nums[ind]

        if ind < 0:
            return 0

        if dp[ind] != -1:
            return dp[ind]

        # Pick (If we pick this element, then we will skip its next element as to avoid adjacents)
        pick = nums[ind] + self.solveUsingMemoization(ind - 2, nums, dp)

        # Not Pick
        notPick = 0 + self.solveUsingMemoization(ind - 1, nums, dp)

        dp[ind] = max(pick, notPick)
        return dp[ind]


    # TC: O(n)
    # SC: O(n) (dp array)

    def solveUsingTabulation(self, nums, dp):
        n = len(nums)

        # Base Case
        dp[0] = nums[0]

        for ind in range(1, n):
            # Pick (If we pick this element, then we will skip its next element as to avoid adjacents)
            pick = nums[ind] 
            if ind > 1:
                pick += dp[ind - 2]

            # Not Pick
            notPick = 0 + dp[ind - 1]

            dp[ind] = max(pick, notPick)
        
        return dp[n - 1]


    # TC: O(n)
    # SC: O(1)
    def solveUsingSpaceOptimization(self, nums, dp):
        n = len(nums)

        prev = nums[0]
        prev2 = 0
        curr = 0

        for ind in range(1, n):
            
            # Pick (If we pick this element, then we will skip its next element as to avoid adjacents)
            pick = nums[ind]
            if ind > 1:
                pick += prev2

            # Not Pick
            notPick = 0 + prev

            curr = max(pick, notPick)

            # Set the variables for next iteration
            prev2 = prev
            prev = curr

        return prev # Note: Can also return curr here

            




        



        



        