from itertools import permutations
from PyDictionary import PyDictionary

dictionary=PyDictionary()
str1 = input("Enter a small string to check for words: ")
l = list(permutations(range(0, len(str1))))

for j in l:
    temp = ''
    for k in j:
        temp = temp + str1[k]

    if dictionary.meaning(temp) is not None:
        print(temp)
        print(dictionary.meaning(temp))
