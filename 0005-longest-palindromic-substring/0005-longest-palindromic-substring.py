# Brute Force 
# TC: O(n^3)
# SC: O(1)
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
        
#         res = ""
#         longest = 0
#         for i in range(len(s)):
#             for j in range(i, len(s)):
#                 if self.isPalindrome(i, j, s):
#                     if (j - i + 1) > longest:
#                         longest = j - i + 1
#                         res = s[i : j + 1]


#         return res

#     def isPalindrome(self, l, r, s):
#         while l <= r:
#             if s[l] != s[r]:
#                 return False
#             l += 1
#             r -= 1

#         return True

# Intuition: Two Pointers (we expand around each character as a center)
# Instead of using a DP table, we expand around each character as a center:

# A palindrome is symmetric, meaning it expands equally outward.
# We consider both odd-length and even-length palindromes:
# Odd-length: Center at s[i], expand l=i, r=i
# Even-length: Center between s[i] and s[i+1], expand l=i, r=i+1
# At each expansion, we update the longest palindrome found.

# TC: O(n^2)
# SC: O(1)
class Solution: 
    def longestPalindrome(self, s: str) -> str: # Two Pointers
        resLen = 0
        res = ""
        for i in range(len(s)):
            # Odd Length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    res = s[l : r + 1]
                l -= 1
                r += 1

            # Even Length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    res = s[l : r + 1]
                l -= 1
                r += 1

        return res
                    


