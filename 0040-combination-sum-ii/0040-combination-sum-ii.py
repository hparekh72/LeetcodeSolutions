# Brute Force:
# TC: O(2^n * k)
# SC: O(n) + k * x
# k -> Average length of k(ds)
# x -> Number of combinations


# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         res = set()
#         self.findCombinations(sorted(candidates), target, 0, [], res)
#         return [list(comb) for comb in res]  # Converts each tuple in the set to a list

#     def findCombinations(self, candidates, target, index, ds, res):

#         # Base Case
#         if index == len(candidates):
#             if target == 0:
#                 res.add(tuple(ds))
#             return

#         # Pick
#         if target - candidates[index] >= 0:
#             ds.append(candidates[index])
#             self.findCombinations(candidates, target - candidates[index], index + 1, ds, res)
#             ds.pop()

#         # Not Pick
#         self.findCombinations(candidates, target, index + 1, ds, res)



# Optimal: Another approach
# TC: O(2^n * k)
# SC: O(n) + k * x
# k -> Average length of k(ds)
# x -> Number of combinations

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.findCombinations(sorted(candidates), target, 0, [], res)
        return res

    def findCombinations(self, candidates, target, index, ds, res):

        # Base Case
        if target == 0:
            res.append(ds.copy())
            return

        # Iterate over the remaining elements to explore further combinations
        for i in range(index, len(candidates)):

            # Skip duplicates in the same recursive level
            if i > index and candidates[i] == candidates[i - 1]:
                continue

            # If the current candidate exceeds the target, break the loop (as further elements won't fit either)
            if candidates[i] > target:
                break

            # Include the current candidate and recurse
            ds.append(candidates[i])
            self.findCombinations(candidates, target - candidates[i], i + 1, ds, res)
            ds.pop()  # Backtrack

        







