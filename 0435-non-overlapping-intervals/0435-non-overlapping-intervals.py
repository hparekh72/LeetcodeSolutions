class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Greedy Approach
        # Similar approach of N meetings in one room (on GFG)
        # Intution: Say if you have two meetings, one which gets over early and another which gets over late. Which one should we choose?  If our meeting lasts longer the room stays occupied and we lose our time. On the other hand, if we choose a meeting that finishes early we can accommodate more meetings. Hence we should choose meetings that end early and utilize the remaining time for more meetings.

        # TC: O(nlogn) + O(n)
        # SC: O(1)

        intervals.sort(key=lambda x : x[1])

        overlappingIntervals = 0
        intervalEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervalEnd:
                intervalEnd = intervals[i][1]
            else:
                overlappingIntervals += 1
        
        return overlappingIntervals





        