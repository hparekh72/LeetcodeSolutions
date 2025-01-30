class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int: # Brute Force
    #     # TC: O(n * m) m-> length of unique characters
    #     # SC: O(m)

    #     res = 0
    #     for i in range(len(s)):
    #         charSet = set()
    #         for j in range(i, len(s)):
    #             if s[j] in charSet:
    #                 break
    #             charSet.add(s[j])
    #         res = max(res, len(charSet))
        
    #     return res
    
    def lengthOfLongestSubstring(self, s: str) -> int: # Sliding Window
        # TC: O(n) 
        # SC: O(m) m-> length of unique characters

        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            charSet.add(s[r])
            res = max(res, len(charSet))

        return res
        



        