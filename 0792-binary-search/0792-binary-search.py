# class Solution:
#     # TC: O(logn)
#     # SC: O(logn) (Recursive Stack Space)
#     def search(self, nums: List[int], target: int) -> int: # Recursive
#         return self.binarySearch(0, len(nums) - 1, nums, target)

#     def binarySearch(self, l, r, nums, target):
#         # Base Case
#         if l > r:
#             return -1
        
#         mid = l + (r - l) // 2 # Get middle index

#         if nums[mid] == target:
#             return mid
#         if nums[mid] < target: # Search Right
#             return self.binarySearch(mid + 1, r, nums, target)

#         return self.binarySearch(0, mid - 1, nums, target) # Search left


class Solution:
    # TC: O(logn)
    # SC: O(1) 
    def search(self, nums: List[int], target: int) -> int: # Iterative
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid  - 1

        return -1
        


        

    




        