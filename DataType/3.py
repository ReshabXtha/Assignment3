# 3. Write a Python program to get a string from a given string where all
# occurrences of its first char have been changed to '$', except the first char itself.

x = 'restart'
y = x[0]
x = x.replace(y, '$')
x = y + x[1:]
print(x)
