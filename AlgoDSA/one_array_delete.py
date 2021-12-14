import sys
def delet(arr, deletIdx):
    length = len(arr)
    tempArr = [0 for _ in range(length-1)]

    for i in range(0, length):
        if i< deletIdx:
            tempArr[i] = arr[i]