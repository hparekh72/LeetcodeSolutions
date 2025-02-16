# Brute Force:
# TC: O(N^2)
# SC: O(1)

# Optimal: Sort with the start time for each meeting
# TC: O(NlogN)
# SC: O(1)


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        if len(intervals) == 0:
            return True

        intervals.sort()

        previousMeetEndTime = intervals[0][1]

        for startTime, endTime in intervals[1:]:
            if previousMeetEndTime > startTime:
                return False
            previousMeetEndTime = endTime

        return True

