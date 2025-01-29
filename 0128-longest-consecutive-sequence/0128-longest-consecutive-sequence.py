class Solution:
    # def longestConsecutive(self, nums: List[int]) -> int: # Brute Force
    #     # TC: O(n^2)
    #     # SC: O(n)

    #     res = 0
    #     store = set(nums)

    #     for num in nums:
    #         streak = 0
    #         curr = num
    #         while curr in store:
    #             streak += 1
    #             curr += 1
    #         res = max(res, streak)

    #     return res
    
    def longestConsecutive(self, nums: List[int]) -> int: # Sorting (Better)
        # TC: O(nlogn)
        # SC: O(1)

        if not nums:
            return 0

        res = 0
        nums.sort()

        curr = nums[0]
        streak = 0
        i = 0
        while i < len(nums):
            if curr != nums[i]:
                curr = nums[i]
                streak = 0
            while i < len(nums) and nums[i] == curr:
                i += 1
            streak += 1
            curr += 1
            res = max(res, streak)
        
        return res
        
        