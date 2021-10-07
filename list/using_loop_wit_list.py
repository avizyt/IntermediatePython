supplies = ['model', 'frame', 'paints', 'brush', 'papers']
for i in range(len(supplies)):
    print(f"Index: {str(i)} in supplies is: {supplies[i]}")



if __name__ == "__main__":
    # validate item in the list using in and not in Operator
    bool1 = 'frame' in supplies
    print(bool1)

    bool2 = 'oil Paint' not in supplies
    print(bool2)

    alphabet = ['a', 'b','c','d','e','f']
    print("Enter a alphabet: ")
    name = input()
    if name not in alphabet:
        print('I do know it ' + name)
    else:
        print("Hurrh! you know "+ name)