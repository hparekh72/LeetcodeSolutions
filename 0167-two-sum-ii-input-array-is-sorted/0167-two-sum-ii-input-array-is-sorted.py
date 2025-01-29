class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:# 2 pointer approach
        # TC: O(n)
        # SC: O(n)

        n = len(numbers)
        l = 0
        r = n - 1

        while l < r:
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                return [l + 1, r + 1]
        
        
         