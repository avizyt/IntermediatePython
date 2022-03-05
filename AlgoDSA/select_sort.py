# Sort an array by repeatedly finding the minimum element from unsorted part and putting it at the beginning.

def selectSort(arr):
    length = len(arr) -1
    min_idx = 0
    for i in range(0,length):
        min_idx = i
        min_val = arr[min_idx]
        for j in range(i, length):
            if min_val > arr[j+1]:
                min_val = arr[j+1]
                min_idx = j+1
        if i != min_idx:
            temp = arr[i]
            arr[i] = arr[min_idx]
            arr[min_idx] = temp
    return arr

if __name__ == "__main__":
    arr = [60,50,50,95,80,70]
    print(selectSort(arr))