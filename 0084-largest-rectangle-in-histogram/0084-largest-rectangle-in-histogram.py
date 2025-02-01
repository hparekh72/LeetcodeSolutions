class Solution:
    # def largestRectangleArea(self, heights: List[int]) -> int: # Brute Force
    #     # TC: O(n^2)
    #     # SC: O(1)

    #     largest = heights[0]
    #     for i in range(len(heights)):
    #         area = 0
    #         minimum = heights[i]
    #         for j in range(i + 1, len(heights)):
    #             minimum = min(minimum, heights[j])
    #             area = max((j - i + 1) * minimum, heights[j])
    #             largest = max(largest, area)

    #     return largest

    def largestRectangleArea(self, heights: List[int]) -> int: # Stack (Optimal)
        # TC: O(n)
        # SC: O(n)

        maxArea = 0
        stack = [] # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, (i - index) * height)
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea
            


    
            

        