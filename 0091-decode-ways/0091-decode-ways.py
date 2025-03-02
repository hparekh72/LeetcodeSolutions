class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        # return self.solveUsingRecursion(0, s)

        dp = [-1 for _ in range(len(s))]

        # return self.solveUsingMemoization(0, s, dp)
        # return self.solveUsingTabulation(s)
        return self.solveUsingSpaceOptimization(s)



    # Brute Force
    # TC: O(2^n)
    # SC: O(n) (recursion stack space)
    def solveUsingRecursion(self, i, s):
        # Base Case
        if i == len(s):
            return 1
        
        if s[i] == "0": # Leading zero is invalid
            return 0

        res = self.solveUsingRecursion(i + 1, s) # Decode Single Digits
        if i < len(s) - 1 and (s[i] == "1" or (s[i] == "2" and s[i + 1] < '7')):
            res += self.solveUsingRecursion(i + 2, s) # Decode Two Digits

        return res

    # Optimal
    # TC: O(n)
    # SC: O(n) (Memoization + recursion stack space)
    def solveUsingMemoization(self, i, s, dp):
        # Base Case
        if i == len(s):
            return 1
        
        if s[i] == "0": # Leading zero is invalid
            return 0

        if dp[i] != -1:
            return dp[i]

        res = self.solveUsingMemoization(i + 1, s, dp) # Decode Single Digits
        if i < len(s) - 1 and (s[i] == "1" or (s[i] == "2" and s[i + 1] < '7')):
            res += self.solveUsingMemoization(i + 2, s, dp) # Decode Two Digits

        dp[i] = res
        return dp[i]  


    # Here, dp[i] represents the number of ways to decode the substring s[i:]
    # TC: O(n)
    # SC: O(n) (dp array)
    def solveUsingTabulation(self, s):
        n = len(s)
        dp = [0 for _ in range(len(s) + 1)]

        dp[n] = 1 # Base case: one way to decode an empty string

        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0 # 0 cannot be decoded
            else:
                dp[i] = dp[i + 1] # Decode Single Digit

                if i < len(s) - 1 and (s[i] == "1" or (s[i] == "2" and s[i + 1] < '7')):
                    dp[i] += dp[i + 2]

        return dp[0]


    # TC: O(n)
    # SC: O(1)
    def solveUsingSpaceOptimization(self, s):
        n = len(s)
        next1 = 1 # dp[i + 1] # Base case: when i = len(s), equivalent to dp[n] (one way to decode an empty string)
        next2 = 0 # dp[i + 2] # Equivalent to dp[n + 1], which is out of bounds (If i is at the last character (s[n-1]), there is no s[n+1].

        for i in range(n - 1, -1, -1):
            curr = 0
            if s[i] == "0":
                curr = 0 
            else:
                curr = next1

                if i < n - 1 and (s[i] == "1" or (s[i] == "2" and s[i + 1] < '7')):
                    curr += next2

            next2 = next1
            next1 = curr

        return next1
         


            
 
         



        

        