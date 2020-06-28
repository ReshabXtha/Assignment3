# 18. Write a Python program to check whether a given string is number or not using Lambda.
str1 = "123456"
start_with = lambda x: True if x.isdigit() else False
str2 = start_with(str1)
print(str2)
