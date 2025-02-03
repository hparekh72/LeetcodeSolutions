# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: # Brute Force
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

    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: # Iterative
    #     # TC: O(n)
    #     # SC: O(1)

    #     prev, curr = None, head

    #     while curr:
    #         nextNode = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = nextNode

    #     return prev

        def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: # Recursive
            # TC: O(n)
            # SC: O(n)

            if head == None or head.next == None:   # Base Case
                return head

            newHead = self.reverseList(head.next)
            nextNode = head.next
            nextNode.next = head
            head.next = None

            return newHead






        
        