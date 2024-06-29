# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Brute Force
        # TC: O(2N)
        # SC: O(1)

        # if head.next == None:
        #     return None

        # temp = head
        # length = 0

        # while temp != None:
        #     length += 1
        #     temp = temp.next

        # mid = length // 2

        # temp = head
        # prev = None
        # pos = 0
        # while temp != None:
        #     if pos == mid:
        #         prev.next = temp.next
        #         del temp
        #         break
        #     pos += 1
        #     prev = temp
        #     temp = temp.next

        # return head

        # Optimal: Slow and Fast pointers
        # TC: O(N/2)
        # SC: O(1)

        if head.next == None:
            return None

        slow = head
        fast = head
        prev = None

        while fast != None and fast.next != None:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next
        return head
        

        