
# Implementation of recursion Binary Search

def recursiveBS(arr: list, target: int, start: int, end: int):
    '''Binary Search in an array using recursion.
    arr:: list
    target:: target element in Array
    start:: Starting index of array
    end:: End index of array
    '''

    # if start index is greater than end index
    # return target not found or -1
    if (start> end):
        return -1
    mid = start + ( end - start)//2

    # if middle element of the array is the target element
    # return middle index or mid

    if (arr[mid] == target):
        return mid
    
    # if target less than the middle element of the array
    # return the recursion function with start = start 
    # but end = mid -1 
    if (target < arr[mid]):
        return recursiveBS(arr, target, start, mid-1)
    # if target is greater than the middle elemnet
    # return the recursion function with start = mid + 1
    # but end = end.
    else:
        return recursiveBS(arr, target, mid+1, end)



if __name__ == "__main__":
    arr = [-18, -12, -4, 0, 2, 3, 4, 15, 16, 18, 22, 45, 89]
    target = 16
    start = 0
    end = len(arr)-1
    found = recursiveBS(arr, target, 0, end)
    print(f"The target element's index: {found}")