# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Brute Force:

        # TC: O(2N)
        # SC: O(N)

        # if head == None or head.next == None or head.next.next == None:
        #     return head

        # dummyNode = ListNode()
        # curr = dummyNode
        
        # temp = head
        # while temp != None:
        #     node = ListNode(temp.val)
        #     curr.next = node
        #     curr = curr.next

        #     if temp.next:
        #         temp = temp.next.next
        #     else:
        #         temp = temp.next

        # temp = head.next
        # while temp != None:
        #     node = ListNode(temp.val)
        #     curr.next = node
        #     curr = curr.next

        #     if temp.next:
        #         temp = temp.next.next
        #     else:
        #         temp = temp.next

        # return dummyNode.next

        # Optimal:
        # TC: O(N)
        # SC: O(1)

        if head == None or head.next == None:
            return head

        odd = head
        even = head.next
        evenHead = head.next

        # Note: If Even has not reached the end, then odd will also not reach. 

        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next

            odd = odd.next
            even = even.next

        odd.next = evenHead

        return head


        

        