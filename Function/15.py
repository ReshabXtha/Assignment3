# 15. Write a Python program to filter a list of integers using Lambda.
even = lambda x: x % 2 == 0
lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = filter(even, lis)
print(list(i))
