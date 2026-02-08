"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        def dfs(curr):
            if not curr.child and not curr.next:
                return curr
            if not curr.child:
                return dfs(curr.next)
            tail = dfs(curr.child)
            oldNext = curr.next
            curr.next = curr.child
            curr.child.prev = curr
            curr.child = None
            tail.next = oldNext
            if oldNext:
                oldNext.prev = tail
                return dfs(oldNext)
            return tail
        
        dfs(head)
        return head