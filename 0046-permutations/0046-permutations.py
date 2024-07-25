
"""
Brute Force:
TC: O(n! * n(looping)) 
SC: O(n) (Recursive stack space) + O(n) (ds array) + O(n)(visited array) + O(n!)(res array)
"""

# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:

#         res = []
#         visited = [False]*len(nums)
#         self.getPermutations(nums, visited, [], res)
#         return res

#     def getPermutations(self, nums, visited, ds, res):

#         # Base Case
#         if len(ds) == len(nums):
#             res.append(ds.copy())
#             return


#         for i in range(len(nums)):
#             if not visited[i]:

#                 visited[i] = True
#                 ds.append(nums[i])

#                 self.getPermutations(nums, visited, ds, res)

#                 visited[i] = False
#                 ds.pop()

"""
Optimal: Swapping
TC: O(n! * n(looping)) 
SC: O(n) (Recursive stack space) + O(n!)(res array)
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.getPermutations(nums, 0, res)
        return res

    def swap(self, i, j, nums):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def getPermutations(self, nums, index, res):

        # Base Case:
        if index == len(nums):
            res.append(nums.copy())
            return 

        for i in range(index, len(nums)):
            self.swap(index, i, nums)
            self.getPermutations(nums, index + 1, res)
            self.swap(index, i, nums) # Backtrack






     
        