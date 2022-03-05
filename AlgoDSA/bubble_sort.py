import sys

def bubble_sort(arr):
    length = len(arr)
    for i in range(0, length-1):
        for j in range(0, length-i-1):
            if arr[j] > arr[j+1]:
                flag = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = flag
    return arr
if __name__ == "__main__":
    arr = [60,50,95,80,70]
    print(bubble_sort(arr)) 