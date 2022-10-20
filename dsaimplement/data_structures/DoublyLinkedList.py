from typing import Optional, Any

class Node():
    """
    Define node class - used in doubly linked list class

    Attributes:
        data (Any): data value of node
        next (Node): stores reference to next node in linked list
        prev (Node): stores reference to previous node in linked list
    """
    def __init__(self, data: Any, next = None, prev = None) -> None:
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList():
    """
    Doubly linked list implementation without dummy nodes and with tail
    
    """
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size: int = 0

    def insert_start(self, data: Any):
        """
        insert node at start of list - O(1) time complexity

        Args:
            data (Any): data value
        """
        newNode = Node(data, self.head)
        self.head = newNode
        # if empty list, assign tail
        if not self.head:    
            self.tail = newNode
            return
        
        self.head.prev = newNode
        self.size += 1
    
    def insert_end(self, data: Any):
        """
        insert node at end of list - O(1) time complexity

        Args:
        data (Any): data value
        """
        newNode = Node(data, prev=self.tail)
        self.tail = newNode
        # if empty list, assign head
        if not self.tail:
            self.head = newNode
            return

        self.tail.next = newNode
        self.size += 1
    
    
    def return_list(self) -> list:
        """
        returns linked list - O(n) time complexity

        Returns:
            list: returns list
        """
        currentNode = self.head
        ll_arr = []

        while currentNode:
            ll_arr.append(currentNode.data)
            currentNode = currentNode.next
        
        return ll_arr
    
    def remove(self, data: Any):
        """
        removes first occurence of data from linked list

        Args:
            data (Any): data value
        """
        if not self.head: return
        



ll = DoublyLinkedList()
ll.insert_start(50)
print(ll.return_list())

