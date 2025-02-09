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
        if not head.next:
            return 
        array = []
        while head:
            array.append(head)
            head = head.next
        left, right = 0, len(array) - 1
        while left < right:
            temp = array[left].next # next is null
            array[left].next = array[right] # next is self
            array[right].next = temp # next is null
            left += 1
            right -= 1
        array[left].next = None

        