# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None or head.next == None or head.next.next == None:
            return head

        dummyNode = ListNode()
        curr = dummyNode
        
        temp = head
        while temp != None:
            node = ListNode(temp.val)
            curr.next = node
            curr = curr.next

            if temp.next:
                temp = temp.next.next
            else:
                temp = temp.next

        temp = head.next
        while temp != None:
            node = ListNode(temp.val)
            curr.next = node
            curr = curr.next

            if temp.next:
                temp = temp.next.next
            else:
                temp = temp.next

        return dummyNode.next

        

        