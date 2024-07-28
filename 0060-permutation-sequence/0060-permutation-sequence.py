class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Brute Force:
        # Store all the elements from 1 to n in a list in an ascending order.
        # Generate all permutations from 1 to n. 
        # The kth permutation will be at the (k-1)th index.

        # TC: O(n) (list) + O(n!) * O(n) (putting the list into result)
        # SC: O(n) + O(n) (recursive stack space)

        # Optimal
        # TC: O(n^2)
        # SC: O(n)

        fact = 1
        nums = []
        for i in range(1, n+1):
            fact = i * fact
            nums.append(i)
    
        k -= 1 # 0-based indexing

        res = ""
        while len(nums) > 0:
            fact = fact // len(nums)
            res += str(nums[k // fact])
            nums.remove(nums[k // fact]) # TC: O(n)
            k = k % fact

        return res


    
        




        