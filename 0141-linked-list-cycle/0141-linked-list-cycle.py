# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # def hasCycle(self, head: Optional[ListNode]) -> bool: # Brute Force
        # TC: O(N)
        # SC: O(N)

        # temp = head
        # hashSet = set()
        # while temp != None:
        #     if temp in hashSet:
        #         return True
        #     hashSet.add(temp)
        #     temp = temp.next

        # return False

        def hasCycle(self, head: Optional[ListNode]) -> bool: # Slow and Fast pointer(Optimal)
            
            # TC: O(N)
            # SC: O(1)

            slow, fast = head, head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

                if slow == fast:
                    return True
            
            return False


