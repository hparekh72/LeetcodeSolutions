class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # Brute Force:
        # TC: O(n! * n(looping)) 
        # SC: O(n) (Recursive stack space) + O(n) (ds array) + O(n)(visited array)

        res = []
        visited = [False]*len(nums)
        self.getPermutations(nums, visited, [], res)
        return res

    def getPermutations(self, nums, visited, ds, res):

        # Base Case
        if len(ds) == len(nums):
            res.append(ds.copy())
            return


        for i in range(len(nums)):
            if not visited[i]:

                visited[i] = True
                ds.append(nums[i])

                self.getPermutations(nums, visited, ds, res)

                visited[i] = False
                ds.pop()


            




     
        