# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # if not same length, just append the extra stuff

        head = mergedCurr = ListNode()
        curr1 = list1
        curr2 = list2
        while curr1 and curr2:
            if curr1.val < curr2.val:
                mergedCurr.next = curr1
                curr1 = curr1.next  
            else:
                mergedCurr.next = curr2
                curr2 = curr2.next
            mergedCurr = mergedCurr.next
        # add extra nodes
        if curr1:
            mergedCurr.next = curr1
        else:
            mergedCurr.next = curr2
        return head.next