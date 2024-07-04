# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Brute Force
        # TC: O(n) + O(nlogn) + O(n)
        # SC: O(N)

        if head == None or head.next == None:
            return head

        arr = []

        temp = head
        while temp != None:
            arr.append(temp.val)
            temp = temp.next

        arr.sort()

        temp = head
        for idx in range(len(arr)):
            temp.val = arr[idx]
            temp = temp.next

        return head


        # Optimal: Using Merge Sort

        

        

        

        