class Solution:
    # TC: O(2^n)
    # SC: O(n)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.getSubsets(nums, 0, [], res)
        return res

    def getSubsets(self, nums, index, ds, res):

        # Base Case
        if index == len(nums):
            res.append(ds.copy())
            return

        # Pick 
        ds.append(nums[index])
        self.getSubsets(nums, index + 1, ds, res)
        ds.pop()
        
        # Not Pick
        self.getSubsets(nums, index + 1, ds, res)