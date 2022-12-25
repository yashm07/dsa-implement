from typing import Optional, Any

class MaxHeap():
    def __init__(self, capacity: int) -> None:
        """
        Max Heap implementation using array implementation

        Finding max - O(n)
        Insertion, deletion - O(log n) (complete binary tree)

        Args:
            capacity (int): max size of array
        """
        self.heap = [0] * capacity
        self.capacity = capacity
        self.size = 0
        
    def insert(self, val: int) -> None:
        """
        Insert value into heap

        Args:
            val (int): value

        Raises:
            Exception: Heap is full
        """
        if self.is_full():
            raise Exception("Heap is full.")
        
        self.heap[self.size] = val
        self.__shift_up(self.size)
        self.size += 1
    
    def get_max(self) -> int:
        """
        Returns maximum value (from root in max heap) and deletes max value

        Raises:
            Exception: Empty heap

        Returns:
            int: max value
        """
        if not self.size:
            raise Exception("Empty heap.")
        
        # get max value
        max = self.heap[0]

        # swap with last element, and delete last element
        self.heap[0] = self.heap[self.size-1]
        self.heap[self.size-1] = 0

        # shift element down
        self.size -= 1
        self.__shift_down(0)

        # return max
        return max
        
    def __shift_up(self, pos: int) -> None:
        """
        Private method to shift element up tree - used when inserting element

        Args:
            pos (int): current position
        """
        parent_index = self.__parent_index(pos)

        # while parent exists and parent is less than child
        while parent_index >= 0 and self.heap[parent_index] < self.heap[pos]:
            # swap values
            self.heap[parent_index], self.heap[pos] = self.heap[pos], self.heap[parent_index]
            
            pos = parent_index
            parent_index = self.__parent_index(pos)
    
    def __shift_down(self, pos:int) -> None:
        """
        Private method to shift element down tree - used when deleting max

        Args:
            pos (int): current position
        """
        # while there is a child
        while self.__left_child(pos) < self.size:
            # get the larger child
            big_child = self.__max_child(pos)

            # if current element is smaller than largest child, swap
            if self.heap[pos] < self.heap[big_child]:
                self.heap[pos], self.heap[big_child] = self.heap[big_child], self.heap[pos]
            
            pos = big_child
            
    def __max_child(self, pos: int) -> int:
        """
        Private method to get maximum child - used in shift down method

        Args:
            pos (int): current position

        Returns:
            int: index of maximum child
        """
        
        right_child = self.__right_child(pos)
        left_child = self.__left_child(pos)
        
        # if only 1 child, return that index
        if right_child > self.size:
            return left_child
        else:
            if self.heap[left_child] > self.heap[right_child]:
                return left_child
            else:
                return right_child
    
    def is_full(self) -> bool:
        """
        Checks if heap is full

        Returns:
            bool: True/False
        """
        return self.capacity-1 == self.size
    
    def __parent_index(self, pos: int) -> int:
        """
        Private method to get parent index (using 0 indexed heap)
        """
        return (pos-1) // 2
    
    def __left_child(self, pos: int) -> int:
        """
        Private method to get left child index
        """
        return 2 * pos + 1
    
    def __right_child(self, pos: int) -> int:
        """
        Private method to get right child index
        """
        return 2 * pos + 2