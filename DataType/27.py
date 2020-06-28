# 27. Write a Python program to replace the last element in a list with another list.
sam1 = [1, 3, 5, 7, 9, 10]
sam2 = [2, 4, 6, 8]
sam1.pop()
for x in sam2:
    sam1.append(x)
print(sam1)
