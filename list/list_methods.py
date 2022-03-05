# create a list from string

str1 = 'abcdefghijkl'
alph = list(str1)
print(alph)

print(alph.index('j'))
alph.append('m')
print(alph)
alph.insert(1, 'A')
print(alph)

alph.remove('A')
print(alph)

# sorting the value of the list using sorting

number = [2,1,5,3,4,7,8,4]
print(number)
number.sort()
print(number)

# sorting work on alphabetical order also
spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
print(spam)
spam.sort()
print(spam)