arr = [1,2,3,4,5,6,7,8,9,10]
even_idx = []
odd_idx = []
for idx, val in enumerate(arr):
    if idx % 2 == 0:
        even_idx.append((idx,val))
    else:
        odd_idx.append((idx,val))
print(arr)
print(even_idx)
print(odd_idx)