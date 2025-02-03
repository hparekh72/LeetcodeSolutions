class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Brute Force: Sorting
        # TC: O(NlogN)
        # SC: O(1)

        # Better: Hashing
        # TC: O(N)
        # SC: O(N)

        # Optimal: Linked List Cycle, slow and fast pointers
        # Floyd's Tortoise and Hare (Cycle Detection) algorithm

        # Intuition: 

        # Treating the Array as a Linked List:
            # 1) Imagine each index as a node in a linked list.
            # 2) The value at each index points to the next node.

        # Why a Cycle Exists:
            # 1) Since there's a duplicate number, it creates a cycle in the linked list representation.
            # 2) The entrance to this cycle represents the duplicate number.

        # TC: O(N)
        # SC: O(1)

        # First Phase: Detect if a cycle exists (slow and fast pointers meet).

        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        # Second Phase: Find the start of the cycle (the duplicate number).
        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow






      