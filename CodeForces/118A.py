# Author: Abshar Mohammed Aslam, github.com/abxhr

s = list(input())
vowels = ['a', 'e', 'i', 'y', 'o', 'u', 'A', 'E', 'I', 'O', 'U', 'Y']
str = ""
for letter in s:
    if letter not in vowels:
        str += '.'
        if letter.isupper():
            str += letter.lower()
        else:
            str += letter
print(str)