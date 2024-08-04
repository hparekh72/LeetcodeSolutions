# Brute Force:
# TC: O(nlogn) + O(2n)
# SC: O(n)

#  Optimal:
# TC: O(nlogn) + O(n)
# SC: O(n)

#  Optimal:
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()

        res = []
        previousInterval = intervals[0]

        for i in range(1, len(intervals)):
            if previousInterval[1] >= intervals[i][0]:
                previousInterval[1] = max(previousInterval[1], intervals[i][1])
            else:
                res.append(previousInterval)
                previousInterval = intervals[i]
        
        res.append(previousInterval)

        return res

        