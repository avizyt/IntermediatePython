def copy2Array(arr):
    N = len(arr)
    b = []
    i = 0
    while i< N-1:
        b[i] = arr[i]
        i += 1
    return b

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    print(copy2Array(arr))