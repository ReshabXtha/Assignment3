# 10. Write a Python program to remove the characters which have odd index values of a given string
print('Enter the string:')
str = input()
str1 = ""
for i in range(0, len(str)):
    if i % 2 == 0:
        str1 = str1 + str[i]
print(str1)
