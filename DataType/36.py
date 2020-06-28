#36. Write a Python program to sum all the items in a dictionary.
dic = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
sum=0
for x in dic.values():
    sum=sum+x
print(sum)