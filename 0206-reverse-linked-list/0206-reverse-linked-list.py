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

        # Optimal: Iterative
        # TC: O(N)
        # SC: O(1)

        # temp = head
        # prev = None

        # while temp != None:
        #     nextNode = temp.next
        #     temp.next = prev
        #     prev = temp
        #     temp = nextNode
        
        # return prev

        # Optimal: Recursive
        # TC: O(N)
        # SC: O(N) (Recursive Stack Space)

        if head == None or head.next == None:
            return head

        newHead = self.reverseList(head.next)
        nextNode = head.next
        nextNode.next = head
        head.next = None

        return newHead

        