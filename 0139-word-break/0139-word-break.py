class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # return self.solveUsingRecursion(0, s, wordDict)

        # dp = [-1 for _ in range(len(s) + 1)]
        # return self.solveUsingMemoization(0, s, wordDict, dp)

        return self.solveUsingTabulation(s, wordDict)
    
    # TC: O(2^n * m)
    # SC: O(n) (Recursion Stack Space)
    def solveUsingRecursion(self, ind, s, wordDict):
        
        if ind == len(s): # Base case: reached the end
            return True

        for w in wordDict: # Try each word from dictionary
            if (ind + len(w)) <= len(s) and s[ind : ind + len(w)] == w:  # Check if within bounds and substring matches
                if self.solveUsingRecursion(ind + len(w), s, wordDict): # Recursively check remaining part
                    return True
        return False  # No valid segmentation found



    # TC: O(n * m)
    # SC: O(n) (Dp and Recursion Stack Space)
    def solveUsingMemoization(self, ind, s, wordDict, dp):
        if ind == len(s):
            return True

        if dp[ind] != -1:
            return dp[ind]

        for w in wordDict:
            if (ind + len(w)) <= len(s) and s[ind : ind + len(w)] == w:  # Check if within bounds and substring matches
                if self.solveUsingMemoization(ind + len(w), s, wordDict, dp): # Recursively check remaining part
                    dp[ind] = True
                    return dp[ind]

        dp[ind] = False
        return dp[ind]


    # TC: O(n * m)
    # SC: O(n) (Dp)
    def solveUsingTabulation(self, s, wordDict):
        n = len(s)

        dp = [False for _ in range(len(s) + 1)]
        dp[n] = True

        for ind in range(n - 1, -1, -1):
            for w in wordDict:
                if (ind + len(w)) <= len(s) and s[ind : ind + len(w)] == w:  # Check if within bounds and substring matches
                    if dp[ind + len(w)]:
                        dp[ind] = True
                        break

        return dp[0]
    





    


            
        
        