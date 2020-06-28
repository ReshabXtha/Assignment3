# 26. Write a Python program to insert a given string at the beginning of all items in a list.
sample = [1, 2, 3, 4]
str1 = 'emp'
str2=[]
for x in sample:
    str2.append(str1+'{}'.format(x))
print(str2)
