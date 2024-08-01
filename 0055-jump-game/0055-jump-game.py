class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Greedy Approach
        # TC: O(n)
        # SC: O(1)
        
        max_index = 0
        for ind in range(len(nums)):
            
            if ind > max_index:
                return False

            max_index = max(max_index, ind + nums[ind])

            if max_index >= len(nums) - 1:
                return True

        return True
            


        