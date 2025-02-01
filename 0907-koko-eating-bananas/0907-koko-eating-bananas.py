class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Approach: Brute Force
        # Traverse through 1 to max(p) for each element
        # TC: max(piles) * len(piles)

        # Approach: Binary Search (First Occurence)
        # TC: O(nlog(max(piles)))
        # SC: O(1)

        l = 1
        r = max(piles)

        while l <= r:
            mid = l + (r - l) // 2
            
            if self.hoursRequired(piles, mid) <= h:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
    

    def hoursRequired(self, piles, speed):
        totalTime = 0
        for p in piles:
            totalTime += math.ceil(p / speed)
        return totalTime 

        