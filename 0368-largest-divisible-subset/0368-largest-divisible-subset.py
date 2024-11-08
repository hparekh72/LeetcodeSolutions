# Intuition: Use similar approach of Longest Increasing Subsequence (LIS). Use the Print LIS approach.
# Sort the array to make it easier to find divisible pairs in an increasing order.

class Solution:

    # TC: O(n * n) + O(n) (printing the list)
    # SC: O(n) + O(n) ~ O(n)
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        # Step 1: Sort the nums array
        nums.sort()

        # Step 2: Initialize dp and hashArr arrays
        n = len(nums)
        dp = [1 for _ in range(n)] 
        hashArr = []


        # Step 3: Variables to track the maximum subset length and its ending index
        maxSize = 0
        lastIndex = 0


        # Step 4: Populate dp and hashArr arrays
        for ind in range(n):
            hashArr.append(ind)
            for prev_ind in range(ind):
                if nums[ind] % nums[prev_ind] == 0 and (1 + dp[prev_ind]) > dp[ind]:
                    dp[ind] = 1 + dp[prev_ind]
                    hashArr[ind] = prev_ind
        
            # Update max_size and last_index if we found a new maximum
            if dp[ind] > maxSize:
                maxSize = dp[ind]
                lastIndex = ind
        
        # Step 5: Reconstruct the subset. # TC: O(n)
        res = []
        res.append(nums[lastIndex])

        while hashArr[lastIndex] != lastIndex:
            lastIndex = hashArr[lastIndex]
            res.append(nums[lastIndex])

        res.reverse() # Optional

        return res
        


        