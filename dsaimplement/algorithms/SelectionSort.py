def selectionSort(data: list[int, float]):
    """
    Selection sort implementation.

    O(n^2) run time, O(1) space complexity

    Args:
        data (list[int, float]): list with data
    Returns:
        data: sorted list
    """
    for i in range(0, len(data) - 1):
        min = i
        
        for j in range(i+1, len(data)):
            if data[j] < data[min]:
                min = j
        
        data[i], data[min] = data[min], data[i]
    
    return data


        
    