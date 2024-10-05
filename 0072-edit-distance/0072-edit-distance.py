class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        # return self.solveUsingRecursion(l1 - 1, l2 - 1, word1, word2) # 0-based indexing
        # return self.solveUsingRecursion1(l1, l2, word1, word2) # 1-based indexing

        dp = [[-1 for _ in range(l2 + 1)] for _ in range(l1 + 1)]

        return self.solveUsingMemoization(l1, l2, word1, word2, dp)


    # TC: O(3 ^ l1 * 3 ^ l2) (Exponential)
    # SC: O(l1 + l2) (recursion stack space)
    def solveUsingRecursion(self, ind1, ind2, word1, word2): # 0-based indexing
        # Base Case
        # Example: word1 = "", word2 = "hello"
        if ind1 < 0:
            return ind2 + 1

        # Example: word1 = "hello", word2 = ""
        if ind2 < 0:
            return ind1 + 1

        # Matching
        if word1[ind1] == word2[ind2]:
            return 0 + self.solveUsingRecursion(ind1 - 1, ind2 - 1, word1, word2)

        # Not Matching (Replace, delete, insert)
        return 1 + min(self.solveUsingRecursion(ind1 - 1, ind2 - 1, word1, word2), self.solveUsingRecursion(ind1 - 1, ind2, word1, word2), self.solveUsingRecursion(ind1, ind2 - 1, word1, word2))

    
    # TC: O(3 ^ l1 * 3 ^ l2) (Exponential)
    # SC: O(l1 + l2) (recursion stack space)
    def solveUsingRecursion1(self, ind1, ind2, word1, word2): # 1-based indexing
        # Base Case
        if ind1 == 0:
            return ind2

        if ind2 == 0:
            return ind1

        # Matching
        if word1[ind1 - 1] == word2[ind2 - 1]:
            return 0 + self.solveUsingRecursion1(ind1 - 1, ind2 - 1, word1, word2)

        # Not Matching (Replace, delete, insert)
        return 1 + min(self.solveUsingRecursion1(ind1 - 1, ind2 - 1, word1, word2), self.solveUsingRecursion1(ind1 - 1, ind2, word1, word2), self.solveUsingRecursion1(ind1, ind2 - 1, word1, word2))


    # TC: O(l1 * l2) 
    # SC: O(l1 + l2) + O(l1 + l2) (recursion stack space)
    def solveUsingMemoization(self, ind1, ind2, word1, word2, dp):  # 1-based indexing
        # Base Case
        if ind1 == 0:
            return ind2

        if ind2 == 0:
            return ind1

        if dp[ind1][ind2] != -1:
            return dp[ind1][ind2]

        # Matching
        if word1[ind1 - 1] == word2[ind2 - 1]:
            dp[ind1][ind2] = 0 + self.solveUsingMemoization(ind1 - 1, ind2 - 1, word1, word2, dp)

        else:
            # Not Matching (Replace, delete, insert)
            dp[ind1][ind2] = 1 + min(self.solveUsingMemoization(ind1 - 1, ind2 - 1, word1, word2, dp), self.solveUsingMemoization(ind1 - 1, ind2, word1, word2, dp), self.solveUsingMemoization(ind1, ind2 - 1, word1, word2, dp))

        return dp[ind1][ind2]

    def solveUsingTabulation(self, word1, word2, l1, l2):
        
        dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]

        # Base Case
        for ind2 in range(l2 + 1):
            dp[0][ind2] = ind2

        for ind1 in range(l1 + 1):
            dp[ind1][0] = ind1

        for ind1 in range(1, l1 + 1):
            for ind2 in range(1, l2 + 1):
                # Matching
                if word1[ind1 - 1] == word2[ind2 - 1]:
                    dp[ind1][ind2] = 0 + dp[ind1 - 1][ind2 - 1] 
                else:
                    # Not Matching (Replace, delete, insert)
                    dp[ind1][ind2] = 1 + min(dp[ind1 - 1][ind2 - 1], dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])
        
        return dp[l1][l2]
            



    

    

    

