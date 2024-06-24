# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Brute Force
        #TC: O(2N)
        #SC: O(1)

        if head.next == None:
            return 

        temp = head
        length = 0
        while temp != None: # Calculate the length
            length += 1
            temp = temp.next

        if n == length:
            head = head.next
            return head

        posToDelete = length - n

        temp = head
        prev = None
        while temp != None:
            if posToDelete == 0:
                prev.next = temp.next
                del temp
                break
            posToDelete -= 1
            prev = temp
            temp = temp.next

        return head