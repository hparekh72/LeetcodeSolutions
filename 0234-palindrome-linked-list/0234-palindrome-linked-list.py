# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # Brute Force:
        # TC: O(2N)
        # SC: O(N)

        # temp = head
        # stack = []

        # while temp != None:
        #     stack.append(temp.val)
        #     temp = temp.next

        # temp = head
        # while temp != None:
        #     data = stack.pop(-1)
        #     if temp.val != data:
        #         return False
        #     temp = temp.next

        # return True

        # Optimal: Slow and Fast Pointers
        # TC: O(2N)
        # SC: O(1)

        if head == None or head.next == None:
            return head

        slow = head
        fast = head

        while fast.next != None and fast.next.next != None: # TC: O(N/2)
            slow = slow.next
            fast = fast.next.next

        newHead = self.reverse(slow.next) # TC: O(N/2)

        first = head
        second = newHead

        while second != None:     # TC: O(N/2)
            if first.val != second.val:
                self.reverse(newHead)
                return False
            first = first.next
            second = second.next

        self.reverse(newHead)  # TC: O(N/2)
        
        return True

        

    def reverse(self, head):
        temp = head
        prev = None
        while temp != None:
            nextNode = temp.next
            temp.next = prev
            prev = temp
            temp = nextNode

        return prev

        




        
        