# 16. Write a Python program to sum all the items in a list.
x = [5, 43, 5, 2, 6, 8, 42, 1]
add = 0
for i in range(len(x)):
    add = add + x[i]
print('The sum of the list is', add)
