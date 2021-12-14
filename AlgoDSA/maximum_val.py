
def max_val(arr):
    arr_size = len(arr)-1
    for i in range(0, arr_size):
        if arr[i] > arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
    print(arr)
    maxValue = arr[arr_size]    
    return maxValue

if __name__ == "__main__":
    arr = [5,4,7,6,3,2,19,15,11,17,14]
    print(max_val(arr))
