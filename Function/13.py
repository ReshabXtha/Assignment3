# 13. Write a Python program to sort a list of tuples using Lambda
lis = [(1, 2), (2, 3), (4, 5), (7, 8, 5), (6, 4)]
print(lis)
lis.sort(key=lambda x: x[1])
print(lis)
