# 16. Write a Python program to square and cube every number in a given list of integers using Lambda.
lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sq = lambda x: x * x
i = map(sq, lis)
print(list(i))
cu = lambda x: x * x * x
i = map(cu, lis)
print(list(i))
