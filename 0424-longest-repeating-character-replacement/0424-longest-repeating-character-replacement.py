class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Brute Force: Generate all substrings
        # TC: O(N^2)
        # SC: O(1)

        # longest = 0
        # for i in range(len(s)):
        #     temp = s[i]
        #     noOfReplacement = 0
        #     for j in range(i, len(s)):
        #         if s[j] != temp:
        #             noOfReplacement += 1
                
        #         if noOfReplacement <= k:
        #             longest =max(longest, j - i + 1)
        #         else:
        #             break
        # return longest

        # Approach 2: Two pointer
        # window length - MaxFrequency <= k
        # TC: O(N + N) * len(hashMap)

        # longest = 0
        # l, r = 0, 0
        # maxFrequency = 0
        # hashMap = defaultdict(int)
        # while r < len(s):
        #     hashMap[s[r]] += 1
        #     maxFrequency = max(maxFrequency, hashMap[s[r]])

        #     while (r - l + 1) - maxFrequency > k:
        #         hashMap[s[l]] -= 1
        #         maxFrequency = max(hashMap.values())
        #         l += 1

        #     if (r - l + 1) - maxFrequency <= k:
        #         longest = max(longest, r - l + 1)
            
        #     r += 1

        # return longest

        # Approach 3: Two pointer
        # window length - MaxFrequency <= k
        # TC: O(N) 

        # longest = 0
        # l, r = 0, 0
        # maxFrequency = 0
        # hashMap = defaultdict(int)
        # while r < len(s):
        #     hashMap[s[r]] += 1
        #     maxFrequency = max(maxFrequency, hashMap[s[r]])

        #     while (r - l + 1) - maxFrequency > k:
        #         hashMap[s[l]] -= 1
        #         l += 1

        #     if (r - l + 1) - maxFrequency <= k:
        #         longest = max(longest, r - l + 1)
            
        #     r += 1

        # return longest

        # Neetcode Solutions

        # Approach 2: Two Pointer 
        # TC: O(m * n) m -> Total no. of unique characters in the string
        # SC: O(m)

        # count = {}
        # res = 0
        # l = 0

        # for r in range(len(s)):
        #     count[s[r]] = 1 + count.get(s[r], 0)

        #     while (r - l + 1) - max(count.values()) > k:
        #         count[s[l]] -= 1
        #         l += 1

        #     res = max(res, (r - l + 1))

        # return res

        # Approach 3: Two Pointer 
        # TC: O(n) 
        # SC: O(m)

        count = {}
        res = 0
        l = 0
        maxFrequency = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxFrequency = max(maxFrequency, count[s[r]])

            while (r - l + 1) - maxFrequency > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, (r - l + 1))

        return res



