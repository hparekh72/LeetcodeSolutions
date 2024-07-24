class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        ds = []
        total = 0
        self.solve(candidates, target, 0, total, ds, res)
        return res

    def solve(self, candidates, target, index, total, ds, res):

        if total > target:
            return 

        # Base Case 
        if index == len(candidates):
            if total == target:
                res.append(list(ds))
            return 

        # Pick
        ds.append(candidates[index])
        self.solve(candidates, target, index, total + candidates[index], ds, res) 

        # Not Pick
        ds.pop()
        self.solve(candidates, target, index + 1, total, ds, res) 

        
        