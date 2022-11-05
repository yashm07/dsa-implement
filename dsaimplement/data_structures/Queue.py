from typing import Any, List

from matplotlib.lines import Line2D


class QueueArray():
    """
    Implementation of queue using an array 
    - For other languages, like C/C++ circular array implementation can be used

    FIFO -> first in, first out
    """

    def __init__(self) -> None:
        self.queue: List[Any] = []
        self.size: int = 0
    
    def enqueue(self, data: Any) -> None:
        # add to end of array 
        self.queue.append(data)
        self.size += 1
    
    def dequeue(self) -> Any:
        # delete from start array 
        if not self.size:
            raise Exception("Dequeuing from empty queue")
        val = self.queue[0]
        del self.queue[0]
        self.size -= 1
        return val
    
    def get_size(self) -> int:
        return self.size
    
    def peek(self) -> int:
        return self.queue[0]

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

class QueueLinkedList():
    """
    Implementation of queue using linked list with dummy header

    Enqueue adds node to end of linked list, dequeue deletes node from start of linked list 

    Attributes:
        head (Node): dummy header
        size (int): stores size of stack
        tail (Node): points to last node
    """

    def __init__(self) -> None:
        self.head = Node(None)
        self.tail = self.head
        self.size = 0
    
    def enqueue(self, data: Any) -> None:
        self.tail.next = Node(data)
        self.tail = self.tail.next
        self.size += 1
    
    def dequeue(self) -> Any:
        if self.size == 1:
            self.tail = self.head
        delete_node = self.head.next
        val = delete_node.data
        self.head.next = delete_node.next
        self.size -= 1
        return val

    def peek(self) -> Any:
        if not self.head.next:
            raise Exception("No nodes in queue")
        return self.head.next.data
    
    def get_size(self) -> int:
        return self.size
    
    def traverse(self):
        curr = self.head.next
        while curr:
            print(curr.data)
            curr = curr.next





