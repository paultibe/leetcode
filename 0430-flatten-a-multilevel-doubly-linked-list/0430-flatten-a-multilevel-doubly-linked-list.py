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
            tail = curr
            if curr.child:
                tail = dfs(curr.child)
                oldNext = curr.next
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None
                tail.next = oldNext
                if oldNext:
                    oldNext.prev = tail
                if oldNext:
                    return dfs(oldNext)
                return tail
            elif not curr.next:
                # this is tail
                return curr
            else:
                # return eventual tail
                return dfs(curr.next)
        
        dfs(head)
        return head