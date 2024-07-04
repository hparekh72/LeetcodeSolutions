# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Brute Force
        # TC: (n * k) + (n*k)log(n*k) + O(n*k)
        # SC: O(2*n*k)

        # arr = []

        # for i in range(len(lists)): # Storing all the lists items in an array
        #     head = lists[i]
        #     temp = head
        #     while temp != None:
        #         arr.append(temp.val)
        #         temp = temp.next
        
        # arr.sort()

        # dummyNode = ListNode()
        # temp = dummyNode

        # for i in range(len(arr)): # Creating a new LL for the result
        #     temp.next = ListNode(arr[i])
        #     temp = temp.next

        # return dummyNode.next

        # Optimal: Using Priority Queue
        # TC: O(k) + O(n*k)
        # SC: O(k)

        heap = []

        # for i in range(len(lists)):
        #     head = lists[i]
        #     heapq.heappush(heap, (head.val, i, head))

        for index, head in enumerate(lists):
            if head:                  # To handle Edge Case: [[]]
                heapq.heappush(heap, (head.val, index, head))


        dummyNode = ListNode() 
        temp = dummyNode
        while heap:
            val, index, node = heapq.heappop(heap)
            temp.next = node
            nextNode = node.next
            if nextNode:
                heapq.heappush(heap, (nextNode.val, index, nextNode))

            temp = temp.next

        return dummyNode.next

        



        