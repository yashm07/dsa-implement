from typing import Optional, Any

class Node():
    """
    Define node class - used in linked list class

    Attributes:
        data (Any): data value of node
        next (Node): stores reference to next node in linked list
    """
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next: Optional[Node] = None

class LinkedList():
    """
    Linked list implementation with dummy header
    
    """
    def __init__(self) -> None:
        self.head: Node = Node(None)
        self.size: int = 0
    
    # O(1) time comeplexity
    def insert_start(self, data: Any):
        # create new node with data
        newNode = Node(data)

        # set pointers
        newNode.next = self.head.next
        self.head.next = newNode

        # update size
        self.size += 1
    
    # O(n) time complexity due to traversing
    def insert_end(self, data: Any):
        # create new node with data
        newNode = Node(data)

        currentNode = self.head
        
        # traverse through list 
        while currentNode.next:
            currentNode = currentNode.next
        
        # point last element to new node
        currentNode.next = newNode
        
        # update size
        self.size += 1
    
    # removal is quick if location is known
    def remove(self, data: Any): 
        """
        Removes first instance of data value
        """ 
        currentNode = self.head

        # traverse till end of list
        while currentNode.next:
            # check if the next value is the desired value
            if currentNode.next.data == data:
                # assign next pointer to the value after the next node
                currentNode.next = currentNode.next.next
                # update size
                self.size -= 1
                return
            
            currentNode = currentNode.next
        
        # otherwise, element not in list
        print("Element not in list.")
    
    # O(1) time complexity if size attribute is stored 
    def get_size(self) -> int:
        return self.size        
    
    # O(n) time complexity due to list traversal
    def return_list(self) -> list:
        currentNode = self.head.next
        ll_arr = []

        while currentNode:
            ll_arr.append(currentNode.data)
            currentNode = currentNode.next
        
        return ll_arr


        

