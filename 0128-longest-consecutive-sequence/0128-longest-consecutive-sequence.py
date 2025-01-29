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

    def longestConsecutive(self, nums: List[int]) -> int: # HashSet

        # TC: O(n)
        # SC: O(n)
        n = len(nums)
        if n == 0:
            return 0

        hashSet = set(nums)

        longest = 1
        for element in hashSet:
            prev = element - 1
            count = 1
            if prev not in hashSet:
                while element + 1 in hashSet:
                    element += 1
                    count += 1
                longest = max(count, longest)

        return longest




        
        