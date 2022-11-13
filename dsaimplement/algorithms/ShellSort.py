def shellSort(arr: list[int], incr_list: list[int], order: str = "increasing") -> None:
    """
    Shell sort implementation. Based off of insertion sort, except breaks list into sublists
    (makes list shorter, and sorts elements far apart from each other)

    Depending on increment selections, time complexity can vary

    For Hibbard's increment, worse case is O(n^(3/2)), space complexity is always O(1)

    Overall, worst case is O(n^2) and best case O(nlog n)

    Args:
        arr (list[int]): list of values
        incr_list (list[int]): increment values
        order (str, optional): Specifies order sequence. Defaults to "increasing".
    """
    for incr in incr_list:
        insertionSort2(arr, incr, order)

def insertionSort2(arr: list[int], incr: int, order: str) -> None:
    """
    Slight modification from regular insertion sort - just accounts for increment

    Args:
        arr (list[int]): list of values
        incr (int): increment values
        order (str): order sequence
    """
    for i in range(1, len(arr)):
        temp = arr[i]

        j = i
        while (compare(arr, j, incr, temp, order) and j >= incr):
            arr[j] = arr[j-incr]
            j -= incr
        
        arr[j] = temp

def compare(arr, j, incr, temp: int, order: str) -> None:
    """
    Determines which truth condition to use depending on order required
    """
    return (arr[j-incr] > temp if order == "increasing" else arr[j-incr] < temp)
