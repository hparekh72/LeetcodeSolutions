class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        # TC: (4 ^ n) * n (worst case)
        # SC: o(n) (dictionary) +  O(len(digits)) + (4 ^ n)(output array) (recursive stack space) 

        res = []
        digitsToChar = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def backtrack(ind, currStr):
            # Base Case
            if len(currStr) == len(digits):
                res.append(currStr)
                return

            for c in digitsToChar[digits[ind]]:
                backtrack(ind + 1, currStr + c)

        if digits:
            backtrack(0, "")
        
        return res

        