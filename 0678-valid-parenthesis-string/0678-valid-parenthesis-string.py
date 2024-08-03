# Brute Force: Using Recursion
# TC: O(3^n)
# SC: O(n)

# Better: Using Dynamic Programming
# TC: O(n^2)
# SC: O(n^2)

# Optimal: Using Greedy
# TC: O(n)
# SC: O(1)

class Solution:
    def checkValidString(self, s: str) -> bool:
        # Using Recursion
        # return self.isValid(s, 0, 0)
        minimumRange = 0
        maximumRange = 0


        # Using Greedy Approach
        for i in range(len(s)):
            if s[i] == "(":
                minimumRange += 1
                maximumRange += 1
            elif s[i] == ")":
                minimumRange -= 1
                maximumRange -= 1
            else:
                minimumRange -= 1
                maximumRange += 1
            
            if minimumRange < 0:
                minimumRange = 0
            
            if maximumRange < 0:
                return False
        
        return minimumRange == 0




    # Using Recursion
    def isValid(self, s, ind, count): # TC: O(3^n)
        if count < 0:
            return False

        if ind == len(s):
            return count == 0

        if s[ind] == "(":
            return self.isValid(s, ind + 1, count + 1)
        elif s[ind] == ")":
            return self.isValid(s, ind + 1, count - 1)
        else: # Asterisk
            # 3 choices if asterisk: ( "(" or ")" or "" )
            return self.isValid(s, ind + 1, count + 1) or self.isValid(s, ind + 1, count - 1) or self.isValid(s, ind + 1, count)

        

