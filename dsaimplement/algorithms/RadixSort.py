def radixSort(arr: list[int]) -> None:
    """
    Radix sort implementation. Sorts by k digits, used when information regarding the range of values is known

    O(nk) run time, O(n+k) space complexity

    Args:
        arr (list[int]): array of values
    """
    max_val = max(arr)

    exp = 1
    while max_val // exp >= 1:
        countSort(arr, exp)
        exp *= 10

def countSort(arr: list[int], exp: int) -> None:
    """
    Modified counting sort 

    Args:
        arr (list[int]): list of values
    """

    output = [0] * len(arr)
    
    # only for digits 0-9
    count = [0] * 10

    for val in arr:
        index = val // exp
        count[index % 10] += 1
    
    for j in range(1, len(count)):
        count[j] += count[j-1]
    
    for val in arr:
        index = val // exp
        output[count[index % 10]-1] = val
        count[index % 10] -= 1
    
    for i in range(len(arr)):
        arr[i] = output[i]