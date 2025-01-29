class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: # 2 pointer approach (Optimal)
        # TC: O(nlogn) + O(n^2)
        # SC: O(1)

        res = []

        nums.sort()

        for i in range(len(nums)):
            if i > 0  and nums[i] == nums[i - 1]: # Skip Duplicates
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1

                    while nums[l] == nums[l - 1] and l < r: # Skip Duplicates
                        l += 1

        return res

            

