from typing import Union

def binarySearchIterative(arr: Union[int, float], l: int, r: int, x: Union[int, float]) -> bool:
    """
    Binary search iterative approach - binary search used when list is already sorted

    O(log n) runtime, O(1) space complexity

    Args:
        arr (Union[int, float]): array of values
        l (int): left index
        r (int): right index_
        x (Union[int, float]): target value

    Returns:
        bool: found or not found
    """
    while l <= r:
        mid = (l + r) // 2

        if arr[mid] == x:
            return 1
        
        elif x < arr[mid]:
            r = mid - 1
        
        else:
            l = mid + 1
        
    return -1


def binarySearchRecursive(arr: Union[int, float], l: int, r: int, x: Union[int, float]) -> bool:
    """
    Binary search recursive implementation - binary search used when list is already sorted

    O(log n) runtime, O(log n) space complexity

    Args:
        arr (Union[int, float]): array of values
        l (int): left index
        r (int): right index_
        x (Union[int, float]): target value

    Returns:
        bool: found or not found
    """

    if l <= r:
        mid = (l + r) // 2

        if arr[mid] == x:
            return 1
        
        elif x < arr[mid]:
            return binarySearchRecursive(arr, l, mid-1, x)
        
        else:
            return binarySearchRecursive(arr, mid+1, r, x)
    
    return -1