def bubbleSort(data: list[int, float]):
    """
    Bubble sort implementation. Optimized approach - considers when list is sorted, and does not 
    check already sorted values (large values bubbled to the end)

    O(n^2) run time, O(1) space complexity

    Args:
        data (list[int, float]): list with data

    Returns:
        data: sorted
    """

    done = False
    count = 0

    while (done == False):
        done = True

        for i in range(0, len(data)-1-count):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                done = False
        count += 1
    
    return data

        
