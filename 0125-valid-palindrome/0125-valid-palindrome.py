class Solution:
    def isPalindrome(self, s: str) -> bool: # Reverse String
        # TC: O(n)
        # SC: O(n)

        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]

    

        