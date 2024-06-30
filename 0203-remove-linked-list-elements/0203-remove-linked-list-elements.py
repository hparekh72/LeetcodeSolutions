# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        # TC: O(N)
        # SC: O(1)
        temp = head
        prev = None

        while temp != None:
            if temp.val == val:
                if temp == head: # If 1st node is to be deleted
                    head = temp.next
                else:
                    prev.next = temp.next
                temp = temp.next
            else:
                prev = temp
                temp = temp.next

        return head
            