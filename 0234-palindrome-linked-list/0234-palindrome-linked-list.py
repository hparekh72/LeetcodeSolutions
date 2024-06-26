# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # Brute Force:
        # TC: O(2N)
        # SC: O(1)

        temp = head
        stack = []

        while temp != None:
            stack.append(temp.val)
            temp = temp.next

        temp = head
        while temp != None:
            data = stack.pop(-1)
            if temp.val != data:
                return False
            temp = temp.next

        return True
        
        