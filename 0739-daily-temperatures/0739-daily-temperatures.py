class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]: # Monotonic Stack (Decreasing) 
        # TC: O(n)
        # SC: O(n)

        stack = [] # pair: [temp, index]
        res = [0] * len(temperatures)

        for ind, temp in enumerate(temperatures):
            while stack and temperatures[ind] > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = ind - stackInd
            stack.append([temp, ind])

        return res








        

        