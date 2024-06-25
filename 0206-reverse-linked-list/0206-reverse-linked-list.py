# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Brute Force
        #TC: O(2N)
        #SC: O(N)

        # temp = head
        # stack = []
        # while temp != None:
        #     stack.append(temp.val)
        #     temp = temp.next

        # temp = head
        # while temp != None:
        #     temp.val = stack.pop(-1)
        #     temp = temp.next

        # return head

        # Optimal
        # TC: O(N)
        # SC: O(1)

        temp = head
        prev = None

        while temp != None:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
        
        return prev

        