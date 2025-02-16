# TC: O(n)
# SC: O(1)

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        # Iterate through all intervals
        for i in range(len(intervals)):
            # Case 2: New interval comes before the current interval
            # No overlap; directly add newInterval and remaining intervals
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)  # Add the new interval
                return res + intervals[i:]  # Add the rest of the intervals as they are
            
            # Case 1: Current interval comes before the new interval
            # No overlap; directly add the current interval to the result
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            # Case 3: Overlapping intervals
            # Merge the current interval with the new interval
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),  # Start of the merged interval
                    max(newInterval[1], intervals[i][1])   # End of the merged interval
                ]

        # If newInterval wasn't added during the loop, add it at the end
        res.append(newInterval)

        return res
