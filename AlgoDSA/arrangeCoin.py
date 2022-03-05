def arrangeCoin(n):
    i = 1
    val = n
    arr = []
    if val <= 1:
        return 1
    else:
        while(i < val):
            arr.append(i)
            val = val - i
            i += 1
        

    return len(arr)

if __name__ == "__main__":
    n = 1
    print(arrangeCoin(n))