# 11. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and print the result.
add = lambda a: a + 15
r = add(5)
print(r)
mul = lambda a, b: a * b
r = mul(5, 10)
print(r)
