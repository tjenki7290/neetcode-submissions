import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        d = ListNode()

        for i, node in enumerate(lists): #this will populate our heap to start it off
            if node:# makes sure the linked list has a head
                heapq.heappush(heap, (node.val, i, node)) # need the index because if two values are the same then python's heap will try and compare by memory addresses('node') if you don't include the index

        curr = d

        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = node
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, i, node))

        return d.next