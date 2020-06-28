# 8. Write a Python program to remove the nth index character from a nonempty string.
print('Enter the string:')
str = input()
x = len(str)
if x == 0:
    print('Empty string')
else:
    str = str[:x-1]
print(str)
