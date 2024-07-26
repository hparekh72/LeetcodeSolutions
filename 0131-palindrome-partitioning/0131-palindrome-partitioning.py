
# TC: O((2^n) * k * (n/2))
# This (2^n) complexity arises because for each character, there is a decision to either end the current palindrome partition at that character or extend it, effectively creating a decision tree. 
# (n/2) is the time require to check if it is palindrome or not.
# k is the time to append the current list into the result.

# SC: O(k * x) + O(l) (recursive stack space)

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.solve(s, 0, [], res)
        return res

    def solve(self, s, index, path, res):
        if index == len(s):
            res.append(path.copy())
            return

        for i in range(index, len(s)):
            if self.isPalindrome(s, index, i):
                path.append(s[index : i + 1])
                self.solve(s, i+1, path, res)
                path.pop() # Backtrack

    
    def isPalindrome(self, s, start, end):
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1

        return True

        