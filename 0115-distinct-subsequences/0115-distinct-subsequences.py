class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        l1 = len(s)
        l2 = len(t)
        # return self.solveUsingRecursion(l1 - 1, l2 - 1, s, t) # 0-based indexing

        # return self.solveUsingRecursion1(l1, l2, s, t) # 1-based indexing

        # dp = [[-1 for _ in range(l2 + 1)] for _ in range(l1 + 1)]

        # return self.solveUsingMemoization(l1, l2, s, t, dp) # 1-based indexing

        # return self.solveUsingTabulation(s, t, l1, l2)

        # return self.solveUsingSpaceOptimization1(s, t, l1, l2) # 2 Array Space Optimization
        return self.solveUsingSpaceOptimization1(s, t, l1, l2) # 1 Array Space Optimization




    # TC: O(2^l1 * 2^l2) (exponential)
    # SC: O(l1 + l2) (recursion stack space)
    def solveUsingRecursion(self, ind1, ind2, s, t): # 0-based indexing
        # Base Case

        if ind2 < 0:
            return 1

        if ind1 < 0:
            return 0

        # If Matching Characters, 2 choices (Pick or Not pick)
        if s[ind1] == t[ind2]:
            return self.solveUsingRecursion(ind1 - 1, ind2 - 1, s, t) + self.solveUsingRecursion(ind1 - 1, ind2, s, t)  

        # Not Matching Characters, cannot pick, move ind1
        return self.solveUsingRecursion(ind1 - 1, ind2, s, t) 

    # TC: O(2^l1 * 2^l2) (exponential)
    # SC: O(l1 + l2) (recursion stack space)
    def solveUsingRecursion1(self, ind1, ind2, s, t): # 1-based indexing
        # Base Case

        if ind2 == 0:
            return 1

        if ind1 == 0:
            return 0

        # If Matching Characters, 2 choices (Pick or Not pick)
        if s[ind1 - 1] == t[ind2 - 1]: # 1-based indexing
            return self.solveUsingRecursion1(ind1 - 1, ind2 - 1, s, t) + self.solveUsingRecursion1(ind1 - 1, ind2, s, t)  

        # Not Matching Characters, cannot pick, move ind1
        return self.solveUsingRecursion1(ind1 - 1, ind2, s, t) 

    # TC: O(l1 * l2) 
    # SC: O(l1 * l2) + O(l1 + l2) (recursion stack space)
    def solveUsingMemoization(self, ind1, ind2, s, t, dp): # 1-based indexing
        # Base Case

        if ind2 == 0:
            return 1

        if ind1 == 0:
            return 0

        if dp[ind1][ind2] != -1:
            return dp[ind1][ind2]

        # If Matching Characters, 2 choices (Pick or Not pick)
        if s[ind1 - 1] == t[ind2 - 1]: # 1-based indexing
            dp[ind1][ind2] = self.solveUsingMemoization(ind1 - 1, ind2 - 1, s, t, dp) + self.solveUsingMemoization(ind1 - 1, ind2, s, t, dp)     
        else:
            # Not Matching Characters, cannot pick, move ind1
            dp[ind1][ind2] = self.solveUsingMemoization(ind1 - 1, ind2, s, t, dp) 

        return dp[ind1][ind2]


    # TC: O(l1 * l2) 
    # SC: O(l1 * l2) 
    def solveUsingTabulation(self, s, t, l1, l2):
        dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]

        # Base Case
        for ind1 in range(l1 + 1):
            dp[ind1][0] = 1

        # for ind2 in range(1, l2 + 2):
        #     dp[0][ind2] = 0

        for ind1 in range(1, l1 + 1):
            for ind2 in range(1, l2 + 1):
                # If Matching Characters, 2 choices (Pick or Not pick)
                if s[ind1 - 1] == t[ind2 - 1]: # 1-based indexing
                    dp[ind1][ind2] = dp[ind1 - 1][ind2 - 1] + dp[ind1 - 1][ind2]      
                else:
                    # Not Matching Characters, cannot pick, move ind1
                    dp[ind1][ind2] = dp[ind1 - 1][ind2] 


        return dp[l1][l2]


    # TC: O(l1 * l2) 
    # SC: O(l2) 
    def solveUsingSpaceOptimization1(self, s, t, l1, l2): # 2 Array Space Optimization
        prev = [0 for _ in range(l2 + 1)] 

        # Base Case
        prev[0] = 1

        for ind1 in range(1, l1 + 1):
            curr = [0 for _ in range(l2 + 1)] 
            curr[0] = 1
            for ind2 in range(1, l2 + 1):
                # If Matching Characters, 2 choices (Pick or Not pick)
                if s[ind1 - 1] == t[ind2 - 1]: # 1-based indexing
                    curr[ind2] = prev[ind2 - 1] + prev[ind2]      
                else:
                    # Not Matching Characters, cannot pick, move ind1
                    curr[ind2] = prev[ind2] 

            prev = curr

        return prev[l2]  

    # TC: O(l1 * l2) 
    # SC: O(l2) 
    def solveUsingSpaceOptimization2(self, s, t, l1, l2): # 1 Array Space Optimization
        prev = [0 for _ in range(l2 + 1)] 

        # Base Case
        prev[0] = 1

        for ind1 in range(1, l1 + 1):
            for ind2 in range(l2, -1, -1):
                # If Matching Characters, 2 choices (Pick or Not pick)
                if s[ind1 - 1] == t[ind2 - 1]: # 1-based indexing
                    prev[ind2] = prev[ind2 - 1] + prev[ind2]      
                else:
                    # Not Matching Characters, cannot pick, move ind1
                    prev[ind2] = prev[ind2] 

        return prev[l2]  

