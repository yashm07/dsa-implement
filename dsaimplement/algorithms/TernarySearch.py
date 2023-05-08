from typing import Union

def ternarySearchRecursive(arr: Union[int, float], l: int, r: int, x: Union[int, float]) -> bool:
    """
    Similar to binary search, except split into 3 arrays

    O(log n) runtime, O(log n) space complexity

    Args:
        arr (Union[int, float]): array of values
        l (int): left index
        r (int): right index
        x (Union[int, float]): target value

    Returns:
        bool: found or not found
    """

    if l <= r:
        mid1 = l + (r - l) // 3
        mid2 = r - (r - l) // 3

        if arr[mid1] == x:
            return mid1
        
        elif arr[mid2] == x:
            return mid2

        if x < arr[mid1]:
            return ternarySearchRecursive(arr, l, mid1-1, x)
        
        elif x > arr[mid1] and x < arr[mid2]:
            return ternarySearchRecursive(arr, mid1+1, mid2-1, x)
        
        else:
            return ternarySearchRecursive(arr, mid2+1, r, x)

    return -1