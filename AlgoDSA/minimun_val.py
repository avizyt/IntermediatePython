def minimunVal(arr):
    min_idx = 0
    length = len(arr)-1
    for i in range(1, length):
        if arr[min_idx] > arr[i]:
            temp = arr[min_idx]
            arr[min_idx] = arr[i]
            arr[i] = temp

    minVal = arr[min_idx]
    return minVal

if __name__ == "__main__":
    arr = [60,50,50,95,80,70]
    print(minimunVal(arr))