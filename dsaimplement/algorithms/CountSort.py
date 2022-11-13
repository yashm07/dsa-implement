def countSort(arr: list[int]) -> None:
    """
    Counting sort implementation. Used when information regarding the range of values in the list is known

    O(n+k) run time, O(k) space complexity

    Args:
        arr (list[int]): list of values
    """

    output = [0] * len(arr)
    
    # only for digits 0-9
    count = [0] * 10

    for val in arr:
        count[val] += 1
    
    for j in range(1, len(count)):
        count[j] += count[j-1]
    
    for val in arr:
        output[count[val]-1] = val
        count[val] -= 1
    
    for i in range(len(arr)):
        arr[i] = output[i]