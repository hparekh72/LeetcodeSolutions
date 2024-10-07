class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        l1 = len(s)
        l2 = len(p)

        # return self.solveUsingRecursion(l1 - 1, l2 - 1, s, p) # 0-based indexing
        # return self.solveUsingRecursion1(l1, l2, s, p) # 1-based indexing

        dp = [[-1 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        return self.solveUsingMemoization(l1, l2, s, p, dp) # 1-based indexing

        return self.solveUsingTabulation(s, p, l1, l2)


    # TC: O(Exponentil)
    # SC: O(l1 + l2) (recursion stack space)
    def solveUsingRecursion(self, ind1, ind2, s, p): # 0-based indexing
        # Base Case
        if ind1 < 0 and ind2 < 0:
            return True
        elif ind1 >= 0 and ind2 < 0:
            return False
        elif ind1 < 0 and ind2 >= 0:
            for i in range(ind2+1):
                if p[i] != "*":
                    return False
            return True

        # Matching Character or ?
        if s[ind1] == p[ind2] or p[ind2] == '?':
            return self.solveUsingRecursion(ind1 - 1, ind2 - 1, s, p)
        elif p[ind2] == "*": # For *
            # When * is consider as empty "" or when * is considered as one or more character 
            return  self.solveUsingRecursion(ind1, ind2 - 1, s, p) or self.solveUsingRecursion(ind1 - 1, ind2, s, p)
        else: # When characters does not match
            return False


    # TC: O(Exponentil)
    # SC: O(l1 + l2) (recursion stack space)
    def solveUsingRecursion1(self, ind1, ind2, s, p): # 1-based indexing
        # Base Case
        if ind1 == 0 and ind2 == 0:
            return True
        elif ind1 > 0 and ind2 == 0:
            return False
        elif ind1 == 0 and ind2 > 0:
            for i in range(1, ind2 + 1):
                if p[i - 1] != "*":
                    return False
            return True

        # Matching Character or ?
        if s[ind1 - 1] == p[ind2 - 1] or p[ind2 - 1] == '?':
            return self.solveUsingRecursion1(ind1 - 1, ind2 - 1, s, p)
        elif p[ind2 - 1] == "*": # For *
            # When * is consider as empty "" or when * is considered as one or more character 
            return  self.solveUsingRecursion1(ind1, ind2 - 1, s, p) or self.solveUsingRecursion1(ind1 - 1, ind2, s, p)
        else: # When characters does not match
            return False


    # TC: O(l1 * l2)
    # SC: O(l1 * l2) + O(l1 + l2) (recursion stack space)
    def solveUsingMemoization(self, ind1, ind2, s, p, dp):
        # Base Case
        if ind1 == 0 and ind2 == 0:
            return True
        elif ind1 > 0 and ind2 == 0:
            return False
        elif ind1 == 0 and ind2 > 0:
            for i in range(1, ind2 + 1):
                if p[i - 1] != "*":
                    return False
            return True

        if dp[ind1][ind2] != -1:
            return dp[ind1][ind2]
        
        # Matching Character or ?
        if s[ind1 - 1] == p[ind2 - 1] or p[ind2 - 1] == '?':
            dp[ind1][ind2] = self.solveUsingMemoization(ind1 - 1, ind2 - 1, s, p, dp)
        elif p[ind2 - 1] == "*": # For *
            # When * is consider as empty "" or when * is considered as one or more character 
            dp[ind1][ind2] = self.solveUsingMemoization(ind1, ind2 - 1, s, p, dp) or self.solveUsingMemoization(ind1 - 1, ind2, s, p, dp)
        else: # When characters does not match
            dp[ind1][ind2] = False

        return dp[ind1][ind2]



    # TC: O(l1 * l2)
    # SC: O(l1 * l2) 
    def solveUsingTabulation(self, s, p, l1, l2):
        # Base Case
        dp = [[False for _ in range(l2 + 1)] for _ in range(l1 + 1)]

        dp[0][0] = True

        # for ind1 in range(1, l1 + 1):
        #     dp[ind1][0] = False

        for ind2 in range(ind2 + 1):
            flag = True
            for i in range(1, ind2 + 1):
                if p[i - 1] != "*":
                    flag = False
                    break
            dp[0][ind2] = flag

        for ind1 in range(1, l1 + 1):
            for ind2 in range(1, l2 + 1):
                # Matching Character or ?
                if s[ind1 - 1] == p[ind2 - 1] or p[ind2 - 1] == '?':
                    dp[ind1][ind2] = dp[ind1 - 1][ind2 - 1] 
                elif p[ind2 - 1] == "*": # For *
                    # When * is consider as empty "" or when * is considered as one or more character 
                    dp[ind1][ind2] = dp[ind1][ind2 - 1] or dp[ind1 - 1][ind2] 
                else: # When characters does not match
                    dp[ind1][ind2] = False

                return dp[ind1][ind2]


        



        
        


        