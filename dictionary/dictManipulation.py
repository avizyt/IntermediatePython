x = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

x_up = list(x)
x_lo = list(x.lower())
# print(len(x_up))

x_up_dict = {}
x_lo_dict = {}
for i in range(len(x_up)):
    x_up_dict[x_up[i]] = i
# print(x_up_dict)

for i in range(len(x_lo)):
    x_lo_dict[x_lo[i]] = i
# print(x_lo_dict)

for k, v in x_lo_dict.items():
    x_lo_dict[k] = v+26
# print(x_lo_dict)
for val in x_lo_dict.values():
    print(val)
