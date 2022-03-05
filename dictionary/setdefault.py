spam = {'name': 'Jhon', 'age': 25}

if 'color' not in spam:
    spam['color'] = 'black'
print(spam)

spam.setdefault('height', '5.5ft')
print(spam)

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}


for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
print(count)