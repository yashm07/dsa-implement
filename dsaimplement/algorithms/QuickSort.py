def partition(arr: list[float], l: int, r: int) -> int:
    """
    Performs quick sort. Selects pivot to be right-most element

    Args:
        arr (list[float]): list of values
        l (int): left index
        r (int): right index

    Returns:
        int: index of pivot
    """

    # select right-most element to be pivot
    pivot = arr[r]
    # i represents larger than pivot index
    i = l-1
    # j represents smaller than pivot index
    for j in range(l, r):
        if arr[j] <= pivot:
            i += 1
            # swap larger and smaller values
            arr[i], arr[j] = arr[j], arr[i]
    
    # place pivot in correct location
    arr[i+1], arr[r] = arr[r], arr[i+1]

    # return index of pivot
    return i+1


def quickSort(arr: list[float], l: int, r: int) -> None:
    """
    Performs quick sort recursively (divide and conquer algorithm)

    O(n log n) run time on average, O(n^2) worst case run time, O(log n) space complexity

    Args:
        arr (list[float]): list of values
        l (int): left index
        r (int): right index
    """

    if l < r:
        p = partition(arr, l, r)
        quickSort(arr, l, p-1)
        quickSort(arr, p+1, r)
