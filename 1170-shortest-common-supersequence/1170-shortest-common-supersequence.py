# Intution: LCS, Print LCS
# Find the LCS & then skip the Characters in LCS(pick only once) & pick the remaining ones from both strings.



class Solution:
    # TC: O(l1 * l2) + O(l1 + l2)
    # SC: O(l1 * l2) 
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        l1 = len(str1)
        l2 = len(str2)

        dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)] # 1 based indexing

        # LCS (Tabulation)

        # Base Case (Not require as the dp array is initilized with 0)
        # for ind1 in range(l1 + 1): 
        #     dp[ind1][0] = 0

        # for ind2 in range(l2 + 1): 
        #     dp[0][ind2] = 0


        for ind1 in range(1, l1 + 1):
            for ind2 in range(1, l2 + 1):
                if str1[ind1 - 1] == str2[ind2 - 1]:    # Matching
                    dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
                else:                                   # Not Matching
                    dp[ind1][ind2] = 0 + max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])

        # Printing the LCS
        i, j = l1, l2 # 1 based indexing
        ans = ""
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:  # Matching (Select one element)
               ans += str1[i - 1]
               i -= 1
               j -= 1
            elif  dp[i - 1][j] > dp[i][j - 1]: # Not Matching
                ans += str1[i - 1]
                i -= 1
            else:                              # Not Matching
                ans += str2[j - 1]
                j -= 1
        
        # Append the remaining characters in the ans
        while i > 0:
            ans += str1[i - 1]
            i -= 1
            
        while j > 0:
            ans += str2[j - 1]
            j -= 1

        return ans[::-1] # Reverse the answer, since we started from the end

        



                





        


    