from collections import Counter

class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    #     return Counter(s) == Counter(t)

    # def isAnagram(self, s: str, t: str) -> bool:
    #     return sorted(s) == sorted(t)

    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False

    #     countS, countT = {}, {}
    #     for i in range(len(s)):
    #         countS[s[i]] = 1 + countS.get(s[i], 0)
    #         countT[t[i]] = 1 + countT.get(t[i], 0)

    #     return countS == countT

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for num in count:
            if num != 0:
                return False

        return True


        

    


        

        