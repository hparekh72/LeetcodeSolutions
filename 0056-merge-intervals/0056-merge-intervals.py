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
        output = [intervals[0]]

        for start, end in intervals:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output