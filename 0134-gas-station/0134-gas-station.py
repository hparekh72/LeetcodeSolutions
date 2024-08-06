class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Brute Force: Try all possible subarray
        # TC: O(N^2)
        # SC: O(1)

        # Optimal: Greedy Approach
        # TC: O(N)
        # SC: O(1)

        if sum(gas) < sum(cost):
            return -1
        
        # ie. a unique solution will exist as sum(gas) < sum(cost) will return -1
        total, startIndex = 0, 0

        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                startIndex = i + 1
        
        return startIndex



