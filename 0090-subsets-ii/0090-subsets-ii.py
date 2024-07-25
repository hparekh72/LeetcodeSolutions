class Solution:
    # TC: O(2^n)
    # SC: O(n)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.getSubsetsWithDup(sorted(nums), 0, [], res)
        return res

    def getSubsetsWithDup(self, nums, index, ds, res):

        # Base Case
        res.append(ds.copy())

        for i in range(index, len(nums)):

            # Skip duplicates in the same recursive level
            if i > index and nums[i] == nums[i - 1]:
                continue

            ds.append(nums[i])
            self.getSubsetsWithDup(nums, i + 1, ds, res)
            ds.pop()