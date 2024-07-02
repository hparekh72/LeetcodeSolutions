# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Brute Force: Use a list or stack and modify the list 
        # TC: O(2N)
        # SC: O(N)

        # Optimal: Reverse the second half of the list and then traverse from start and end 
        # TC: O(2N)
        # SC: O(1)

        # Find the middle of the list

        middle = self.findMiddle(head)
        second = middle.next
        middle.next = None    # Seperated the list into two

        secondHead = self.reverse(second) # Reverse the second half

        temp1 = head
        temp2 = secondHead
        nextNode1, nextNode2 = None, None

        while temp2 != None:
            nextNode1 = temp1.next
            nextNode2 = temp2.next

            temp1.next = temp2
            temp2.next = nextNode1

            temp1 = nextNode1
            temp2 = nextNode2

        return head


    def findMiddle(self, head):
        slow, fast = head, head

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow


    def reverse(self, head):
        temp = head
        prev, nextNode = None, None

        while temp != None:
            nextNode = temp.next 
            temp.next = prev
            prev = temp
            temp = nextNode

        return prev






        


        # Reverse the second half





        