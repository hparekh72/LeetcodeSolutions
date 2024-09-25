class Solution:

    # Similar to the Tabulation of LCS
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # Tabulation (Bottom-Up)

        l1 = len(nums1)
        l2 = len(nums2)

        # return self.solveUsingTabulation(nums1, nums2, l1, l2)
        return self.solveUsingSpaceOptimization(nums1, nums2, l1, l2)

    # TC: O(l1 * l2) 
    # SC: O(l1 * l2) 
    def solveUsingTabulation(self, nums1, nums2, l1, l2):
        dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]

        # Base Case
        # for ind2 in range(l2):
        #     dp[0][ind2] = 0

        # for ind1 in range(l1):
        #     dp[ind1][0] = 0

        maximumLength = 0
        for ind1 in range(1, l1 + 1):
            for ind2 in range(1, l2 + 1):
                if nums1[ind1 - 1] == nums2[ind2 - 1]: # Matching
                    dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
                    maximumLength = max(maximumLength, dp[ind1][ind2])
                else:   # Not Matching
                    dp[ind1][ind2] = 0
        
        return maximumLength


    # TC: O(l1 * l2) 
    # SC: O(l2) 
    def solveUsingSpaceOptimization(self, nums1, nums2, l1, l2):
        prev = [0 for _ in range(l2 + 1)]

        maximumLength = 0
        for ind1 in range(1, l1 + 1):
            curr = [0 for _ in range(l2 + 1)]
            for ind2 in range(1, l2 + 1):
                if nums1[ind1 - 1] == nums2[ind2 - 1]: # Matching
                    curr[ind2] = 1 + prev[ind2 - 1]
                    maximumLength = max(maximumLength, curr[ind2])
                else:   # Not Matching
                    curr[ind2] = 0
            prev = curr

        return maximumLength
        

        

                




        