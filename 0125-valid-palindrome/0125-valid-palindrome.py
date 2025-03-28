class Solution:
    # def isPalindrome(self, s: str) -> bool: # Reverse String
    #     # TC: O(n)
    #     # SC: O(n)

    #     newStr = ""
    #     for c in s:
    #         if c.isalnum():
    #             newStr += c.lower()
    #     return newStr == newStr[::-1]

    def isPalindrome(self, s: str) -> bool: # 2 Pointers

        # TC: O(n)
        # SC: O(1)

        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not self.isAlphaNumeric(s[l]):
                l += 1
            while r > l and not self.isAlphaNumeric(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1

        return True


    def isAlphaNumeric(self, c):
        return(ord('A') <= ord(c) <= ord('Z') or
           ord('a') <= ord(c) <= ord('z') or
           ord('0') <= ord(c) <= ord('9'))


    

        