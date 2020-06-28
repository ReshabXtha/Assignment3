# 12. Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
def mul(n):
    n = n * 10
    return n


print("Enter the number")
m = int(input())
print(mul(m))
