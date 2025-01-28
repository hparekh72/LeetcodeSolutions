class Solution:

    # TC: O(n^2)
    # SC: O(1)

    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]

    #     return []


    # TC: O(nlogn)
    # SC: O(n)

    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     arr = []
    #     for ind, num in enumerate(nums):
    #         arr.append([num, ind])

    #     arr.sort()

    #     l = 0
    #     r = len(nums) - 1

    #     while l < r:
    #         curr = arr[l][0] + arr[r][0]
    #         if curr == target:
    #             return [arr[l][1], arr[r][1]]
    #         elif curr < target:
    #             l += 1
    #         else:
    #             r -= 1

    #     return []

    # TC: O(n)
    # SC: O(n)

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for ind, num in enumerate(nums):
            diff = target - num
            if diff in hashMap:
                return [ind, hashMap[diff]]
            else:
                hashMap[num] = ind

        return []






        