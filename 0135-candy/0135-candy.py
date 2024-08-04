# Brute Force: Consider the left and right neighbors seperately
# TC: O(n) + O(n) + O(n) = O(3n)
# SC: O(n) + O(n) = O(2n)

# Better: Modified Brute Force
# TC: O(n) + O(n) = O(2n)
# SC: O(n)

# Optimal: Slope Approach Intuition
# TC: O(n)
# SC: O(1)

# Brute Force
# class Solution:
#     def candy(self, ratings: List[int]) -> int:
#         # Only consider left neighbors ratings and give candies accordingly
#         left = [1] * len(ratings)
#         for i in range(1, len(ratings)):
#             if ratings[i] > ratings[i-1]:
#                 left[i] = left[i-1] + 1

#         # Only consider right neighbors ratings and give candies accordingly
#         right = [1] * len(ratings)
#         for i in range(len(ratings) - 2, -1, -1):
#             if ratings[i] > ratings[i+1]:
#                 right[i] = right[i+1] + 1

#         # Consider left and right neighbors by taking the maximum
#         res = 0
#         for i in range(len(ratings)):
#             res += max(left[i], right[i])

#         return res

# Better: Modified Brute Force  
# class Solution:
#     def candy(self, ratings: List[int]) -> int:
#         # Only consider left neighbors ratings and give candies accordingly
#         left = [1] * len(ratings)
#         for i in range(1, len(ratings)):
#             if ratings[i] > ratings[i-1]:
#                 left[i] = left[i-1] + 1

#         # Calculate the right neigbor and the res
#         curr, right = 1, 1
#         # As the right array starts from len(ratings) - 2, we need to consider the last element result
#         res = max(left[len(left) - 1], 1) 
#         for i in range(len(ratings) - 2, -1, -1):
#             if ratings[i] > ratings[i+1]:
#                 curr = right + 1
#                 right = curr
#             else:
#                 curr = 1
#             res += max(left[i], curr)

#         return res

# Optimal
class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        res = 1
        i = 1
        while i < len(ratings):
            if ratings[i] == ratings[i-1]:
                res += 1
                i += 1
                continue

            peak = 1
            while i < len(ratings) and ratings[i] > ratings[i-1]:
                peak += 1
                res += peak
                i += 1
            
            down = 1
            while i < len(ratings) and ratings[i] < ratings[i-1]:
                res += down
                down += 1
                i += 1

            if down > peak:
                res += (down - peak)

        return res
            
