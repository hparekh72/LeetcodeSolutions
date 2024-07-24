class Solution:
    # TC: (Exponential) O(2^T * k)
    # Here T is how many times the smallest candidate can be used to reach or exceed the target, and k is the average combination size.

    # SC : O(T/min(candidates)) + O(2^T * k)
    # Here, both the recursion stack depth and the storage for all valid combinations.

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.solve(candidates, target, 0, [], res)
        return res

    def solve(self, candidates, target, index, ds, res):

        # Base Case 
        if index == len(candidates):
            if target == 0:
                res.append(ds[:]) # or res.append(list(ds)) 
            return 

        # Pick
        if target - candidates[index] >= 0:
            ds.append(candidates[index])
            self.solve(candidates, target - candidates[index], index, ds, res) 
            ds.pop()

        # Not Pick  
        self.solve(candidates, target, index + 1, ds, res) 

        
        