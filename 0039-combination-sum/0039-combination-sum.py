# TC: O(2 ^ t/m) * k, where t is the target, m is the minimum value in nums and k is the average combination size.

# SC: O(t/m) (Recursion Stack Space)

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.solve(0, candidates, target, [], res)
        return res

    def solve(self, ind, candidates, target, ds, res):
        # Base Case
        if ind >= len(candidates):
            if target == 0:
                res.append(ds.copy())  # or res.append(list(ds))  # or res.append(ds[:])
            return 

        # Pick
        if target - candidates[ind] >= 0:
            ds.append(candidates[ind])
            self.solve(ind, candidates, target - candidates[ind], ds, res)
            ds.pop()
        # Not Pick

        self.solve(ind + 1, candidates, target, ds, res)
        