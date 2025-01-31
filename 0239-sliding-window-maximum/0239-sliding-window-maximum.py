class Solution:
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]: # Brute Force
    #     # TC: O(n * k)
    #     # SC: O(1)

    #     maxWindow = [] 
    #     for i in range(len(nums) - k + 1):
    #         maximum = float('-inf')
    #         for j in range(i, i + k):
    #             maximum = max(maximum, nums[j])
    #         maxWindow.append(maximum)

    #     return maxWindow

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]: # Sliding Window (Monotonically Decreasing Queue)
        # TC: O(n)
        # SC: O(n)

        output = []
        q = collections.deque() # index
        l = 0
        r = 0

        while r < len(nums):
            # pop smaller values from the queue
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            # remove left value from the window
            if l > q[0]:
                q.popleft()


            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1

            r += 1

        return output

            








    
        


        

    # [3,1,-1,-3,5,3,6,7]
