class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # Brute Force: Sorting
        # TC: O(NlogN)
        # SC: O(1)

        # Better: Hashing
        # TC: O(N)
        # SC: O(N)

        # Optimal: Linked List Cycle, slow and fast pointers
        # TC: O(N)
        # SC: O(1)

        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
