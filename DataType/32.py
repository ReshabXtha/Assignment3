# 32. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
n = 5
dic = {}
for i in range(1, n):
    dic[i] = i * i
print(dic)
