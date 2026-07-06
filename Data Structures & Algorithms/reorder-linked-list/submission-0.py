# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        prev = None

        while second: #reverses the second half linked list so that our pointer can start at the end and work inwards
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        #merge the two halves 
        second = prev #second = prev because our second var went out of bounds to None during the while loop
        first = head
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2


