class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # TC: O(n)
        # SC: O(m) m -> length of unique characters in the str

        if len(t) > len(s):
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        l = 0
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float('inf')

        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)

            if char in countT and window[char] == countT[char]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                
                l += 1

        if resLen != float('inf'):
            return s[res[0] : res[1] + 1]
        else:
            return ""
                



            






        
        