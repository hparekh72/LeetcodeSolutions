class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)

        dp = [[-1 for _ in range(l2 + 1)] for _ in range(l1 + 1)]

        lcs =  self.longestCommonSubsequence(l1, l2, word1, word2, dp)

        return (l1 - lcs) + (l2 - lcs)


    # Memoization Approach
    # TC: O(l1 * l2)
    # SC: O(l1 * l2) + O(l1 + l2) (recursion stack space)

    def longestCommonSubsequence(self, ind1, ind2, s1, s2, dp):
        # Base Case
        if ind1 == 0 or ind2 == 0:
            return 0

        if dp[ind1][ind2] != -1:
            return dp[ind1][ind2]

        if s1[ind1 - 1] == s2[ind2 - 1]:
            dp[ind1][ind2] = 1 + self.longestCommonSubsequence(ind1 - 1, ind2 - 1, s1, s2, dp) # Matching
        else:
            dp[ind1][ind2] = 0 + max(self.longestCommonSubsequence(ind1 - 1, ind2, s1, s2, dp), self.longestCommonSubsequence(ind1, ind2 - 1, s1, s2, dp)) 
        
        return dp[ind1][ind2]
        