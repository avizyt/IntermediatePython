


def searchRange(nums, target):
    ans = [-1,-1]
    start = search(nums, target, True)
    end = search(nums, target, False)
    ans[0] = start
    ans[1] = end
    return ans
    


def search(nums, target, findStartIndex):
    ans = -1
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = start + (end-start)//2

        if (target < nums[mid]):
            end = mid -1
        elif(target > nums[mid]):
            start = mid+1
        else:
            ans = mid
            if (findStartIndex):
                end = mid-1
            else:
                start = mid + 1
    return ans


if __name__ == "__main__":
    arr = [5,7,7,8,8,10]
    target = 7
    print(searchRange(arr, target))