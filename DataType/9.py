# 9. Write a Python program to change a given string to a new string where the first and last chars have been exchanged.

print('Enter the string:')
str = input()
n = len(str)
if n == 0:
    print('Empty string')
else:
    str = str[n - 1] + str[1:(n - 2)] + str[0]
    print(str)
