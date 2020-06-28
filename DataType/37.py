#37. Write a Python program to multiply all the items in a dictionary.
dic = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
mul=1
for x in dic.values():
    mul= mul * x
print(mul)