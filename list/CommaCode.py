def commaCode(arr: []):
    for idx in range(len(arr)):
        print(arr[idx])
        if arr[idx] == arr[-1]:
            print('and ' + arr[-1])
    return


def commaCode2(arr: []):
    for idx in range(len(arr)):
        if arr[idx] != arr[-1]:
            print(arr[idx])
        else:
            print('and ' + arr[-1])
    return


if __name__ == "__main__":
    spam = ['apple', 'banana', 'tofu', 'cats']
    commaCode(spam)
    commaCode2(spam)