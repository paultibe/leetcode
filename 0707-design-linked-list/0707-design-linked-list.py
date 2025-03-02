class Node:
  def __init__(currentInstance, val, nextNode=None):
    currentInstance.val = val
    currentInstance.next = nextNode

class MyLinkedList:
    # create empty linked list
    def __init__(currentInstance):
        currentInstance.head = None
        currentInstance.size = 0

    def get(currentInstance, index: int) -> int:
        if (index < 0 or index >= currentInstance.size):
            return -1
        # traverse to index
        currIndex = 0 
        curr = currentInstance.head
        while currIndex != index:
            currIndex += 1
            curr = curr.next
    
        return curr.val

    def addAtHead(currentInstance, val: int) -> None:
        newNode = Node(val, currentInstance.head)
        currentInstance.head = newNode
        currentInstance.size += 1

    def addAtTail(currentInstance, val: int) -> None:
        newNode = Node(val)
        curr = currentInstance.head
        if not currentInstance.head:
            currentInstance.head = newNode
            currentInstance.size += 1
            return
        currIndex = 0
        while currIndex != currentInstance.size - 1:
            curr = curr.next
            currIndex += 1
        curr.next = newNode
        currentInstance.size += 1
        

    def addAtIndex(currentInstance, desiredIndex: int, val: int) -> None:
        if (desiredIndex < 0 or desiredIndex > currentInstance.size):
            return
    # first index, O(1)
        if desiredIndex == 0:
            currentInstance.addAtHead(val)
            return
        
        # else traverse to node before
        curr = currentInstance.head
        currIndex = 0
        while currIndex != desiredIndex - 1:
            currIndex += 1
            curr = curr.next
        
        # insert
        newNode = Node(val, curr.next)
        curr.next = newNode
        currentInstance.size += 1

    def deleteAtIndex(currentInstance, index: int) -> None:
        if (index < 0 or index >= currentInstance.size):
            return
        if index == 0:
            if currentInstance.head:
                currentInstance.head = currentInstance.head.next
                currentInstance.size -= 1
            return
        # travese to node before
        curr = currentInstance.head
        currIndex = 0
        while (currIndex != index - 1):
            currIndex += 1
            curr = curr.next 
        # at node before
        curr.next = curr.next.next
        currentInstance.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)