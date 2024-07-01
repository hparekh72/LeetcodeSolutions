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
        while tail.next != None:  # Find length and tail
            length += 1
            tail = tail.next

        
        k = k % length 

        if k == 0:
            return head 

        tail.next = head # Connecting the end of the list with the head node

        newLastNode = self.findNthNode(head, length - k)

        head = newLastNode.next
        newLastNode.next = None
        
        return head

    def findNthNode(self, head, k):
        temp = head
        count = 1
        while temp != None:
            if count == k:
                return temp
            count += 1
            temp = temp.next
        return temp

