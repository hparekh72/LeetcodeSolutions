# Greedy Approach
# TC: O(nlogn) + O(n)
# SC: O(1)

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        boxTypes.sort(key=lambda x: x[1], reverse=True)

        res = 0
        i = 0
        while i < len(boxTypes) and truckSize > 0:
            if boxTypes[i][0] <= truckSize:
                res += boxTypes[i][0] * boxTypes[i][1]
                truckSize -= boxTypes[i][0]
                i += 1
                print(res, truckSize)
            else:   
                break

        if i < len(boxTypes) and truckSize > 0:
            res += truckSize * boxTypes[i][1]

        return res
        


