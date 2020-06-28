# 17. Write a Python program to multiplies all the items in a list
x = [5, 43, 5, 2, 6, 8, 42, 1]
mul = 1
for i in range(len(x)):
    mul = mul * x[i]
print('The product of the list is', mul)
