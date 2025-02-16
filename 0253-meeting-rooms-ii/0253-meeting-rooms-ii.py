# Optimal: 
# TC: O(NlogN)
# SC: O(N)

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        startTime = sorted([time[0] for time in intervals])
        endTime = sorted(time[1] for time in intervals)

        res, count = 0, 0
        start, end = 0, 0

        while start < len(intervals):
            if startTime[start] < endTime[end]:
                start += 1
                count += 1
                res = max(res, count)
            else:
                end += 1
                count -= 1

        return res

