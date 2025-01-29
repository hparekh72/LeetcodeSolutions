class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     # TC: O(n^2)
    #     # SC: O(1)
    #     n = len(nums)
    #     res = [0] * n
        
    #     for i in range(n):
    #         product = 1
    #         for j in range(n):
    #             if i == j:
    #                 continue
    #             product *= nums[j]
    #         res[i] = product
        
    #     return res

    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     # TC: O(n)
    #     # SC: O(n)
    #     n = len(nums)
    #     res = [0] * n
    #     prefix = [0] * n
    #     suffix = [0] * n

    #     prefix[0] = suffix[n - 1] = 1
    #     for i in range(1, n):
    #         prefix[i] = prefix[i - 1] * nums[i - 1]
    #     for i in range(n-2, -1, -1):
    #         suffix[i] = suffix[i + 1] * nums[i + 1] 

    #     for i in range(n):
    #         res[i] = prefix[i] * suffix[i]

    #     return res 

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # TC: O(n)
        # SC: O(1)
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix 
            prefix *= nums[i] 

        suffix = 1
        for i in range(n-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i] 
        
        return res



    
                

        
        