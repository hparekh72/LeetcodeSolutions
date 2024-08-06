# Optimal
# TC: O(n)
# SC: O(1)

# Approach: Selectively consider only those triplets that do not exceed target values and tracks indices where the target values are matched exactly.

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for t in triplets:
            if (t[0] > target[0]) or (t[1] > target[1]) or (t[2] > target[2]):
                continue
            
            for index, value in enumerate(t):
                if value == target[index]:
                    good.add(index)

        # Check if all three indices (0, 1, 2) are in the 'good' set, which means all target values are achievable 
        return len(good) == 3


                
        