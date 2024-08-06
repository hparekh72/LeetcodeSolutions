# Optimal
# TC: O(n)
# SC: O(1) + O(n) (required for output) 

class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        # Hashmap to store last-index for each unique character
        hashMap = {}

        for index, char in enumerate(s):
            hashMap[char] = index

        res = []
        size, end = 0, 0
        for index, char in enumerate(s):
            size += 1
            end = max(end, hashMap[char])

            if index == end:
                res.append(size)
                size = 0

        return res






        
        