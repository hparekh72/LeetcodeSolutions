class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)
        # return self.solveUsingRecursion(l1 -1, l2 - 1, text1, text2) # 0 based indexing
        # return self.solveUsingRecursion1(l1, l2, text1, text2) # 1 based indexing
        
        # dp = [[-1 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        # return self.solveUsingMemoization(l1, l2, text1, text2, dp) # 1 based indexing

        return self.solveUsingTabulation(text1, text2, l1, l2)



    # TC: O(2^l1 + 2^l2)
    # SC: O(l1 + l2)
    def solveUsingRecursion(self, ind1, ind2, text1, text2):
        # Base Case
        if ind1 < 0 or ind2 < 0:
            return 0

        # Matching
        if text1[ind1] == text2[ind2]:
            return 1 + self.solveUsingRecursion(ind1 - 1, ind2 - 1, text1, text2)

        # Not Matching
        return 0 + max(self.solveUsingRecursion(ind1 - 1, ind2, text1, text2), self.solveUsingRecursion(ind1, ind2 - 1, text1, text2))

    # TC: O(2^l1 + 2^l2)
    # SC: O(l1 + l2)
    def solveUsingRecursion1(self, ind1, ind2, text1, text2):
        # Base Case
        if ind1 == 0 or ind2 == 0:
            return 0

        # Matching
        if text1[ind1 - 1] == text2[ind2 - 1]:
            return 1 + self.solveUsingRecursion1(ind1 - 1, ind2 - 1, text1, text2)

        # Not Matching
        return 0 + max(self.solveUsingRecursion1(ind1 - 1, ind2, text1, text2), self.solveUsingRecursion1(ind1, ind2 - 1, text1, text2))



    # TC: O(l1 * l2)
    # SC: O(l1 * l2) + O(l1 + l2) (recursion stack space)
    def solveUsingMemoization(self, ind1, ind2, text1, text2, dp):
        # Base Case
        if ind1 == 0 or ind2 == 0:
            return 0

        if dp[ind1][ind2] != -1:
            return dp[ind1][ind2]

        # Matching 
        if text1[ind1 - 1] == text2[ind2 - 1]:
            dp[ind1][ind2] = 1 + self.solveUsingMemoization(ind1 - 1, ind2 - 1, text1, text2, dp)
        else:
            # Not Matching
            dp[ind1][ind2] = 0 + max(self.solveUsingMemoization(ind1 - 1, ind2, text1, text2, dp), self.solveUsingMemoization(ind1, ind2 - 1, text1, text2, dp))

        return dp[ind1][ind2]

    def solveUsingTabulation(self, text1, text2, l1, l2):
        dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]

        # Base Case
        for ind2 in range(l2):
            dp[0][ind2] = 0

        for ind1 in range(l1):
            dp[ind1][0] = 0

        for ind1 in range(1, l1 + 1):
            for ind2 in range(1, l2 + 1):
                # Matching 
                if text1[ind1 - 1] == text2[ind2 - 1]:
                    dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1] 
                else:
                    # Not Matching
                    dp[ind1][ind2] = 0 + max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])

        return dp[l1][l2]



    




        


        