# 22. Write a Python program to remove duplicates from a list.
str = ['red', 'white', 'black', 'red', 'green', 'black']
str1 = []
for x in str:
    if x in str1:
        str.remove(x)
    else:
        str1.append(x)
print(str)
