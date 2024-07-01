# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # Optimal

        # TC: O(2N)
        # SC: O(1)


        if head == None or head.next == None:
            return head

        length = 1
        tail = head
        while tail.next != None:
            length += 1
            tail = tail.next
        k = k % length

        temp = head
        pos = 0
        while pos < (length - k - 1):
            temp = temp.next
            pos += 1

        
        tail.next = head
        newHead = temp.next
        temp.next = None

        return newHead

        
