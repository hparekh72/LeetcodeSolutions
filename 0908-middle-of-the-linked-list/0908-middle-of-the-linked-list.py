# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Brute Force
        # TC: O(N) + O(N/2)

        # temp = head
        # length = 0

        # while temp != None:
        #     length += 1
        #     temp = temp.next

        # mid = length // 2


        # temp = head
        # pos = 0
        # while pos < mid:
        #     pos += 1
        #     temp = temp.next
        
        # return temp

        # Optimal: Tortoise and Hare approach
        # TC: O(N/2)
        # SC: O(1)

        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow




        
        