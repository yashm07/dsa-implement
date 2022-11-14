from typing import Any, Union

class Node():
    def __init__(self, data: Any, left = None, right = None) -> None:
        self.data = data
        self.left = left
        self.right = right
        
class BinarySearchTree():
    """
    Implementation of binary search tree using linked list implementation

    Attributes:
        stack (list): stores the stack
    """
    
    def __init__(self) -> None:
       self.root = None
       self.size = 0

    # O(log n) average case, O(n) for unbalanced tree
    def insert(self, data: Union[int, float]) -> None:
        """
        Insert node anywhere in the binary search tree. Does not include duplicate values.

        Only accepts int or float values to make searching easier in BST

        Args:
            data (int, float): value to be added to the binary search tree
        """

        # if tree does not exist, assign values
        if not self.root:
            self.root = Node(data)
            self.size += 1
        else:
            # call private method to insert node
            self.__insert(data, self.root)
    
    def __insert(self, data: Union[int, float], node):
        """
        Recursive call to insert node into binary search tree

        Args:
            data (int, float): data value
            node: pointer to node 
        """
        # if value is less than current node value
        if data < node.data:
            # if left child exists, make recursive call
            if node.left:
                self.__insert(data, node.left)
            # else, insert node
            else:
                node.left = Node(data)
                self.size += 1
        
        elif data > node.data:
            # if right child exists, make recursive call
            if node.right:
                self.__insert(data, node.right)
            # else, insert node
            else:
                node.right = Node(data)
                self.size += 1

    # O(log n) average case, O(n) for unbalanced tree
    def search(self, data: Union[int, float]) -> bool:
        """
        Search for data value in binary search tree

        Args:
            data (Union[int, float]): _description_

        Raises:
            Exception: If tree does not exist

        Returns:
            bool: Returns true/false if value is found in tree
        """
        # check if tree exists
        if not self.root:
            raise Exception("Tree does not exist.")
        else:
            # recursively call private search method 
            return self.__search(data, self.root)
    
    def __search(self, data: Union[int, float], node):
        # if value not found, return False
        if node == None:
            return False
        # if data less than node data, search left subtree
        elif data < node.data:
            return self.__search(data, node.left)
        # if data less than node data, search right subtree
        elif data > node.data:
            return self.__search(data, node.right)
        # if data == node data, return True
        else:
            return True
        
    def find_min(self) -> Union[int, float]:
        """
        Finds minimum of binary search tree using recursive approach

        Raises:
            Exception: Checks if tree does not exist

        Returns:
            (int, float): minimum value
        """
        # check if tree exists
        if not self.root:
            raise Exception("Tree does not exist.")
        else:
            # call recursive method
            return self.__find_min(self.root)
    
    def __find_min(self, node):
        # if left child exists, continue to propagate
        if node.left:
            return self.__find_min(node.left)
        else:
            # else, return minimum
            return node.data
    
    def find_max(self) -> Union[int, float]:
        """
        Finds maximum of binary search tree using recursive approach

        Raises:
            Exception: Checks if tree does not exist

        Returns:
            (int, float): maximum value
        """
        # check if tree exists
        if not self.root:
            raise Exception("Tree does not exist.")
        else:
            # call recursive method
            return self.__find_max(self.root)
    
    def __find_max(self, node):
        # if left child exists, continue to propagate
        if node.right:
            return self.__find_max(node.right)
        else:
            # else, return maximum
            return node.data

    def delete(self, data: Union[int, float]) -> None:
        """
        Deletes given value data from binary search tree using successor approach (minimum element from right subtree)

        Args:
            data (Union[int, float]): data value to be deleted

        Raises:
            Exception: Checks if tree exists
        """
        # check if tree exists
        if not self.root:
            raise Exception("Tree does not exist.")
        else:
            self.__delete(data, self.root)
    
    def __delete(self, data: Union[int, float], node):
        """
        Recursive method to delete node

        Args:
            data (Union[int, float]): data value to be deleted
            node (_type_): pointer to a node

        """
        # if data not found, make no changes to binary search tree
        if node == None:
            return node
        
        elif data > node.data:
            node.right = self.__delete(data, node.right)
        
        elif data < node.data:
            node.left = self.__delete(data, node.left)
        
        else:
            # if one child None, point to the other child
            if node.left == None:
                self.size -= 1
                return node.right
            elif node.right == None:
                self.size -= 1
                return node.left
            
            # if both child are not None, use successor approach
            node.element = self.__find_min(node.right)
            node.right = self.__delete(node.element, node.right)
        
        return node
    
    def get_size(self):
        return self.size
    
    def in_order_traversal(self):
        """
        In order traversal, prints elements in order based on value

        Raises:
            Exception: Checks if tree exists
        """
        # check if tree exists
        if not self.root:
            raise Exception("Tree does not exist.")
        else:
            # call recursive method 
            self.__in_order_traversal(self.root)
    
    def __in_order_traversal(self, node):
        """
        Prints in order traversal

        Args:
            node: pointer to node
        """
        if node != None:
            self.__in_order_traversal(node.left)
            print(f"{node.data} ")
            self.__in_order_traversal(node.right)