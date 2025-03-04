class MyQueue:
    def __init__(instance):
        instance.stack1 = []
        instance.stack2 = []
    
    def push(instance, x: int) -> None:
        instance.stack1.append(x)
    
    def pop(instance) -> int:
        if instance.stack2:
            return instance.stack2.pop()
        else:
            while instance.stack1:
                instance.stack2.append(instance.stack1.pop())
            return instance.stack2.pop()

    def peek(instance) -> int:
        return instance.stack1[0]
    
    def empty(instance) -> bool:
        return not instance.stack1 and not instance.stack2

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()