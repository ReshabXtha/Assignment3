# 25. Write a Python program to check whether all dictionaries in a list are empty or not
lis1 = [{}, {}, {}]
lis2 = [{1, 2}, {}, {}]
print(all(not d for d in lis1))
print(all(not d for d in lis2))
