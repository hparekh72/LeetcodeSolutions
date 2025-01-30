class Solution:
    # def checkInclusion(self, s1: str, s2: str) -> bool: # Brute Force Approach
    #     # TC: O(n^3logn)
    #     # SC: O(n)
    #     s1 = sorted(s1)

    #     for i in range(len(s2)):
    #         for j in range(i, len(s2)):
    #             subStr = s2[i : j + 1]
    #             subStr = sorted(subStr) 

    #             if s1 == subStr:
    #                 return True
        
    #     return False


# Approach 2: Fixed Size Sliding window
# Instead of generating all substrings and checking for permutations (which is inefficient), we use a fixed-size sliding window and hashmaps (frequency counters) to efficiently track character counts.

    def checkInclusion(self, s1: str, s2: str) -> bool:

        # TC: O(n * m) m -> 26 characters (constant) ~ O(n)
        # SC: O(m) (constant) ~ O(1)

        hashMap1 = defaultdict(int)
        for char in s1:
            hashMap1[char] += 1

        l = 0
        r = 0
        hashMap2 = defaultdict(int)

        while r < len(s2):
            hashMap2[s2[r]] += 1

            if (r - l + 1) < len(s1):
                r += 1
            else:           # When (r - l + 1) == len(s1)
                if hashMap1 == hashMap2:
                    return True
                else:
                    hashMap2[s2[l]] -= 1
                    if hashMap2[s2[l]] == 0:
                        del hashMap2[s2[l]]
                    l += 1
                    r += 1
        return False

                    




                


            
            





        