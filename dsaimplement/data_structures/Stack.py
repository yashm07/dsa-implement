from typing import Any, List, Optional

class StackArray():
    """
    Implementation of stack using an array

    LIFO -> last in, first out

    Attributes:
        stack (list): stores the stack
    """

    def __init__(self) -> None:
        self.stack: List[Any] = []
    
    def push(self, data: Any):
        self.stack.append(data)
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def getSize(self) -> int:
        return len(self.stack)

class Node():
    """
    Define node class - used in linked list class

    Attributes:
        data (Any): data value of node
        next (Node): stores reference to next node in linked list
    """
    def __init__(self, data: Any, next = None) -> None:
        self.data = data
        self.next = next

class StackLinkedList():
    """
    Implementation of stack using linked list with dummy header

    Attributes:
        head (Node): dummy header
        size (int): stores size of stack
    """
    def __init__(self) -> None:
        self.head = Node(None)
        self.size = 0 
    
    def push(self, data: Any):
        self.head.next = Node(data, self.head.next)
        self.size += 1
    
    def pop(self) -> Any:
        deleteNode = self.head.next
        if not deleteNode: raise Exception("Popping from empty stack")
        self.head.next = deleteNode.next
        self.size -= 1
        return deleteNode.data
    
    def peek(self) -> Any:
        if not self.head.next: raise Exception("Peeking from empty stack")
        return self.head.next.data
    
    def getSize(self) -> int:
        return self.size

    # def traverse(self):
    #     curr = self.head.next
        
    #     while curr:
    #         print(curr.data)
    #         curr = curr.next
        
