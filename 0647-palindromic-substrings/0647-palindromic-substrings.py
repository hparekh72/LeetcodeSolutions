# Brute Force: Generate all substrings and check for palindrome
# TC: O(n^3)
# SC: O(1)

# Optimal: Similar approach of Longest Palindromic Substring
# Intuition: Two Pointers (we expand around each character as a center)

# A palindrome is symmetric, meaning it expands equally outward.
# We consider both odd-length and even-length palindromes:
# Odd-length: Center at s[i], expand l=i, r=i
# Even-length: Center between s[i] and s[i+1], expand l=i, r=i+1
# At each expansion, we update the longest palindrome found.

# TC: O(n^2)
# SC: O(1)
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            # Odd Length
            res += self.countPalindromes(i, i, s)
    
            # Even Length
            l, r = i, i + 1
            res += self.countPalindromes(i, i + 1, s)
        return res

    def countPalindromes(self, l, r, s):
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1 
        return count  




            

        
        