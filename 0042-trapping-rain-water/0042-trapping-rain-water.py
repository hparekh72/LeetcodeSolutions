class Solution:
    def trap(self, height: List[int]) -> int:
        # Approach1: Using extra time (2 loops)
        # min(maxLeft, maxRight) - height[i]
        # Calculare the maxLeft and maxRight for each index
        # TC: O(N^2)
        # SC: O(N)

        # Approach2: Using extra space
        # min(maxLeft, maxRight) - height[i]
        # Store the maxLeft and maxRight for each index in seperate arrays
        # TC: O(N)
        # SC: O(N)

        # n = len(height)
        # if n == 0:
        #     return 0

        # leftMax = [0] * n
        # rightMax = [0] * n

        # leftMax[0] = height[0]
        # for i in range(1, n):
        #     leftMax[i] = max(leftMax[i-1], height[i])

        # rightMax[n - 1] = height[n - 1]
        # for i in range(n - 2, -1, -1):
        #     rightMax[i] = max(rightMax[i + 1], height[i])

        # res = 0
        # for i in range(n):
        #     res += min(leftMax[i], rightMax[i]) - height[i]

        # return res

        # Approach3: Two Pointer
        # TC: O(N)
        # SC: O(1)

        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                # res += max(leftMax - height[l], 0)
                # leftMax = max(leftMax, height[l])

                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]

            else:
                r -= 1
                # res += max(rightMax - height[r], 0)
                # rightMax = max(rightMax, height[r])

                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res
            

 