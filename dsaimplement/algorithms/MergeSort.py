def merge(arr: list[int, float], l: int, m: int, r: int, order: str):
    """
    Merges two sublists together into sorted list

    Args:
        arr (list): list of values
        l (int): left index
        m (int): middle index
        r (int): right index
        order (str): order of values
    """
    # determine length of sublists
    n1 = m - l + 1
    n2 = r - m

    # create lists
    L = [0] * n1
    R = [0] * n2

    # copy values over
    for i in range(n1):
        L[i] = arr[l + i]
    
    for j in range(n2):
        R[j] = arr[m + 1 + j]
    
    # index for sublists
    i = 0
    j = 0
    # index for merged list
    k = l

    # sort sublists and merge sorted lists
    while (i < n1) and (j < n2):
        if compare(order, L, R, i, j):
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        
        k += 1
    
    # copy any remaining elements from L list
    while (i < n1):
        arr[k] = L[i]
        i += 1
        k += 1
    
    # copy any remaining elements from R list
    while (j < n2):
        arr[k] = R[j]
        j += 1
        k += 1

def compare(order, L, R, i, j) -> bool:
    """
    Allows user to select increasing or decreasing order, adjusts conditional statement
    
    Returns:
        bool: True/False
    """
    if order == "increasing":
        return L[i] <= R[j]
    else:
        return L[i] >= R[j]

def mergeSort(arr: list[int, float], l: int, r: int, order: str = "increasing"):
    """
    Merge sort implementation

    O(nlogn) run time, O(n) space complexity

    Args:
        arr (list): array of values
        l (int): left index
        r (int): right index
        order (str, optional): Set desired order. Defaults to "increasing".
    """
    if l < r:
        # calculate new middle
        m = (l+r-1)//2

        mergeSort(arr, l, m, order)
        mergeSort(arr, m+1, r, order)
        merge(arr, l, m, r, order)
