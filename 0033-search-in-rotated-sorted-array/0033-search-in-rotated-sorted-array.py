# Note in binary search problems, elimination is the key
# Identify the sorted half

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid

            # Identify the sorted hald
            if nums[l] <= nums[mid]: # Left half is sorted
                # Check if target is present in the sorted half
                if nums[l] <= target and target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            else:   # Right half is sorted
                # Check if target is present in the sorted half
                if nums[mid] <= target and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1



                
        