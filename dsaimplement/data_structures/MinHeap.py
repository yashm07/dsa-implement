from typing import Optional, Any

class MinHeap():
    def __init__(self, capacity: int) -> None:
        """
        Min Heap implementation using array implementation

        Finding min - O(n)
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
    
    def get_min(self) -> int:
        """
        Returns minimum value (from root in min heap) and deletes min value

        Raises:
            Exception: Empty heap

        Returns:
            int: min value
        """
        if not self.size:
            raise Exception("Empty heap.")
        
        # get min value
        min = self.heap[0]

        # swap with last element, and delete last element
        self.heap[0] = self.heap[self.size-1]
        self.heap[self.size-1] = 0

        # shift element down
        self.size -= 1
        self.__shift_down(0)

        # return min
        return min
        
    def __shift_up(self, pos: int) -> None:
        """
        Private method to shift element up tree - used when inserting element

        Args:
            pos (int): current position
        """
        parent_index = self.__parent_index(pos)

        # while parent exists and parent is greater than child
        while parent_index >= 0 and self.heap[parent_index] > self.heap[pos]:
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
            # get the smaller child
            small_child = self.__min_child(pos)

            # if current element is greater than smallest child, swap
            if self.heap[pos] > self.heap[small_child]:
                self.heap[pos], self.heap[small_child] = self.heap[small_child], self.heap[pos]
            
            pos = small_child
            
    def __min_child(self, pos: int) -> int:
        """
        Private method to get minimum child - used in shift down method

        Args:
            pos (int): current position

        Returns:
            int: index of minimum child
        """
        
        right_child = self.__right_child(pos)
        left_child = self.__left_child(pos)
        
        # if only 1 child, return that index
        if right_child > self.size:
            return left_child
        else:
            if self.heap[left_child] < self.heap[right_child]:
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