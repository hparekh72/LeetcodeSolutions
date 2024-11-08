# Brute Force
# 1) Generate all the subsequences. (Using Recursion or Power Set {TC: O(2^n)})
# 2) Check for increase
# 3) Store the longest among them

# Subsequence -> So think in the direction of pick and not-pick

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # return self.solveUsingRecursion(0, -1, nums)

        # n = len(nums)
        # dp = [[-1 for _ in range(n + 1)] for _ in range(n)]
        # return self.solveUsingMemoization(0, -1, nums, dp)

        # return self.solveUsingTabulation(nums)
        # return self.solveUsingSpaceOptimization(nums)

        # return self.solveLIS(nums)
        # return self.printLIS(nums)

        return self.lengthOfLISUingBS(nums)
    
    # TC: O(2^n) 
    # SC: O(n) (recursion stack space)
    def solveUsingRecursion(self, ind, prev_ind, nums): 
        # Base Case
        if ind == len(nums):
            return 0

        # Not Pick
        notPick = 0 + self.solveUsingRecursion(ind + 1, prev_ind, nums)
        # Pick
        pick = float('-inf')
        if prev_ind == -1 or nums[ind] > nums[prev_ind]:
            pick = 1 + self.solveUsingRecursion(ind + 1, ind, nums)
        
        return max(pick, notPick)

    # TC: O(n * n)
    # SC: O(n * n) + O(n)(recursion stack space)
                      
    # Here, we did a co-ordinate change inorder to store the prev_ind from (-1, n-1) in dp array. (Since, we cannot store -ve indexes in an array)
    # After co-ordinate change, the prev_ind will range from (0, n) in dp array.

    def solveUsingMemoization(self, ind, prev_ind, nums, dp):
        # Base Case
        if ind == len(nums):
            return 0

        if dp[ind][prev_ind + 1] != -1:
            return dp[ind][prev_ind + 1]

        # Not Pick
        notPick = 0 + self.solveUsingMemoization(ind + 1, prev_ind, nums, dp)
        # Pick
        pick = float('-inf')
        if prev_ind == -1 or nums[ind] > nums[prev_ind]:
            pick = 1 + self.solveUsingMemoization(ind + 1, ind, nums, dp)

        dp[ind][prev_ind + 1] = max(pick, notPick)
        return dp[ind][prev_ind + 1]

    # Note as the name suggest prev_ind(previous index), it will be ind(current index) - 1
    # TC: O(n * n)
    # SC: O(n * n)
    def solveUsingTabulation(self, nums):
        n = len(nums)                               
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]  

        # Base case is done as the dp matrix is initialized with 0

        for ind in range(n-1, -1, -1):
            # Since, prev_ind ranges from (-1 to n-1) in recursion. And do cordinate change(reason is mentioned above).
            for prev_ind in range(ind-1, -2, -1): 
                # Not Pick
                notPick = 0 + dp[ind + 1][prev_ind + 1]
                # Pick
                pick = float('-inf')
                if prev_ind == -1 or nums[ind] > nums[prev_ind]:
                    pick = 1 + dp[ind + 1][ind + 1] 

                dp[ind][prev_ind + 1] = max(pick, notPick)
        
        return dp[0][-1 + 1] # dp[ind][prev_ind + 1]


    # Note as the name suggest prev_ind(previous index), it will be ind(current index) - 1
    # TC: O(n * n)
    # SC: O(n)
    def solveUsingSpaceOptimization(self, nums):
        n = len(nums)                               
        front = [0 for _ in range(n + 1)]  

        # Base case is done as the dp matrix is initialized with 0

        for ind in range(n-1, -1, -1):
            curr = [0 for _ in range(n + 1)]  
            # Since, prev_ind ranges from (-1 to n-1) in recursion. And do cordinate change(reason is mentioned above).
            for prev_ind in range(ind-1, -2, -1): 
                # Not Pick
                notPick = 0 + front[prev_ind + 1]
                # Pick
                pick = float('-inf')
                if prev_ind == -1 or nums[ind] > nums[prev_ind]:
                    pick = 1 + front[ind + 1] 

                curr[prev_ind + 1] = max(pick, notPick)
            front = curr
        
        return front[-1 + 1] 


    # TC: O(n * n)
    # SC: O(n)
    def solveLIS(self, nums):
        n = len(nums)
        dp = [1 for _ in range(n)]
        lengthOfLIS = 0

        for ind in range(n):
            for prev_ind in range(ind):
                if nums[prev_ind] < nums[ind]:
                    dp[ind] = max(dp[ind], 1 + dp[prev_ind])
            lengthOfLIS = max(lengthOfLIS, dp[ind])

        return lengthOfLIS
            
    # Print the LIS
    # TC: O(n * n) + O(n) (printing the list)
    # SC: O(n) + O(n) ~ O(n)
    def printLIS(self, nums):
        n = len(nums)
        dp = [1 for _ in range(n)]
        hashArr = []
        
        lengthOfLIS = 0
        lastIndex = 0

        for ind in range(n):
            hashArr.append(ind)
            for prev_ind in range(ind):
                if nums[prev_ind] < nums[ind] and (1 + dp[prev_ind]) > dp[ind]:
                    dp[ind] = 1 + dp[prev_ind]
                    hashArr[ind] = prev_ind
            if dp[ind] > lengthOfLIS:
                lengthOfLIS = dp[ind]
                lastIndex = ind

        res = []
        res.append(nums[lastIndex])
        
        # Backtrack                                   

        while hashArr[lastIndex] != lastIndex:
            lastIndex = hashArr[lastIndex]
            res.append(nums[lastIndex])

        res.reverse()
        # print(res)

        return lengthOfLIS


    # Binary Search Approach
    # 1. Find nums[ind] (if possible) OR 2. Find first element grater than nums[ind] (lower bound in C++ and bisect_left in Python)

    # Binary Search (Simplified explanation)
    # If at that number or at first element after that number
    # eg: num = 4
    # If at number 4(if present) or at first element after 4

    # TC: O(nlogn)
    # SC: O(n)
    def lengthOfLISUingBS(self, nums):
        n = len(nums)
        temp = [] # Initialize temp list to store the increasing subsequence
        lengthOfLIS = 0

        for num in nums:
            # If num is greater than the last element in temp, append it
            if len(temp) == 0 or num > temp[-1]:
                temp.append(num)
                lengthOfLIS += 1
            else:
                # Find the index to replace in temp (like lower_bound in C++)
                index = bisect.bisect_left(temp, num)
                temp[index] = num

        return lengthOfLIS




        
        
 

        






        