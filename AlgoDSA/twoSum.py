def search(arr, target, s, e):
    while s <= e:
        m = s + (e-s)//2;
        if target < arr[m]:
            e = m - 1
        elif target > arr[m]:
            s = m+ 1
        else:
            return m
    return -1;

def twoSum(arr, target):
    first = 0;
    end = len(arr) -1;
    new_target = target - arr[first]
    output = []
    
    second = search(arr, new_target, first, end)
    if second == -1:
        first += 1
        second = search(arr,new_target,first, end )
    else:
        output.append(first+1)
        output.append(second+1)
    
    return output

def twoSum2(arr, target):
    d = {}
    for i in range(len(arr)):
        if arr[i] in d:
            return [d[arr[i]], i]
        else:
            d[target - arr[i]] = i



if __name__ == "__main__":
    arr = [2,3,4]
    target = 6
    print(twoSum(arr, target))
    print(twoSum2(arr, target))