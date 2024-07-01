# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Brute Force

        if list1 == None and list2 == None:
            return None

        temp1 = list1
        temp2 = list2
        dummyNode = ListNode()
        temp = dummyNode


        while temp1 != None and temp2 != None:
            if temp1.val == temp2.val:
                temp.next = ListNode(temp1.val)
                temp = temp.next
                temp.next = ListNode(temp2.val)

                temp1 = temp1.next
                temp2 = temp2.next

            elif temp1.val < temp2.val:
                temp.next = ListNode(temp1.val)
                temp1 = temp1.next
            else:
                temp.next = ListNode(temp2.val)
                temp2 = temp2.next
            temp = temp.next
            

        while temp1 != None:
            temp.next = ListNode(temp1.val)
            temp = temp.next
            temp1 = temp1.next
        
        while temp2 != None:
            temp.next = ListNode(temp2.val)
            temp = temp.next
            temp2 = temp2.next
        
        return dummyNode.next

            
            