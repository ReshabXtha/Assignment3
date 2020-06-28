# 20. Write a Python program to find intersection of two given arrays using Lambda.
a1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a2 = [11, 21, 5, 3, 8, 4, 21]
result = list(filter(lambda x: x in a1, a2))
print("Intersection : ", result)
