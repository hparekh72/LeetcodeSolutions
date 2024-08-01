# Approach 1: Recursion(Trying all possible ways)
# TC: O(N^N) (Exponential)
# SC: O(N) (Recursive Stack Space)

# Approach 2: Dynamic Programming
# TC: O(N^2) 
# SC: O(N^2) 

# Approach 3: Greedy Algorithm
# TC: O(n)
# SC: O(1)

class Solution:
    def jump(self, nums: List[int]) -> int:
        # Approach 1: Recursion(Trying all possible ways)
        # return self.minimumJumps(0, 0, float('inf'), nums)

        # Approach 2: Dynamic Programming
        # dp = [[-1 for _ in range(len(nums))] for _ in range(len(nums))]

        # return self.minJumps(0, 0, float('inf'), dp, nums)

        # Approach 3: Greedy Algorithm
        # Simplified BFS on 1d array
        jumps = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            jumps += 1

        return jumps




    # Approach 1: Recursion(Trying all possible ways)
    def minimumJumps(self, ind, jumps, minimum, nums):
        # Base Case
        if ind >= len(nums) - 1:
            return jumps

        for jumpSize in range(1, nums[ind] + 1):
            minimum = min(minimum, self.minimumJumps(ind + jumpSize, jumps + 1, minimum, nums))
        
        return minimum

    # Approach 2: Dynamic Programming
    def minJumps(self, ind, jumps, minimum, dp, nums): 
        # Base Case
        if ind >= len(nums) - 1:
            return jumps

        if dp[ind][jumps] != -1:
            return dp[ind][jumps]

        for jumpSize in range(1, nums[ind] + 1):
            minimum = min(minimum, self.minJumps(ind + jumpSize, jumps + 1, minimum, dp, nums))
        
        dp[ind][jumps] = minimum

        return dp[ind][jumps]




        