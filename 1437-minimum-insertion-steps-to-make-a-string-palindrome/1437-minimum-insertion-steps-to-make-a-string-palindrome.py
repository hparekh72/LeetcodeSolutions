# Intution: Reverse the string s and store in s2. Get the longest palindromic subsequence. Now (stringLength-lcs) will be the answer.



class Solution:
    def minInsertions(self, s: str) -> int:
        s1 = s
        s2 = s[::-1] # Reverse of s

        l1 = len(s1)
        l2 = len(s2)

        dp = [[-1 for _ in range(l2 + 1)] for _ in range(l1 + 1)]

        # Get the longest palindromic subsequence
        longestPalindromicSubsequence = self.longestCommonSubsequence(l1, l2, s1, s2, dp)

        return len(s1) - longestPalindromicSubsequence


    # Memoization Approach
    # TC: O(l1 * l2)
    # SC: O(l1 * l2) + O(l1 + l2) (recursion stack space)

    def longestCommonSubsequence(self, ind1, ind2, s1, s2, dp):
        # Base Case
        if ind1 == 0 or ind2 == 0:
            return 0

        if dp[ind1][ind2] != -1:
            return dp[ind1][ind2]

        if s1[ind1 - 1] == s2[ind2 - 1]: # Matching
            dp[ind1][ind2] = 1 + self.longestCommonSubsequence(ind1 - 1, ind2 - 1, s1, s2, dp)
        else: # Not Matching
            dp[ind1][ind2] = max(self.longestCommonSubsequence(ind1 - 1, ind2, s1, s2, dp), self.longestCommonSubsequence(ind1, ind2 - 1, s1, s2, dp))

        return dp[ind1][ind2]


        
