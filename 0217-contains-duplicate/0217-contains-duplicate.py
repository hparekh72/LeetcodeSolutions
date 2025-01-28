class Solution:

    # TC: O(n)
    # SC: O(n)

    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set(nums)
        if len(hashSet) == len(nums):
            return False
        else:
            return True