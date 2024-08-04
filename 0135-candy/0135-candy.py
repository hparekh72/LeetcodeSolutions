# Brute Force

class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Only consider left neighbors ratings and give candies accordingly
        left = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1] + 1

        
        print(left)
        # Only consider right neighbors ratings and give candies accordingly
        right = [1] * len(ratings)
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right[i] = right[i+1] + 1


        print(right)
        # Consider left and right neighbors by taking the maximum
        res = 0
        for i in range(len(ratings)):
            res += max(left[i], right[i])

        return res

