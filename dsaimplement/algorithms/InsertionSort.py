def insertionSort(data: list[int, float]):
    """
    Implementation for insertion sort. Works great when lists are almost sorted
    or when a list is small in length

    O(n^2) run time, O(1) space complexity

    Args:
        data (list[int, float]): list with data

    Returns:
        data: sorted list
    """
    
    for i in range(1, len(data)):
        temp = data[i]

        j = i
        while (data[j-1] > temp and j > 0):
            data[j] = data[j-1]
            j -= 1
        
        data[j] = temp
    
    return data
