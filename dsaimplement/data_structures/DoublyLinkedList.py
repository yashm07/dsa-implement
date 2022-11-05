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
    Doubly linked list implementation with dummy nodes and tail
    
    """
    def __init__(self) -> None:
        self.head: Node = Node(None)
        self.tail: Node = Node(None, prev=self.head)
        self.head.next = self.tail

        self.size: int = 0

    def insert_start(self, data: Any):
        """
        insert node at start of list - O(1) time complexity

        Args:
            data (Any): data value
        """
        # assign pointers
        newNode = Node(data, self.head.next, self.head)
        newNode.next.prev = newNode
        self.head.next = newNode

        # increase size
        self.size += 1
    
    def insert_end(self, data: Any):
        """
        insert node at end of list - O(1) time complexity

        Args:
        data (Any): data value
        """
        # assign pointers
        newNode = Node(data, self.tail, self.tail.prev)
        newNode.prev.next = newNode
        self.tail.prev = newNode

        # increase size
        self.size += 1
    
    def return_list(self) -> list:
        """
        returns linked list - O(n) time complexity

        Returns:
            list: returns list
        """
        currentNode = self.head.next
        ll_arr = []

        # traverse through list
        while currentNode and currentNode != self.tail:
            ll_arr.append(currentNode.data)
            currentNode = currentNode.next
        
        return ll_arr
    
    def remove(self, data: Any):
        """
        removes first occurence of data from linked list

        Args:
            data (Any): data value
        """
        currentNode = self.head

        # traverse through list until end
        while currentNode.next != self.tail:
            # if next node matches data
            if currentNode.next.data == data:
                # assign pointers
                currentNode.next = currentNode.next.next
                currentNode.next.prev = currentNode
                return            
            
            # traverse through list
            currentNode = currentNode.next
        
        # element does not exist in the linked list
        print("Element does not exist.")
