spam = {'color': 'red', 'age': 42}

for val in spam.values():
    print(val)

for key in spam.keys():
    print(key)

for key, val in spam.items():
    print(f"{key}:{val}")

print(spam.get('color',0))
print(spam.get('name', 'Jhon Doe'))